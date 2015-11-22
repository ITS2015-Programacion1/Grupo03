#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine
from pilasengine.habilidades import Habilidad

pilas = pilasengine.iniciar()
pilas.fisica.gravedad_x=0
pilas.fisica.gravedad_y=0
mapa = pilas.actores.MapaTiled("mapa.tmx")
pilas.fisica.eliminar_techo()
pilas.fisica.eliminar_suelo()
pilas.fisica.eliminar_paredes()

class JohnCena(pilasengine.actores.Actor):

    def iniciar(self):
        self.imagen = pilas.imagenes.cargar_grilla("John_Cena_Completo.png" )

    def actualizar(self):
    	pilas.camara.x=self.x
    	pilas.camara.y=self.y

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
          

fisica_principal = pilas.fisica.Rectangulo(0,0,600,300,dinamica=False)

pilas.actores.vincular(JohnCena)
actor = pilas.actores.JohnCena()
actor.aprender(pilas.habilidades.Imitar,fisica_principal)
actor.escala=0.1



#actor.aprender('CambiarImagenConClick')

pilas.ejecutar()
