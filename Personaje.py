#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine
from pilasengine.habilidades import Habilidad

pilas = pilasengine.iniciar()

class JohnCena(pilasengine.actores.Actor):

    def iniciar(self):
        self.grilla = pilas.imagenes.cargar_grilla("John_Cena_Completo.png")
        self.imagen = self.grilla
       
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
            self.rotacion=-90
            self.imagen.avanzar()
            self.x +=2

        if pilas.control.izquierda:
            self.rotacion=90
            self.imagen.avanzar()
            self.x -=2

        if pilas.control.izquierda and pilas.control.arriba:
        	self.rotacion=45

       	if pilas.control.izquierda and pilas.control.abajo:
       		self.rotacion=135
       	
       	if pilas.control.derecha and pilas.control.arriba:
       		self.rotacion=315
       	
       	if pilas.control.derecha and pilas.control.abajo:
       		self.rotacion=225

fondo=pilas.fondos.Pasto()
pilas.actores.vincular(JohnCena)
actor = pilas.actores.JohnCena()

actor.escala=.15



#actor.aprender('CambiarImagenConClick')

pilas.ejecutar()
