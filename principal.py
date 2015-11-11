#! /usr/bin/env python
# -*- encoding: utf-8 -*-
import pilasengine
import enemigo
import personaje

pilas = pilasengine.iniciar()

fondo=pilas.fondos.Fondo()
fondo.imangen=pilas.imagenes.cargar("escenario")

pilas.ejecutar()