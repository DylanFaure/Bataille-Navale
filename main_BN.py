# -*- coding: utf-8 -*-

from fonctions_BN import *

A=Point(789,532)
def main():
    global running_main, running_jeu, running_option
    init_graphic(WEIGHT,HEIGHT,name="Bataille Navale",bg_color=black,fullscreen=0)
    fond1()

    while running_main == 1 :
        RP=Point(0,0)
        while (RP.x < 42 or RP.x > 192 or RP.y < 43 or RP.y > 93) and (RP.x < 42 or RP.x > 192 or RP.y < 143 or RP.y > 193) :
            RP=wait_clic()
        if RP.x >= 42 and RP.x <= 192 and RP.y >= 43 and RP.y <= 93:
            running_jeu = 1
        elif RP.x >= 42 or RP.x <= 192 or RP.y >= 143 or RP.y <= 193:
            running_option = 1

        while running_option == 1 :
            webbrowser.open('https://www.regles-de-jeux.com/regle-de-la-bataille-navale/')
            running_option = 0

        while running_jeu == 1 :

            debut()
            placement_J1()
            placement_J2()

            while CT1>0 and CT2>0 :
                Tir_J1()
                gagner()
                if CT1>0:
                    joueur_suivant2()
                Tir_J2()
                gagner()
                if CT2>0:
                    joueur_suivant1()


main()




