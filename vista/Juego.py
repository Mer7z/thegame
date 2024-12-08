from tkinter import *
import tkinter as tk


class Juego():
    def __init__(self, root, jugador):
        self.root = root
        self.jugador = jugador
        
        self.canvas = Canvas(self.root, bg="black")
        self.canvas.place(x=0, y=0, relheight=1, relwidth=1)