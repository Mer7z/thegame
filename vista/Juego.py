from tkinter import *
import tkinter as tk
import random
from vista.Asteroide import Asteroide
from vista.Nave import Nave
from vista.Bala import Bala
import time
import math
import threading as th

class Juego():
    def __init__(self, root, jugador):
        self.root = root
        self.ventana = root.ventana
        self.jugador = jugador
        
        self.ejecutar = True
        self.fotograma = 0.016
        self.eventosTecla = []

        self.frJuego = Frame(self.ventana)
        self.frJuego.place(x=0, y=0, relheight=1, relwidth=1)
        
        self.canvas = Canvas(self.frJuego, bg="black")
        self.canvas.place(x=0, y=0, relheight=1, relwidth=1) #ventana es 600x500

        self.dibujar_estrellas()

        self.tiempo = 0
        self.puntos = 0
        self.contadorKills = 0
        self.kills = 0
        self.dificultad = 0
        self.palabras = [
            [100,"casa", "luna", "pato", "flor", "vida", "rana", "mesa", "gato", "tiza", "azul"],  # 4 letras
            [200,"raton", "globo", "hojas", "cielo", "piano", "plaza", "nieve", "luzar", "rojas", "leche"],  # 5 letras
            [300,"frutas", "lucero", "madera", "camino", "sender", "quesos", "cocina", "viajes", "limpie", "calend"],  # 6 letras
            [500,"ventana", "milagro", "librera", "pastora", "amapola", "camaron", "espejos", "barroco", "cabezas", "sombrer"],  # 7 letras
            [800,"manzana", "cascada", "tormenta", "pelicano", "elefante", "martillo", "albahaca", "monedero", "borrador", "perdices"],  # 8 letras
            [1000,"salamandra", "teatrista", "alpestada", "balconada", "largartija", "exhibicion", "mundiales", "revolveres", "poblacion", "numeracion"],  # 9 letras
            [2000,"espectador", "provisional", "preparados", "constructo", "montañismo", "silabacion", "desempeñar", "resolucion", "camuflaje", "justificada"]  # 10 letras
        ]

        self.txtPuntos = self.canvas.create_text(20, 450, text=f"Puntos: {self.puntos}", font=("Arial", 17), anchor="w", fill="white")
        self.txtKills = self.canvas.create_text(20, 425, text=f"Bajas: {self.puntos}", font=("Arial", 17), anchor="w", fill="white")

        self.btnSalir = Button(self.frJuego, text="Salir", command=self.root.salir_juego)
        self.btnReiniciar = Button(self.frJuego, text="Reniciar", command=self.root.reiniciar_juego)

        self.nave = Nave(self, 300, 450)
        self.selAsteroide = None
        self.objetos = [
            self.nave,
        ] 

        self.ventana.bind("<KeyPress>", self.presionarTecla)

        self.hilos: list[th.Thread] = []
        self.hilos.append(th.Thread(target=self.dibujarObjetos))
        self.hilos.append(th.Thread(target=self.procesarObjetos))

    def iniciar(self):
        if self.ejecutar:
            for hilo in self.hilos:
                hilo.start()

    def dibujarObjetos(self):
        while self.ejecutar:
            self.canvas.itemconfig(self.txtPuntos, text=f"Puntos: {self.puntos}")
            self.canvas.itemconfig(self.txtKills, text=f"Bajas: {self.kills}")
            for objeto in self.objetos:
                objeto.dibujar()
            time.sleep(0.001)

    def procesarObjetos(self):
        delta = 0
        tiempo_inicial = time.perf_counter()
        while self.ejecutar:
            tiempo_actual = time.perf_counter()
            delta = tiempo_actual - tiempo_inicial
            tiempo_inicial = tiempo_actual
            self.procesarCuadro(delta)
            for objeto in self.objetos:
                objeto.procesarCuadro(delta)
            time.sleep(0.001)

    def detener(self):
        self.ejecutar = False
        for hilo in self.hilos:
            while hilo.is_alive():
                hilo.join(timeout=0.1) 
                self.ventana.update()
        self.frJuego.destroy()

    def fin_juego(self):
        self.ejecutar = False
        self.canvas.create_text(300, 100, text="FIN DEL JUEGO", font=("Arial", 25), fill="red")
        self.canvas.create_text(300, 200, text=f"Puntos: {self.puntos}", font=("Arial", 20), fill="white")
        self.btnSalir.place(relx=0.5, rely=0.5, width=50, height=25, anchor="center")
        self.btnReiniciar.place(relx=0.5, rely=0.5, y=30, width=50, height=25, anchor="center")
        self.jugador.guardar_puntaje(self.puntos)

    def presionarTecla(self, event):
        key = event.keysym.lower()
        if not self.selAsteroide:
            self.elegir_asteroide(key)
        else:
            if self.selAsteroide.recibir_disparo(key):
                self.nave.disparar(self.selAsteroide)
        
        for e in self.eventosTecla:
            e(event)

    def set_evento_teclado(self, evento):
        self.eventosTecla.append(evento)
    
    def procesarCuadro(self, delta):

        if self.contadorKills >= 10:
            self.contadorKills = 0
            self.dificultad += 1

        self.tiempo += delta
        maxtime = 5
        if maxtime - (0.5 * self.dificultad) > 1:
            maxtime = maxtime - (0.5 * self.dificultad)
        else:
            maxtime = 1
        
        if self.tiempo >= maxtime:
            self.tiempo = 0
            for _ in range(math.floor(0.3 * self.dificultad) + 3):
                self.spawnear_asteroide()

    def spawnear_asteroide(self):
        randx = random.randint(0, 600)
        randy = random.randint(-30, -20)
        rands = random.randint(20, 30)
        if self.dificultad < len(self.palabras):
            palabras = self.palabras[self.dificultad]
        else:
            palabras = self.palabras[len(self.palabras)-1]

        palabra = palabras[random.randrange(1, len(palabras) - 1)]
        puntos = palabras[0]
        self.objetos.append(Asteroide(self, randx, randy, self.nave, rands, 40 + (0.5 * self.dificultad ), palabra, puntos))       

    def elegir_asteroide(self, letra):
        minA = None
        for asteroide in self.objetos:
            if type(asteroide) == Asteroide:
                if asteroide.palabra.lower().startswith(letra):
                    if not minA:
                        minA = asteroide
                    else:
                        if minA.distancia > asteroide.distancia:
                            minA = asteroide
        if minA:
            self.selAsteroide = minA
            self.selAsteroide.seleccionar(True)
            if self.selAsteroide.recibir_disparo(letra):
                self.nave.disparar(self.selAsteroide)
    
    def add_kill(self, puntos):
        self.kills += 1
        self.contadorKills += 1
        self.puntos+= puntos

    def dibujar_estrellas(self):
        self.canvas.delete("estrellas")
        for _ in range(40):
            x = random.randint(0, 600)
            y = random.randint(0, 500)
            t = 2

            self.canvas.create_oval(x, y, x+t, y+t, fill="#adadad", outline="",tags="estrellas")