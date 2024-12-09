from vista.Objeto import Objeto

class Nave(Objeto):
    def __init__(self, root, x, y, size = 20, tag = ""):
        super().__init__(root, x, y)
        self.size = size
        self.tag = tag
        self.objeto_canvas = None



    def dibujar(self):
        if not self.objeto_canvas:
            self.objeto_canvas = self.canvas.create_rectangle(self.x, self.y, self.x+self.size, self.y+self.size, fill="#28bf50", outline="white", tags=self.tag)
        else:
            self.canvas.coords(self.objeto_canvas, self.x, self.y, self.x+self.size, self.y+self.size)
    
    def procesarCuadro(self, delta):                                                                
        pass
    
    def destruir(self):
        self.canvas.delete(self.objeto_canvas)
    