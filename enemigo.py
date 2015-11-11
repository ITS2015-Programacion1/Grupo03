# -*- encoding: utf-8 -*-
import pilasengine

pilas = pilasengine.iniciar()

class enemigo(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen ="John_Cena_Completo.png"
        self.direccion=-1
        self.rotacion=90

    def actualizar(self):
        #Funcion que permite sel movimiento de el enemigo
        if self.x <= -300:
            self.direccion=1
            self.rotacion=-90
        if self.x >= 300:
            self.direccion=-1
            self.rotacion=90
        self.x+=self.direccion * 2.5
         
pilas.actores.vincular(enemigo)
actor = pilas.actores.enemigo()

actor.escala=.25
pilas.ejecutar()