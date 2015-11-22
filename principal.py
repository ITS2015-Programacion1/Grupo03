
# -*- encoding: utf-8 -*-
import pilasengine

pilas = pilasengine.iniciar(alto=768, ancho=1366)

fondo = pilas.fondos.Fondo()
fondo.imagen = pilas.imagenes.cargar('menu.jpg')
fondo.definir_escala(3)
sonido=pilas.actores.Sonido()
intro = pilas.musica.cargar("mememe.mp3")
intro.reproducir(repetir=True)
class Menu(pilasengine.actores.Menu):

	def iniciar_juego():
		pilas.escenas.Normal()
		intro.detener()
		pilas.fisica.gravedad_x=0
		pilas.fisica.gravedad_y=0
		pilas.fisica.eliminar_techo()
		pilas.fisica.eliminar_suelo()
		pilas.fisica.eliminar_paredes()
		fondo=pilas.fondos.Pasto()

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

		actor.escala=0.1

	def Ayuda():
		fondo.eliminar()
		fondo3 = pilas.fondos.Fondo()
		fondo3.imagen=pilas.imagenes.cargar('ayuda.jpg')	
		fondo3.definir_escala(2.5)
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