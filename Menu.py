#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine
pilas = pilasengine.iniciar()
fondo = pilas.fondos.Fondo()
fondo.imagen = pilas.imagenes.cargar('menu.jpg')
fondo.escala=1.5
sonido=pilas.actores.Sonido()
intro = pilas.musica.cargar("mememe.mp3")
intro.reproducir(repetir=True)



def iniciar_juego():
	menu.eliminar()
	intro.detener()
def salir_del_juego():
	exit()

menu=pilas.actores.Menu(
        [
            ('Iniciar juego', iniciar_juego),
            ('Salir', salir_del_juego),
        ])

pilas.ejecutar()
