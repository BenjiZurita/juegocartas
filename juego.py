from baralla import Baralla
from ma import Ma

class Juego:
    def __init__(self):
        self.baralla = Baralla()
        self.baralla.barallar()

    def jugar(self):
        majugador = Ma()
        mabot = Ma()

        while majugador.valor < 21:
            
            accio = input("Vols altra carta? (s/n)")
            if accio == "s":
                carta = self.baralla.treure_carta()
                majugador.afegir_carta(carta)
                print("Les teves cartes: ")
                majugador.mostrar_cartes()
                print("Punts: ", majugador.valor)
            elif accio == "n":
                break
            
            if mabot.valor < 17:
                cartabot = self.baralla.treure_carta()
                mabot.afegir_carta(cartabot)
                print("Les cartes del bot: ")
                mabot.mostrar_cartes()
                print("Botpunts: ", mabot.valor)
            elif mabot.valor > 21:
                print("El bot s'ha pasat de 21.")
                break
            else:
                print("El bot s'ha plantat")
            
            self.baralla.barallar()

        if majugador.valor == mabot.valor:
            print("Heu empatat")
        elif 21>majugador.valor > mabot.valor or majugador == 21:
            print("Heu guanyat al bot: ", majugador.valor, "-", mabot.valor)
        elif majugador.valor < mabot.valor < 21 or majugador.valor > 21:
            print("T'ha guanyat el bot", mabot.valor, "-", majugador.valor)