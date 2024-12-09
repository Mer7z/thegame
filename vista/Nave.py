from vista.Objeto import Objeto
from vista.Bala import Bala

class Nave(Objeto):
    def __init__(self, root, x, y, size = 20, tag = ""):
        super().__init__(root, x, y)
        self.size = size
        self.tag = tag
        self.objeto_canvas = None
        self.coordenadas = []



    def dibujar(self):
        if not self.objeto_canvas:
            self.objeto_canvas = self.canvas.create_rectangle(self.x, self.y, self.x+self.size, self.y+self.size, fill="#28bf50", outline="white", tags=self.tag)
        else:
            self.canvas.coords(self.objeto_canvas, self.x, self.y, self.x+self.size, self.y+self.size)
        self.coordenadas = self.canvas.bbox(self.objeto_canvas)
    
    def procesarCuadro(self, delta):                                                                
        pass
    
    def destruir(self):
        self.canvas.delete(self.objeto_canvas)

    def disparar(self, asteroide):
        dnx = self.x + (self.coordenadas[2] - self.x) / 2
        dny = self.y + (self.coordenadas[3] - self.y) / 2
        dax = asteroide.x + (asteroide.coordenadas[2] - asteroide.x) / 2
        day = asteroide.y + (asteroide.coordenadas[3] - asteroide.y) / 2
        self.root.objetos.append(Bala(self.root, dnx, dny, dax, day))
    