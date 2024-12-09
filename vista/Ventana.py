from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from vista.Login import Login
from vista.Registro import Registro
from vista.Juego import Juego
from controlador.Jugador import Jugador

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
        self.juego = Juego(self, self.jugador)
        self.juego.iniciar()

    def reiniciar_juego(self):
        if self.juego:
            self.juego.detener()
            self.juego = Juego(self, self.jugador)
            self.juego.iniciar()

    def salir_juego(self):
        if self.juego:
            self.juego.detener()
            self.juego = None
            self.ventana.config(width=400, height=400)
            self.ingresar_datos_tabla()
            self.frInicio.place(relx=0.5, rely=0.4, anchor="center")
    def cerrar(self):
        if self.juego:
            self.juego.detener()
        self.ventana.destroy()
    
    def obtener_jugadores(self):
        try:
            return Jugador().obtener_jugadores()
        except:
            return []

    def ingresar_datos_tabla(self):
        self.datos = self.obtener_jugadores()

        for item in self.tabla.get_children():
            self.tabla.delete(item)
            
        if len(self.datos) > 0:
            for dato in self.datos:
                jugador = dato[1]
                puntaje = dato[3]
                self.tabla.insert("", "end", values=(jugador, puntaje))

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("The Game") # Ponganle un titulo
        self.ventana.config(width=400, height=400)
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

        self.tabla = ttk.Treeview(self.frInicio, columns=("Jugador", "Puntaje"), show="headings", height=10)

        # Configuración de encabezados
        self.tabla.heading("Jugador", text="Jugador")
        self.tabla.heading("Puntaje", text="Puntaje")
        self.tabla.column("Jugador", width=150, anchor="center")
        self.tabla.column("Puntaje", width=100, anchor="center")

        # Scrollbar vertical
        scrollbar = ttk.Scrollbar(self.frInicio, orient=tk.VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)

        # Empaquetar widgets
        self.tabla.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.datos = []
        
        self.ingresar_datos_tabla()

        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar)

        self.ventana.mainloop()