# -*- encoding: utf-8 -*-
import pilasengine

pilas = pilasengine.iniciar()

class Enemigo(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen ="Enemigo.png"
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
         
pilas.actores.vincular(Enemigo)
actor = pilas.actores.Enemigo()

actor.escala=.25
pilas.ejecutar()