from tkinter import *
import tkinter as tk
import random
from vista.Asteroide import Asteroide
from vista.Nave import Nave
import time
import threading as th

class Juego():
    def __init__(self, root, jugador):
        self.root = root
        self.jugador = jugador
        
        self.ejecutar = True
        self.fotograma = 0.016
        self.eventosTecla = []

        self.root.bind("<KeyPress>", self.presionarTecla)
        
        self.canvas = Canvas(self.root, bg="black")
        self.canvas.place(x=0, y=0, relheight=1, relwidth=1) #ventana es 600x500

        self.dibujar_estrellas()

        self.objetos = [
            Asteroide(self, 300, 250),
            Nave(self, 300, 450)
        ] 

        

        self.hilos: list[th.Thread] = []
        self.hilos.append(th.Thread(target=self.dibujarObjetos))
        self.hilos.append(th.Thread(target=self.procesarObjetos))

    def iniciar(self):
        if self.ejecutar:
            for hilo in self.hilos:
                hilo.start()

    def dibujarObjetos(self):
        while self.ejecutar:
            tiempo_inicial = time.perf_counter()
            for objeto in self.objetos:
                objeto.dibujar()
            tiempo_final = time.perf_counter()

    def procesarObjetos(self):
        delta = 0
        tiempo_inicial = time.perf_counter()
        while self.ejecutar:
            tiempo_actual = time.perf_counter()
            delta = tiempo_actual - tiempo_inicial
            tiempo_inicial = tiempo_actual
            for objeto in self.objetos:
                objeto.procesarCuadro(delta)
            time.sleep(0.001)

    def detener(self):
        self.ejecutar = False
        for hilo in self.hilos:
            while hilo.is_alive():
                hilo.join(timeout=0.1) 
                self.root.update()

    def presionarTecla(self, event):
        print(event.keysym)
        for e in self.eventosTecla:
            e(event)

    def set_evento_teclado(self, evento):
        self.eventosTecla.append(evento)

    def dibujar_estrellas(self):
        self.canvas.delete("estrellas")
        for _ in range(40):
            x = random.randint(0, 600)
            y = random.randint(0, 500)
            t = 2

            self.canvas.create_oval(x, y, x+t, y+t, fill="#adadad", outline="",tags="estrellas")