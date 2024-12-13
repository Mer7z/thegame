from vista.Objeto import Objeto
from vista.Bala import Bala
from tkinter import PhotoImage
import pygame

class Nave(Objeto):

    pygame.mixer.init()

    sonido_nave = pygame.mixer.Sound(r"sonidos\sonidonave.mp3")
    sonido_muere = pygame.mixer.Sound(r"sonidos\explosion_nave.mp3")

    def __init__(self, root, x, y, size = 20, tag = ""):
        super().__init__(root, x, y)
        self.size = size
        self.tag = tag
        self.objeto_canvas = None
        self.coordenadas = []
        self.image = PhotoImage(file="avatars/nave (1).png")  # Cargar la imagen de la nave
        self.image = self.image.subsample(2, 2) # Reduce el tamaño de la imagen
        self.image_width = self.image.width()  # Obtener el ancho de la imagen
        self.image_height = self.image.height() 
        self.sonido_nave.play(loops=-1)
        

    def dibujar(self):
        if self.destruyendo:
            self.canvas.delete(self.objeto_canvas)
            return
        if not self.objeto_canvas:
            # Usar create_image para dibujar la imagen
            self.objeto_canvas = self.canvas.create_image(self.x, self.y, image=self.image, tags=self.tag)
        else:
            self.canvas.coords(self.objeto_canvas, self.x, self.y)
        self.coordenadas = self.canvas.bbox(self.objeto_canvas)
    
    def procesarCuadro(self, delta):                                                                
        pass

    def disparar(self, asteroide):
        dnx = self.x
        dny = self.y
        dax = asteroide.x
        day = asteroide.y
        self.root.objetos.append(Bala(self.root, dnx, dny, dax, day))
    
    def morir(self):
        self.destruir()
        self.root.fin_juego()
        self.dibujar()
        self.sonido_nave.stop()
        self.sonido_muere.play()
    