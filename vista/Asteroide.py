from vista.Objeto import Objeto

class Asteroide(Objeto):
    def __init__(self, root, x, y, size = 20, tag = ""):
        super().__init__(root, x, y)
        self.size = size
        self.tag = tag
        self.objeto_canvas = None

        self.direccion = 1

        self.setInputTeclado(self.precionarTecla)
    
    def precionarTecla(self, event):
        if event.keysym == "a":
            self.direccion = -1
        if event.keysym == "d":
            self.direccion = 1

    def dibujar(self):
        if not self.objeto_canvas:
            self.objeto_canvas = self.canvas.create_rectangle(self.x, self.y, self.x+self.size, self.y+self.size, fill="#8f2525", outline="black", tags=self.tag)
        else:
            self.canvas.coords(self.objeto_canvas, self.x, self.y, self.x+self.size, self.y+self.size)
    
    def procesarCuadro(self, delta):
        self.x += (10 * delta) * self.direccion
    
    def destruir(self):
        self.canvas.delete(self.objeto_canvas)
    