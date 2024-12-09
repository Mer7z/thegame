from tkinter import *
from tkinter import messagebox
import tkinter as tk
from vista.Login import Login
from vista.Registro import Registro
from vista.Juego import Juego

class Ventana():

    def iniciarSesion(self):
        if not self.login:
            self.login = True
            Login(self).ventana.mainloop()

    def registrar(self):
        if not self.login:
            self.login = True
            Registro(self).ventana.mainloop()
    
    def setJugador(self, jugador):
        self.jugador = jugador
        self.iniciar_Juego()
        if self.login:
            self.login = False

    def iniciar_Juego(self):
        self.frInicio.place_forget()
        self.ventana.config(width=600, height=500)
        self.juego = Juego(self.ventana, self.jugador)
        self.juego.iniciar()

    def cerrar(self):
        if self.juego:
            self.juego.detener()
        self.ventana.destroy()

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("The Game") # Ponganle un titulo
        self.ventana.config(width=400, height=300)
        # self.ventana.geometry("400x300")
        self.ventana.resizable(0,0)

        self.login = False
        self.jugador = None
        self.juego = None

        self.frInicio = Frame(self.ventana)
        self.frInicio.place(relx=0.5, rely=0.4, anchor="center")

        self.label = Label(self.frInicio, text="Naves y Asteroides: El Juego")
        self.label.pack()
        self.loginBtn = Button(self.frInicio, text="Iniciar Sesión", command=self.iniciarSesion)
        self.loginBtn.pack()

        self.regisBtn = Button(self.frInicio, text="Registrarse", command=self.registrar)
        self.regisBtn.pack()

        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar)

        self.ventana.mainloop()