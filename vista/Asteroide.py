from vista.Objeto import Objeto
from vista.Texto import Texto

class Asteroide(Objeto):
    def __init__(self, root, x, y, nave, size = 20, velocidad = 40, tag = ""):
        super().__init__(root, x, y)
        self.nave = nave
        self.coordenadas = []
        self.distancia = None
        self.size = size
        self.tag = tag
        self.objeto_canvas = None
        self.seleccionado = False
        

        self.palabra = "Hello"
        self.velocidad = velocidad

        self.hijos = [
            Texto(self, 17, 17, self.seleccionado)
        ]
        self.dibujar()

    def dibujar(self):
        if self.destruyendo:
            for h in self.hijos:
                h.dibujar()
                del h

            self.canvas.delete(self.objeto_canvas)

            if self.root.selAsteroide == self:
                self.root.selAsteroide = None
            
            for objeto in self.root.objetos:
                if objeto == self:
                    self.root.objetos.remove(objeto)
                    break
            return
        if not self.objeto_canvas:
            self.objeto_canvas = self.canvas.create_rectangle(self.x, self.y, self.x+self.size, self.y+self.size, fill="#8f2525", outline="black", tags=self.tag)
        else:
            self.canvas.coords(self.objeto_canvas, self.x, self.y, self.x+self.size, self.y+self.size)

        self.coordenadas = self.canvas.bbox(self.objeto_canvas)

        if len(self.hijos) > 0:
            for h in self.hijos:
                h.dibujar()
    
    def procesarCuadro(self, delta):
        dx = self.nave.x - self.x
        dy = self.nave.y - self.y

        self.distancia = (dx**2 + dy**2)**0.5
        if self.distancia > 1:
            paso_x = (self.velocidad * delta) * dx / self.distancia
            paso_y = (self.velocidad * delta) * dy / self.distancia

            self.x = self.x + paso_x
            self.y = self.y + paso_y
        

    def seleccionar(self, selec):
        self.seleccionado = selec
        for h in self.hijos:
            h.selec = selec
    
    def recibir_disparo(self, letra):
        if self.palabra.lower().startswith(letra):
            self.palabra = self.palabra[1:]
            if not self.palabra:
                self.root.add_kill()
                self.destruir()
            return True
        else:
            return False
    