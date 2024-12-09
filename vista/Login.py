import tkinter as tk
from tkinter import *
from controlador.Jugador import Jugador

class Login():

    def ingresarNombre(self, event):
        self.nombre = self.nombreEntry.get()
    
    def ingresarClave(self, event):
        self.clave = self.pwEntry.get()

    def iniciarSesion(self, event):
        if self.nombre and self.clave:
            try:
                mijugador = Jugador().iniciar_sesion(self.nombre, self.clave)
                if mijugador:
                    self.root.setJugador(mijugador)
                    self.ventana.destroy()
                else:
                    self.lblErr.config(text="Error en la base de datos. Verifique la conexión")
            except Exception as e:
                self.lblErr.config(text=e)
        else:
            self.lblErr.config(text="Campos faltantes.\nDebes ingresar tu nombre y contraseña.")

    def cerrar(self):
        self.root.login = False
        self.ventana.destroy()

    def __init__(self, root):
        self.root = root
        self.ventana = Toplevel(root.ventana)
        self.ventana.title("Iniciar Sesión")
        self.ventana.geometry("300x300")

        self.nombre = ""
        self.clave = ""

        self.lblTitulo = Label(self.ventana, text="Iniciar Sesión")
        self.lblTitulo.pack(pady=20)

        self.nombreLabel = Label(self.ventana, text="Nombre:*")
        self.pwLabel = Label(self.ventana, text="Contraseña:*")

        

        self.nombreLabel.pack()
        self.nombreEntry = Entry(self.ventana)
        self.nombreEntry.pack()

        self.pwLabel.pack()
        self.pwEntry = Entry(self.ventana, show="*")
        self.pwEntry.pack()
        
        self.lblErr = Label(self.ventana, text="", fg="red")
        self.lblErr.pack(pady=5)

        self.btnLogin = Button(self.ventana, text="Iniciar Sesión")
        self.btnLogin.pack(pady=10)

        self.btnLogin.bind("<Button-1>", self.iniciarSesion)

        self.nombreEntry.bind("<KeyRelease>", self.ingresarNombre)
        self.pwEntry.bind("<KeyRelease>", self.ingresarClave)


        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar)
