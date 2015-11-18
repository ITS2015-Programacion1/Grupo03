#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine
from pilasengine.habilidades import Habilidad

pilas = pilasengine.iniciar()

class JohnCena(pilasengine.actores.Actor):

    def iniciar(self):
        self.imagen = pilas.imagenes.cargar_grilla("John_Cena_Completo.png" )
        self.figura = pilas.fisica.Rectangulo(self.x, self.y, 65, 34,
            friccion=0, restitucion=0)
    def actualizar(self):
        self.figura.x=self.x
        self.figura.y=self.y

        if pilas.control.abajo:
            self.imagen.avanzar()
            self.y -= 2
            self.rotacion=180
            self.espejado = True
            self.figura.rotacion=180


        if pilas.control.arriba:
            self.imagen.avanzar()
            self.rotacion=0
            self.y += 2
            self.espejado = False
            self.figura.rotacion=0


        if pilas.control.derecha:
            self.rotacion=-90
            self.imagen.avanzar()
            self.x +=2
            self.figura.rotacion=-90

        if pilas.control.izquierda:
            self.rotacion=90
            self.imagen.avanzar()
            self.x -=2
            self.figura.rotacion=90



        if pilas.control.izquierda and pilas.control.arriba:
            self.rotacion=45
            self.figura.rotacion=45
        if pilas.control.izquierda and pilas.control.abajo:
            self.rotacion=135
            self.figura.rotacion=135
        
        if pilas.control.derecha and pilas.control.arriba:
            self.rotacion=315
            self.figura.rotacion=315
        
        if pilas.control.derecha and pilas.control.abajo:
            self.rotacion=225
            self.figura.rotacion=225
          



pilas.actores.vincular(JohnCena)
actor = pilas.actores.JohnCena()

actor.escala=0.1



#actor.aprender('CambiarImagenConClick')

pilas.ejecutar()
