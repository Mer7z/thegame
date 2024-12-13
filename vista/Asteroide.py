from vista.Objeto import Objeto
from vista.Texto import Texto
import random
from tkinter import PhotoImage
import pygame
from vista.Explosion import Explosion

class Asteroide(Objeto):

    pygame.mixer.init()
    sonido_exp_asteroide = pygame.mixer.Sound(r"sonidos\impacto.mp3")

    def __init__(self, root, x, y, nave, size = 20, velocidad = 40, palabra = "", puntos = 100, tag = ""):
        super().__init__(root, x, y)
        self.nave = nave
        self.coordenadas = []
        self.distancia = None
        self.size = size
        self.tag = tag
        self.objeto_canvas = None
        self.seleccionado = False
        self.puntos = puntos
        

        self.palabra = palabra
        self.velocidad = velocidad


        self.image1 = PhotoImage(file="avatars/mine.png")
        self.image2 = PhotoImage(file="avatars/oppressor.png")

        self.image = random.choice([self.image1, self.image2])

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
            self.root.objetos.append(Explosion(self.root, self.x, self.y))
            return
        if not self.objeto_canvas:
            self.objeto_canvas = self.canvas.create_image(self.x, self.y, image=self.image, tags=self.tag)
        else:
            self.canvas.coords(self.objeto_canvas,self.x, self.y)

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
            
        self.chocar()

    def seleccionar(self, selec):
        self.seleccionado = selec
        for h in self.hijos:
            h.selec = selec
    
    def recibir_disparo(self, letra):
        if self.palabra.lower().startswith(letra):
            self.palabra = self.palabra[1:]
            if not self.palabra:
                self.root.add_kill(self.puntos)
                self.destruir()
                self.sonido_exp_asteroide.play()
            return True
        else:
            return False
    
    def chocar(self):
        x1, y1, x2, y2 = self.coordenadas

        nave_x1, nave_y1, nave_x2, nave_y2 = self.nave.coordenadas

        if (x1 < nave_x2 and x2 > nave_x1 and y1 < nave_y2 and y2 > nave_y1):    
            self.nave.morir()
            self.destruir()