from tkinter import *
from tkinter import messagebox
import tkinter as tk
from vista.Login import Login

class Ventana():

    def iniciarSeccion(self):
        if not self.login:
            self.login = Login(self)
    
    def setJugador(self, jugador):
        self.jugador = jugador
        if self.login:
            self.login = None

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("The Game") # Ponganle un titulo
        self.ventana.geometry("400x300")
        self.ventana.resizable(0,0)

        self.login = None
        self.jugador = None

        self.label = Label(self.ventana, text="Naves y Asteroides: El Juego")
        self.label.pack()
        self.loginBtn = Button(self.ventana, text="Iniciar Sección", command=self.iniciarSeccion)
        self.loginBtn.pack()

        self.regisBtn = Button(self.ventana, text="Registrarse")
        self.regisBtn.pack()


        self.ventana.mainloop()