from tkinter import *
import tkinter as tk
import random


class Juego():
    def __init__(self, root, jugador):
        self.root = root
        self.jugador = jugador

        self.root.bind("<KeyPress>", self.presionarTecla)
        
        self.canvas = Canvas(self.root, bg="black")
        self.canvas.place(x=0, y=0, relheight=1, relwidth=1) #ventana es 600x500

        self.dibujar_estrellas()

    def presionarTecla(self, event):
        print(event.keysym)

    def dibujar_estrellas(self):
        self.canvas.delete("estrellas")
        for _ in range(40):
            x = random.randint(0, 600)
            y = random.randint(0, 500)
            t = 2

            self.canvas.create_oval(x, y, x+t, y+t, fill="#adadad", outline="",tags="estrellas")