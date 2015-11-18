#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine
pilas = pilasengine.iniciar()
fondo = pilas.fondos.Fondo()
fondo.imagen = pilas.imagenes.cargar('menu.jpg')
fondo.escala=1.2
sonido=pilas.actores.Sonido()
intro = pilas.musica.cargar("mememe.mp3")
intro.reproducir(repetir=True)



def iniciar_juego():
	menu.eliminar()
	intro.detener()
	fondo.eliminar()
def Ayuda():
	fondo.eliminar()
	fondo3 = pilas.fondos.Fondo()
	fondo3.imagen=pilas.imagenes.cargar('ayuda.jpg')	
	fondo3.escala=1.2
	menu.eliminar()
	fondo.eliminar()
	def Volver_al_menu():
		menu2.eliminar()
		fondo3.eliminar()
	menu2=pilas.actores.Menu(
        [
            ('Volver', Volver_al_menu),
        ])

def salir_del_juego():
	exit()

menu=pilas.actores.Menu(
        [
            ('Iniciar juego', iniciar_juego),
            ('Ayuda', Ayuda),
            ('Salir', salir_del_juego),
        ])

pilas.ejecutar()
