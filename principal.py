# -*- encoding: utf-8 -*-
import pilasengine

pilas = pilasengine.iniciar(alto=768, ancho=1366)

class Menu(pilasengine.actores.Menu):
    fondo=pilas.fondos.Fondo()
    fondo.imagen=pilas.imagenes.cargar("menu.jpg")
    fondo.definir_escala(3)
    intro=pilas.musica.cargar("mememe.mp3")
    intro.reproducir(repetir=True)
    menu=None
    def iniciar(intro=intro, fondo=fondo):
        pilas.escenas.Normal()
        intro.detener()
        pilas.fisica.gravedad_x=0
        pilas.fisica.gravedad_y=0
        pilas.fisica.eliminar_techo()
        pilas.fisica.eliminar_suelo()
        pilas.fisica.eliminar_paredes()
        fondo= pilas.fondos.Fondo('Fondo.png')
        fondo.escala=2.5
        intro=pilas.musica.cargar("musica.mp3")
        intro.reproducir(repetir=True)
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
        actor.escala=0.2      
        fisica=pilas.fisica.Rectangulo(50.2, -50, 4, 100, dinamica=False)                                        

    def ayuda(fondo=fondo, menu=menu, intro=intro):
        pilas.escenas.Normal()
        fondo2=pilas.fondos.Fondo()
        fondo2.imagen=pilas.imagenes.cargar("ayuda.jpg")
        fondo2.definir_escala(2.5)
        def jugar(intro=intro):
            pilas.escenas.Normal()
            intro.detener()
            pilas.fisica.gravedad_x=0
            pilas.fisica.gravedad_y=0
            pilas.fisica.eliminar_techo()
            pilas.fisica.eliminar_suelo()
            pilas.fisica.eliminar_paredes()
            fondo= pilas.fondos.Fondo('Fondo.png')
            fondo.escala=2.5
            intro=pilas.musica.cargar("musica.mp3")
            intro.reproducir(repetir=True)
        def salir():
            exit()
        menu=pilas.actores.Menu(
            [
                ('Jugar', jugar),
                ('Salir', salir),
            ])
    def salir():
        exit()
    menu=pilas.actores.Menu(
            [
                ('Iniciar juego', iniciar),
                ('Ayuda', ayuda),
                ('Salir', salir),
            ])

pilas.ejecutar()