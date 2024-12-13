from vista.Objeto import Objeto
import os
from tkinter import PhotoImage
import math

class Explosion(Objeto):
    def __init__(self, root, x, y):
        super().__init__(root, x, y)
        self.sprites = self.cargar_sprites("avatars/explosion")
        self.contador = 0
        self.frame = 0
        self.max_frames = len(self.sprites) - 1
        self.objeto_canvas = None

    def cargar_sprites(self, carpeta):    
        sprites = []
        formatos = (".png", ".jpg", ".jpeg", ".gif")
        for archivo in os.listdir(carpeta):
            if archivo.lower().endswith(formatos):
                ruta_completa = os.path.join(carpeta, archivo)
                imagen = PhotoImage(file=ruta_completa)
                imagen = imagen.subsample(2, 2)
                sprites.append(imagen)
        return sprites


    def dibujar(self):
        if self.destruyendo:
            self.canvas.delete(self.objeto_canvas)
            for objeto in self.root.objetos:
                if objeto == self:
                    self.root.objetos.remove(objeto)
                    break
            return

        if not self.objeto_canvas:
            self.objeto_canvas = self.canvas.create_image(self.x, self.y, image=self.sprites[self.frame])
        else:
            self.canvas.itemconfig(self.objeto_canvas, image=self.sprites[self.frame])
        

    def procesarCuadro(self, delta):
        if self.frame < self.max_frames:
            self.contador += delta * 12
            self.frame = math.floor(self.contador)
        else:
            self.frame = self.max_frames
            self.destruir()