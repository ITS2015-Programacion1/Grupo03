# -*- encoding: utf-8 -*-
import pilasengine

pilas = pilasengine.iniciar(alto=768, ancho=1366)
class Menu(pilasengine.escenas.Escena):
    def iniciar(self):
        fondo=pilas.fondos.Fondo("menu.jpg")
        fondo.definir_escala(3)
        intro=pilas.musica.cargar("mememe.mp3")
        intro.reproducir(repetir=True)
        self.menu=pilas.actores.Menu(
            [
                ('Iniciar juego', self.Juego),
                ('Ayuda', self.ayuda),
                ('Salir', self.salir),
            ])
    def Juego(self):
        pilas.escenas.Juego()
    def ayuda(self):
        pilas.escenas.Ayuda()
    def salir(self):
        exit()

class Puerta(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen="exit.png"


class Ayuda(pilasengine.escenas.Escena):
    def iniciar(self):
        fondo=pilas.fondos.Fondo("menu.jpg")
        fondo.definir_escala(3)
        self.menu=pilas.actores.Menu(
            [
                ('Iniciar juego', self.jugar),
                ('Salir', self.salir),
            ])
        texto=pilas.actores.Texto("Utiliza las teclas de control", y=350, x =-500)
        texto1=pilas.actores.Texto("No dejes que la fuerza especial te vea", y=300, x =-435)

    def jugar(self):
        pilas.escenas.Juego()
    def salir(self):
        exit()

class Juego(pilasengine.escenas.Escena):
    def iniciar(self):
        pilas.fisica.gravedad_x=0
        pilas.fisica.gravedad_y=0
        pilas.fisica.eliminar_techo()
        pilas.fisica.eliminar_suelo()
        pilas.fisica.eliminar_paredes()
        intro=pilas.musica.cargar("musica.mp3")
        intro.reproducir(repetir=True)
        fondo=pilas.actores.MapaTiled("prueba.tmx")

        fisica_principal = pilas.fisica.Rectangulo(-1180.5,245,600,300,dinamica=True)
        fisica_enemigo = pilas.fisica.Rectangulo(0,670,600,300,dinamica=True)
        fisica_enemigo1 = pilas.fisica.Rectangulo(-1160,460,600,400,dinamica=True)
        fisica_enemigo2 = pilas.fisica.Rectangulo(430,-30,600,400,dinamica=True)
        fisica_enemigo3 = pilas.fisica.Rectangulo(-0.5,-500,600,400,dinamica=True)
        fisica_enemigo4 = pilas.fisica.Rectangulo(900,-130,600,400,dinamica=True)
        fisica_enemigo5 = pilas.fisica.Rectangulo(440,94.3,600,400,dinamica=True)
        fisica_enemigo6 = pilas.fisica.Rectangulo(500,500,600,400,dinamica=True)


        actor = pilas.actores.JohnCena()
        llave = pilas.actores.llave()
        enemigo=pilas.actores.Enemigo()
        enemigo1=pilas.actores.Enemigo1()
        enemigo2=pilas.actores.Enemigo2()
        enemigo3=pilas.actores.Enemigo3()
        enemigo4=pilas.actores.Enemigo4()
        enemigo5=pilas.actores.Enemigo5()
        enemigo6=pilas.actores.Enemigo6()
        puerta=pilas.actores.Puerta()
        puerta1=pilas.actores.Puerta()

        actor.escala=0.2
        llave.escala=0.3
        enemigo.escala=0.2
        enemigo1.escala=0.2
        enemigo2.escala=0.2
        enemigo3.escala=0.2
        enemigo4.escala=0.2
        enemigo5.escala=0.2
        enemigo6.escala=0.2
        puerta.escala=0.2
        puerta1.escala=0.2

        llave.x=-1020
        llave.y=-620
        puerta.x=-145
        puerta.y=-545
        puerta1.x=-2000
        puerta1.y=-700

        llave.radio_de_colision=40
        
        
        actor.aprender(pilas.habilidades.Imitar,fisica_principal)
        enemigo.aprender(pilas.habilidades.Imitar,fisica_enemigo)
        enemigo1.aprender(pilas.habilidades.Imitar,fisica_enemigo1)
        enemigo2.aprender(pilas.habilidades.Imitar,fisica_enemigo2)
        enemigo3.aprender(pilas.habilidades.Imitar,fisica_enemigo3)
        enemigo4.aprender(pilas.habilidades.Imitar,fisica_enemigo4)
        enemigo5.aprender(pilas.habilidades.Imitar,fisica_enemigo5)
        enemigo6.aprender(pilas.habilidades.Imitar,fisica_enemigo6)

        enemigos=[enemigo, enemigo1, enemigo2, enemigo3, enemigo4, enemigo5, enemigo6]

        
        def coger_llave(actor, llave, puerta1=puerta1):
            llave.eliminar()
            pilas.avisar("Nuevo objeto encontrado: Llave")
            puerta1.y=-545
        def abrir_puerta(actor, puerta):
            puerta.eliminar()
            pilas.avisar("Necesitas la llave para escapar")

        def abrir_puerta1(actor, puerta, fondo=fondo, intro=intro):
            fondo.eliminar()
            intro.detener()
            actor.eliminar()
            pilas.camara.x=3000
            pilas.camara.y=0
            fondo=pilas.fondos.Fondo()
            fondo.imagen=pilas.imagenes.cargar("fondo2.jpg")
            fondo.definir_escala(1.2)
            fondo.x=3000     
            texto=pilas.actores.Texto("Felicitaciones", y=200)
            texto.escala=[5]
            texto1=pilas.actores.Texto("Has ganado", y=100)
            texto1.escala=[2]
            intro=pilas.musica.cargar("mememe.mp3")
            intro.reproducir(repetir=True)
            def salir():
                exit()
            menu=pilas.actores.Menu(
            [
                ('Salir',  salir),
            ])

        pilas.colisiones.agregar(actor, llave, coger_llave)
        pilas.colisiones.agregar(actor, puerta, abrir_puerta)
        pilas.colisiones.agregar(actor, puerta1, abrir_puerta1)


        def perder(enemigos, actor, intro=intro, llave=llave, fondo=fondo):
            actor.eliminar()
            llave.eliminar()
            fondo.eliminar()
            intro.detener()
            enemigos.eliminar()
            pilas.camara.x=3000
            pilas.camara.y=0
            fondo=pilas.fondos.Fondo()
            fondo.imagen=pilas.imagenes.cargar("menu.jpg")
            fondo.definir_escala(1.2)
            fondo.x=3000     
            texto=pilas.actores.Texto("Game Over", y=100)
            texto.escala=[2]
            intro=pilas.musica.cargar("mememe.mp3")
            intro.reproducir(repetir=True)
            def salir():
                exit()
            def volver():
                pilas.escenas.Juego()
            menu=pilas.actores.Menu(
            [
                ('Reintentar', volver),
                ('Salir',  salir),
            ])


        pilas.colisiones.agregar(actor, enemigos, perder)

class JohnCena(pilasengine.actores.Actor):

    def iniciar(self):
        self.imagen = "Personaje.png"

    def actualizar(self):

        pilas.camara.x=self.x
        pilas.camara.y=self.y

        if pilas.control.abajo:
            self.imagen.avanzar()
            self.y -= 4
            self.rotacion=180
            self.espejado = True


        if pilas.control.arriba:
            self.imagen.avanzar()
            self.rotacion=0
            self.y += 4
            self.espejado = False


        if pilas.control.derecha:
            self.rotacion=-90
            self.imagen.avanzar()
            self.x +=4

        if pilas.control.izquierda:
            self.rotacion=90
            self.imagen.avanzar()
            self.x -=4


        if pilas.control.izquierda and pilas.control.arriba:
            self.rotacion=45

        if pilas.control.izquierda and pilas.control.abajo:
            self.rotacion=135

        if pilas.control.derecha and pilas.control.arriba:
            self.rotacion=315

        if pilas.control.derecha and pilas.control.abajo:
            self.rotacion=225

class Enemigo(pilasengine.actores.Actor):
    def iniciar(self):
        self.rotacion=-90
        self.imagen ="Enemigo.png"
        self.direccion=1
        

    def actualizar(self):
        if self.x >= -50:
            self.direccion=-1
            self.rotacion=90
        if self.x <= -1160:
            self.direccion=1
            self.rotacion=-90
        self.x+=self.direccion * 5

class Enemigo1(pilasengine.actores.Actor):
    def iniciar(self):

        self.rotacion=90
        self.imagen ="Enemigo.png"
        self.direccion=1
        

    def actualizar(self):
        if self.x <= -1160:
            self.direccion=1
            self.rotacion=-90
        if self.x >= -50:
            self.direccion=-1
            self.rotacion=90
        self.x+=self.direccion * 5

class Enemigo2(pilasengine.actores.Actor):
    def iniciar(self):
        self.rotacion=-90
        self.imagen ="Enemigo.png"
        self.direccion=-1

    def actualizar(self):
        if self.x >= 400:
            self.direccion=-1
            self.rotacion=90
        if self.x <= -700:
            self.direccion=1
            self.rotacion=-90
        self.x+=self.direccion * 4.7

class Enemigo3(pilasengine.actores.Actor):
    def iniciar(self):
        self.rotacion=-180
        self.imagen ="Enemigo.png"
        self.direccion=-1
        

    def actualizar(self):
        if self.y >= -200:
            self.direccion=-1
            self.rotacion=180
        if self.y <= -500:
            self.direccion=1
            self.rotacion=0
        self.y+=self.direccion * 5

class Enemigo4(pilasengine.actores.Actor):
    def iniciar(self):
        self.rotacion=90
        self.imagen ="Enemigo.png"
        self.direccion=1

    def actualizar(self):
        if self.x >= 900:
            self.direccion=-1
            self.rotacion=90
        if self.x <= 600:
            self.direccion=1
            self.rotacion=-90
        self.x+=self.direccion * 4.5

class Enemigo5(pilasengine.actores.Actor):
    def iniciar(self):
        self.rotacion=-90
        self.imagen ="Enemigo.png"
        self.direccion=1

    def actualizar(self):
        if self.x >= 420:
            self.direccion=-1
            self.rotacion=90
        if self.x <= 125:
            self.direccion=1
            self.rotacion=-90
        self.x+=self.direccion * 4.5

class Enemigo6(pilasengine.actores.Actor):
    def iniciar(self):
        self.rotacion=0
        self.imagen ="Enemigo.png"
        self.direccion=1
        

    def actualizar(self):
        if self.y >= 500:
            self.direccion=-1
            self.rotacion=180
        if self.y <= 270:
            self.direccion=1
            self.rotacion=0
        self.y+=self.direccion * 4
class llave(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen = "Llave.png"

pilas.actores.vincular(JohnCena)
pilas.actores.vincular(llave)
pilas.actores.vincular(Puerta)
pilas.actores.vincular(Enemigo)        
pilas.actores.vincular(Enemigo1)
pilas.actores.vincular(Enemigo2)
pilas.actores.vincular(Enemigo3)
pilas.actores.vincular(Enemigo4)
pilas.actores.vincular(Enemigo5)
pilas.actores.vincular(Enemigo6)   


pilas.escenas.vincular(Juego)
pilas.escenas.vincular(Menu)
pilas.escenas.vincular(Ayuda)
pilas.escenas.Menu()
pilas.ejecutar()