from vista.Objeto import Objeto
import pygame

class Bala(Objeto):

    pygame.mixer.init()

    sonido_bala = pygame.mixer.Sound(r"sonidos\laser.mp3")

    def __init__(self, root, x, y, x2, y2, width= 3):
        super().__init__(root, x, y)
        self.objeto_canvas = None
        self.x2 = x2
        self.y2 = y2
        self.width = width
        self.sonido_bala.play()
        self.tiempo = 0.2

    def dibujar(self):
        if self.destruyendo:
            self.canvas.delete(self.objeto_canvas)
            for objeto in self.root.objetos:
                if objeto == self:
                    self.root.objetos.remove(objeto)
                    break
            return
        if not self.objeto_canvas:
            self.objeto_canvas = self.canvas.create_line(self.x, self.y, self.x2, self.y2, width=self.width, fill="#00ffea")
        else:
            self.canvas.coords(self.objeto_canvas, self.x, self.y, self.x2, self.y2)
        
        self.canvas.tag_lower(self.objeto_canvas)


    def procesarCuadro(self, delta):
        if self.tiempo <= 0:
            self.destruir()
        else:
            self.tiempo -= delta
