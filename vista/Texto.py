from tkinter import Canvas

class Texto():
    def __init__(self, padre, x, y, seleccionado = False, tamFuente = 13):
        self.padre = padre
        self.canvas: Canvas = padre.canvas
        self.x = x
        self.y = y
        self.texto = None
        self.fondo = None
        self.tamFuente = tamFuente
        self.selec = seleccionado

    def dibujar(self):
        if self.padre.destruyendo:
            if self.texto and self.fondo:
                self.canvas.delete(self.fondo)
                self.canvas.delete(self.texto)
            return
        if not self.texto:
            self.texto = self.canvas.create_text(self.x+self.padre.x, self.y+self.padre.y, text=self.padre.palabra.lower(), font=("Arial", self.tamFuente), fill="black", anchor="w")
        else:
            self.canvas.itemconfig(self.texto, text=self.padre.palabra.lower())
            self.canvas.coords(self.texto, self.x+self.padre.x, self.y+self.padre.y)

            x1 = self.canvas.bbox(self.texto)[0] - 2
            y1 = self.canvas.bbox(self.texto)[1] - 2
            x2 = self.canvas.bbox(self.texto)[2] + 2
            y2 = self.canvas.bbox(self.texto)[3] + 2
            if not self.fondo:
                self.fondo = self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="")
            else:
                self.canvas.coords(self.fondo, x1, y1, x2, y2)
        if self.texto and self.fondo:
            if self.selec:
                self.canvas.itemconfig(self.texto, fill="white")
                self.canvas.itemconfig(self.fondo, fill="#66ff52")
            else:
                self.canvas.itemconfig(self.texto, fill="black")
                self.canvas.itemconfig(self.fondo, fill="white")
            
            self.canvas.tag_raise(self.texto, self.padre.objeto_canvas)
            self.canvas.tag_raise(self.fondo, self.padre.objeto_canvas)
            self.canvas.tag_raise(self.texto, self.fondo)
        
