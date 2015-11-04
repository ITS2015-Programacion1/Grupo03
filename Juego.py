#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine
from pilasengine.habilidades import Habilidad

pilas = pilasengine.iniciar()

class Animacion(Habilidad): 
    def __init__(self, receptor): 
        Habilidad.__init__(self, receptor) 
        pilas.escena_actual().click_de_mouse.conectar(self.change) 

    def change(self, evento): 
        self.receptor.imagen.avanzar()

class JohnCena(pilasengine.actores.Actor):

    def iniciar(self):
        self.grilla = pilas.imagenes.cargar_grilla("prueba.png", 9)
        self.imagen = self.grilla
        self.aprender(pilas.habilidades.MoverseConElTeclado,velocidad_maxima=3)
        
    def actualizar(self):
        if pilas.control.abajo:
            self.imagen.avanzar()
            self.y -= 2
            self.rotacion=180
            self.espejado = True
        
        if pilas.control.arriba:
            self.imagen.avanzar()
            self.rotacion=0
            self.y += 2
            self.espejado = False

        if pilas.control.derecha:
            self.rotacion=90
            self.imagen.avanzar()

        if pilas.control.izquierda:
            self.rotacion=-90
            self.imagen.avanzar()


fondo=pilas.fondos.Pasto()

pilas.habilidades.vincular(Animacion)
pilas.actores.vincular(JohnCena)
actor = pilas.actores.JohnCena()

actor.escala=0.5


#actor.aprender('CambiarImagenConClick')

pilas.ejecutar()
