from tkinter import Canvas

class Objeto():
    def __init__(self, root, x, y):
        self.root = root
        self.canvas : Canvas = root.canvas
        self.setInputTeclado = root.set_evento_teclado
        self.x = x
        self.y = y
        self.destruyendo = False


    def dibujar(self):
        pass

    def procesarCuadro(self):
        pass

    def destruir(self):
        self.destruyendo = True