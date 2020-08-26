# -*- coding: utf-8 -*-

from graphics_isn import * #permet au programme de "comprendre" les fonctions et variables definit dans graphics_isn
import webbrowser #permet au programme de "comprendre" comme ouvrir une page internet

""" On définit la taille du graphic et les points utilisés pour faire les grilles """

WEIGHT=1350     #correspond à la largeur de la fenêtre
HEIGHT=855      #correspond à la hauteur de la fenêtre

""" On définit des variables qui seront utilisés par la suite """

running_main = 1        #permet de contrôler la partie "main" qui englobe tous le jeu
running_option = 0      #permet de contrôler la partie option qui permet d'ouvrir une page web avec les règles
running_jeu = 0         #permet de contrôler la partie liée au jeu lorsque l'on appuie sur start
CT1=1  #CT1 et CT2 représentent les compteurs de cases comportant des bateaux non toucher par l'adversaire (5+4+3+3+2=17)
CT2=17

""" On définit les listes en global pour pouvoir les modifier dans toutes les fonctions"""

B_J1=[]   #liste utiliser pour la fonction bateau2 concentrant chacunes des données nécessaires pour la construction des bateau (taille + point de base)
B_J2=[]   #liste utiliser pour la fonction bateau2 concentrant chacunes des données nécessaires pour la construction des bateau (taille + point de base)
CS_1=[]   #list des coords de cases contenant un bateau
CS_2=[]   #list des coords de cases contenant un bateau
TT1=[]      #liste des coords des cases "tir toucher"
TR1=[]      #liste des coords des cases "tir raté"
TT2=[]      #liste des coords des cases "tir toucher"
TR2=[]      #liste des coords des cases "tir raté"
T_IMP1=[]   #liste des coords des cases déjà tirer
T_IMP2=[]   #liste des coords des cases déjà tirer

def grille():

    H1=Point(466,0)         #Tous ces points sont créer de façon à dessinner la grille du haut et celle du bah à
    B1=Point(466,418)       #partir de 4 points : le "haut" ; le "bas" ; la "gauche" ; et la "droite"
    G1=Point(466,0)
    D1=Point(884,0)

    H2=Point(466,437)
    B2=Point(466,855)
    G2=Point(466,437)
    D2=Point(884,437)

    for i in range (12):            #On les décales chacuns 12 fois pour créer notre grille 11x11
        draw_line(H1,B1,white)
        H1.x=H1.x+38
        B1.x=B1.x+38

        draw_line(G1,D1,white)
        G1.y=G1.y+38
        D1.y=D1.y+38

        draw_line(H2,B2,white)
        H2.x=H2.x+38
        B2.x=B2.x+38

        draw_line(G2,D2,white)
        G2.y=G2.y+38
        D2.y=D2.y+38

    aff_pol("A",30,Point(513,1),white)    #lettres du haut
    aff_pol("B",30,Point(551,1),white)
    aff_pol("C",30,Point(589,1),white)
    aff_pol("D",30,Point(627,1),white)
    aff_pol("E",30,Point(665,1),white)
    aff_pol("F",30,Point(703,1),white)
    aff_pol("G",30,Point(741,1),white)
    aff_pol("H",30,Point(779,1),white)
    aff_pol("I",30,Point(817,1),white)
    aff_pol("J",30,Point(855,1),white)

    aff_pol("A",30,Point(513,438),white)    #lettres du bas
    aff_pol("B",30,Point(551,438),white)
    aff_pol("C",30,Point(589,438),white)
    aff_pol("D",30,Point(627,438),white)
    aff_pol("E",30,Point(665,438),white)
    aff_pol("F",30,Point(703,438),white)
    aff_pol("G",30,Point(741,438),white)
    aff_pol("H",30,Point(779,438),white)
    aff_pol("I",30,Point(817,438),white)
    aff_pol("J",30,Point(855,438),white)


    aff_pol("1",30,Point(475,39),white)     #chiffres du haut
    aff_pol("2",30,Point(475,77),white)
    aff_pol("3",30,Point(475,115),white)
    aff_pol("4",30,Point(475,153),white)
    aff_pol("5",30,Point(475,191),white)
    aff_pol("6",30,Point(475,229),white)
    aff_pol("7",30,Point(475,267),white)
    aff_pol("8",30,Point(475,305),white)
    aff_pol("9",30,Point(475,343),white)
    aff_pol("10",30,Point(465,381),white)

    aff_pol("1",30,Point(475,476),white)    #chiffres du bas
    aff_pol("2",30,Point(475,514),white)
    aff_pol("3",30,Point(475,552),white)
    aff_pol("4",30,Point(475,590),white)
    aff_pol("5",30,Point(475,628),white)
    aff_pol("6",30,Point(475,666),white)
    aff_pol("7",30,Point(475,704),white)
    aff_pol("8",30,Point(475,742),white)
    aff_pol("9",30,Point(475,780),white)
    aff_pol("10",30,Point(465,818),white)


def bateau1(taille,X,Y): #calcul et crée les bateau taille menu via la taille et les coordonnées souhaiter

    P1=Point(X,Y)                           #les bateaux sont créé à partir de 6 points, celui de base de coordonnées (X,Y)
    P2=Point(X+(taille-1)*2*29,Y)           #et les 5 autres qui sont des modifications de celui de base afin de les relier en forme de bateau
    P3=Point(X+(taille-1)*2*29+29,Y+23)
    P4=Point(X+(taille-1)*2*29,Y+46)
    P5=Point(X,Y+46)
    P6=Point(X-29,Y+23)

    draw_line(P1,P2,white)
    draw_line(P2,P3,white)
    draw_line(P3,P4,white)
    draw_line(P4,P5,white)
    draw_line(P5,P6,white)
    draw_line(P6,P1,white)

def fond1(): #Crée la grille et les bateaux de fond
    draw_fill_rectangle(Point(675,427),1500,1000,black)     #suppression des éléments présent via un rectangle noir qui prend toutes la page
    draw_rectangle(Point(117,68),150,50,white)              #création du rectangle blanc contenant le mot START
    aff_pol("START",30,Point(62,48),white)

    draw_rectangle(Point(117,168),150,50,gray)              #création du rectangle gris contenant le mot OPTIONS
    aff_pol("OPTIONS",30,Point(47,148),gray)

    grille()                          #affichage de la grille et des bateaux de fond aux coordonnées prédéfini
    bateau1(2,203,417)
    bateau1(3,174,509)
    bateau1(3,174,601)
    bateau1(4,145,693)
    bateau1(5,116,785)

def fond2(): #Agit de la même manière que la fonction "fond1" cependant on enlève le bouton "START" et le bouton "OPTIONS" car la partie a commencé
    draw_fill_rectangle(Point(675,427),1500,1000,black)    #suppression des éléments présent via un rectangle noir qui prend toutes la page
    grille()
    bateau1(2,203,417)
    bateau1(3,174,509)
    bateau1(3,174,601)
    bateau1(4,145,693)
    bateau1(5,116,785)

def bateau2(taille,X,Y): #Agit de même que la fonction bateau1, cependant celle-ci calcul et crée les bateaux "taille grille"

    P1=Point(X-10,Y)
    P2=Point(X-5,Y-10)
    P3=Point(X+(taille-1)*38+5,Y-10)
    P4=Point(X+(taille-1)*38+10,Y)
    P5=Point(X+(taille-1)*38+5,Y+10)
    P6=Point(X-5,Y+10)

    draw_line(P1,P2,white)
    draw_line(P2,P3,white)
    draw_line(P3,P4,white)
    draw_line(P4,P5,white)
    draw_line(P5,P6,white)
    draw_line(P6,P1,white)

def placement_J1():     #placement = fonction qui vérifie les coordonnés et place les bateau
    global B_J1, CS_1       #On importe les variables dont nous avons besoin dans la fonction
    L=(2,3,3,4,5,0)     # la valeur 0 permet d'annuler l'erreur "list out of range" pour la ligne 180 :    "for k in range (1,L[i+1]):"
    C_IMP1=[]           #liste utiliser pour le placement des bateau qui concentre chaque cases impossible au placement d'un bateau
    draw_rectangle(Point(1117,728),150,50,green)    #création de la case contenant "TOUR J1"
    aff_pol("TOUR J1",30,Point(1042,708),green)
    for i in range (5):     #On fait une boucle répéter 5 fois (Car on placent 5 bateaux)
        PPB=Point(0,0)      #On réaffecte PPB aux coordonnées (0,0) afin qu'elle ne correspondent pas aux critères attendues et redemande le point à l'utilisateur
        while PPB.x <= 504 or PPB.x >= 884-((L[i]-1)*38) or PPB.y <= 476 or PPB.y >= 855 or (PPB.x,PPB.y) in C_IMP1 or (PPB.x+(38*(L[i]-1)),PPB.y) in CS_1 :
        #On vérifie nos conditions (Grille 10x10 / Pas de bateau ou d'interdictions sur ces cases / Pas de bateau sur la derniere case de notre bateau placer)
            PPB=B_placement()       #On envoi PPB dans B_placement afin d'être transformer
        bateau2(L[i],PPB.x,PPB.y)   #On crée le bateau de taille L[i] et de coordonnées (PPB.x,PPB.y)
        B_J1+=L[i],PPB.x,PPB.y      #On ajoute à B_J1 les caractéristique du bateau placer pour qu'elle soient sauvergarder et réutiliser par la suite
        SUP_C=Point(PPB.x,PPB.y)    #On utilise SUP_C qui prend les coordonnées de PPB pour qu'il puisse être utiliser (PPB étant sauvegarder en mémoire, il est modifié "constamment"
        for j in range (L[i]):      #On répète une boucle autant de fois que la taille du bateau
            SUP_C.x=PPB.x+(j*38)            #On ajoute à SUP_C.x "j*38" qui correspond aux cases exactes ou se trouvent le bateaux
            C_IMP1+=[(SUP_C.x,SUP_C.y)]     #On les ajoutent donc dans la liste de cases "impossibles"
            CS_1+=[(SUP_C.x,SUP_C.y)]       #et dans la liste de cases contenant un morceau de bateau
        for k in range (1,L[i+1]):  #On répète une boucle en partant de 1 jusqu'à la taille de notre bateau suivant
            SUP_C.x=PPB.x-(k*38)            #On soustrait a SUP_C.x "k*38" qui bloque alors les cases à gauches du bateau
            C_IMP1+=[(SUP_C.x,SUP_C.y)]     #On les ajoutent donc dans la liste de cases "impossibles"

    fin_tour()      #fin_tour() permet à l'utilisateur de voir ce qu'il a fait avant de finir sont tour, jusqu'à ce qu'il appuie sur le bouton "FIN TOUR"
    joueur_suivant2()       #joueur_suivant2() correspond à l'entracte entre le joueur 1 vers le joueur 2 afin que le J2 ne voient pas les pions de J1 et inversement

def placement_J2():         #CETTE FONCTION EST "LA MÊME" QUE "placement_J1()" MAIS CORRESPOND AU J2
    global B_J2, CS_2
    L=(2,3,3,4,5,0)
    C_IMP2=[]
    draw_rectangle(Point(1117,728),150,50,green)
    aff_pol("TOUR J2",30,Point(1042,708),green)
    for i in range (5):
        PPB=Point(0,0)
        while PPB.x <= 504 or PPB.x >= 884-((L[i]-1)*38) or PPB.y <= 476 or PPB.y >= 855 or (PPB.x,PPB.y) in C_IMP2 or (PPB.x+(38*(L[i]-1)),PPB.y) in CS_2 :
            PPB=B_placement()
        bateau2(L[i],PPB.x,PPB.y)
        B_J2+=L[i],PPB.x,PPB.y
        SUP_C=Point(PPB.x,PPB.y)

        for j in range (L[i]):
            SUP_C.x=PPB.x+(j*38)
            C_IMP2+=[(SUP_C.x,SUP_C.y)]
            CS_2+=[(SUP_C.x,SUP_C.y)]
        for k in range (1,L[i+1]):
            SUP_C.x=PPB.x-(k*38)
            C_IMP2+=[(SUP_C.x,SUP_C.y)]

    fin_tour()
    joueur_suivant1()

def B_placement(): #bateau placement = fonction qui calcul les coordonnées du bateau afin qu'elles soit situer "au centre" des cases de la grille
    PPB=wait_clic()         #On attend le click de l'utilisateur
    PPB.x=(884-((int((884-PPB.x)/38))+1)*38)+19     #On modifie via un calcul les coords obtenues pour qu'elle soit situer "au centre" des cases de la grille
    PPB.y=(855-((int((855-PPB.y)/38))+1)*38)+19
    return(PPB)     #On renvoit le point obtenu

def joueur_suivant1():  #phase d'attente du joueur 1 après le tour du joueur 2
    global B_J1     #On importe les variables dont nous avons besoin dans la fonction
    draw_fill_rectangle(Point(675,427),1500,1000,black)             #suppression des éléments présent via un rectangle noir qui prend toutes la page
    aff_pol("Attente du joueur 1",35,Point(480,300),white)          #Affichage des messages d'attente
    aff_pol("Clickez pour continuer",35,Point(480,360),white)
    wait_clic()             #Attente du click du joueur 1 pour afficher le contenu de son camps
    draw_fill_rectangle(Point(675,427),1500,1000,black)         #suppression des éléments présent via un rectangle noir qui prend toutes la page
    fond2()        #réaffichage du fond (sans les boutons du menu)
    if len(B_J1)>0:  #si B_J1[0] contient un terme, les bateaux du joueur 2 ont étais construit et peuvent être placer à nouveau
        T=len(B_J1)-1   #T représente la taille de notre liste (L[T] termes)
        for i in range(0,T,3):    #Pour i allant de 0 jusqu'à T de 3 en 3
            bateau2(B_J1[i],B_J1[i+1],B_J1[i+2])    #On reconstruit les bateaux (comme enregistrer dans B_J1 : Taille/Abscisse/Ordonné)

def joueur_suivant2():  #CETTE FONCTION EST "LA MÊME" QUE "joueur_suivant1()" MAIS CORRESPOND AU J2
    global B_J2
    draw_fill_rectangle(Point(675,427),1500,1000,black)
    aff_pol("Attente du joueur 2",35,Point(480,300),white)
    aff_pol("Clickez pour continuer",35,Point(480,360),white)
    wait_clic()
    fond2()
    if len(B_J2)>0:
        T=len(B_J2)-1
        for i in range(0,T,3):
            bateau2(B_J2[i],B_J2[i+1],B_J2[i+2])

def Tir_J1():       #Fonction permettant au joueur 1 de choisir une case ou tirer et vérifier s'il y a un bateau ennemi ou non
    global B_J2,TT1,TR1,CT1,T_IMP1      #On importe les variables dont nous avons besoin dans la fonction
    PPT=Point(0,0)          #On réaffecte PPT aux coordonnées (0,0) afin qu'elle ne correspondent pas aux critères attendues et redemande le point à l'utilisateur
    Aff_Tir_J1()        #On affiche les anciens tirs du joueur pour pas qu'il ne commette d'erreurs en tirant au même endroit
    draw_rectangle(Point(1117,728),150,50,green)    #création de la case contenant "TOUR J1"
    aff_pol("TOUR J1",30,Point(1042,708),green)
    while PPT.x <= 504 or PPT.x >= 884 or PPT.y <= 38 or PPT.y >= 418 or (PPT.x,PPT.y) in T_IMP1 :  #On vérifie nos conditions (Grille 10x10 / Pas de tirs sur cette cases
        PPT=T_placement()       #On envoi PPT dans T_placement afin d'être transformer
    SUP_T=Point(PPT.x,PPT.y)   #On utilise SUP_T qui prend les coordonnées de PPT pour qu'il puisse être utiliser (PPT étant sauvegarder en mémoire, il est modifié "constamment"
    if (PPT.x,PPT.y+437) in CS_2:       #On regarde si les coordonnées appartiennent à un bateau de la liste CS_2 qui correspond aux bateau du joueur 2
        draw_fill_circle(PPT,19,red)    #Si c'est le cas, on trace un rond rouge et on ajoute les coords du point dans la liste des tirs toucher par le joueur 1
        TT1+=SUP_T.x,SUP_T.y
        CT1=CT1-1               #et on enlève 1 à la variable CT1 qui correspond aux nombres de cases contenant un bateau non touché restantes
        aff_pol("Touché",30,Point(900,50),red)      #On affiche alors le message "TOUCHER" à l'utilisateur
    else:
        draw_fill_circle(PPT,19,white)      #Sinon on fait de même, pour les cases "RATE"
        TR1+=SUP_T.x,SUP_T.y
        aff_pol("Raté",30,Point(900,50),white)

    fin_tour()      #fin_tour() permet à l'utilisateur de voir ce qu'il a fait avant de finir sont tour, jusqu'à ce qu'il appuie sur le bouton "FIN TOUR"
    T_IMP1+=[(SUP_T.x,SUP_T.y)]     #On ajout enfin les coords du point dans la liste d'impossibilités pour pas qu'elle ne soient réutiliser par la suite par le joueur

def Aff_Tir_J1():       #Fonction qui permet au programme d'afficher les tirs précedemment envoyer par le joueur 1 et sauvegarder
    global TT1,TR1      #On importe les variables dont nous avons besoin dans la fonction
    CT=len(TT1)-1       #On utilise les listes précedemment créer ainsi que deux variables correspondants au nombres de tirs toucher et tirs raté
    CR=len(TR1)-1
    for i in range(0,CT,2):     #afin de recréer ces tirs
        A=TT1[i]
        B=TT1[i+1]
        draw_fill_circle(Point(A,B),19,red)
    for i in range(0,CR,2):
        C=TR1[i]
        D=TR1[i+1]
        draw_fill_circle(Point(C,D),19,white)

def Tir_J2():       #CETTE FONCTION EST "LA MÊME" QUE "Tir_J1" MAIS CORRESPOND AU J2
    global B_J1,TT2,TR2,CT2,T_IMP2
    PPT=Point(0,0)
    Aff_Tir_J2()
    draw_rectangle(Point(1117,728),150,50,green)
    aff_pol("TOUR J2",30,Point(1042,708),green)
    while PPT.x <= 504 or PPT.x >= 884 or PPT.y <= 38 or PPT.y >= 418 or (PPT.x,PPT.y) in T_IMP2 :
        PPT=T_placement()
    SUP_T=Point(PPT.x,PPT.y)    #On utilise pas le point d'origine (PPT) car il est enregistrer en mémoire et il changera au cours du temps
    if (PPT.x,PPT.y+437) in CS_1:
        draw_fill_circle(PPT,19,red)
        TT2+=SUP_T.x,SUP_T.y
        CT2=CT2-1
        aff_pol("Touché",30,Point(900,50),red)
    else:
        draw_fill_circle(PPT,19,white)
        TR2+=SUP_T.x,SUP_T.y
        aff_pol("Raté",30,Point(900,50),white)
    fin_tour()
    T_IMP2+=[(SUP_T.x,SUP_T.y)]

def Aff_Tir_J2():        #CETTE FONCTION EST "LA MÊME" QUE "Aff_Tir_J1" MAIS CORRESPOND AU J2
    global TT2,TR2
    CT=len(TT2)-1
    CR=len(TR2)-1
    for i in range(0,CT,2):
        draw_fill_circle((Point(TT2[i],TT2[i+1])),19,red)
    for i in range(0,CR,2):
        draw_fill_circle((Point(TR2[i],TR2[i+1])),19,white)

def T_placement(): #Tir placement = fonction qui calcul les coordonnées du tir ; agit de la même façon que B_Placement mais sur la grille du haut
    PPT=wait_clic()
    PPT.x=(884-((int((884-PPT.x)/38))+1)*38)+19
    PPT.y=(418-((int((418-PPT.y)/38))+1)*38)+19
    return(PPT)

def fin_tour():         #fin_tour() permet à l'utilisateur de voir ce qu'il a fait avant de finir sont tour, jusqu'à ce qu'il appuie sur le bouton "FIN TOUR"
    Next=Point(0,0)
    draw_rectangle(Point(1117,428),150,50,blue)
    aff_pol("FIN TOUR",30,Point(1042,408),blue)
    while Next.x <= 1042 or Next.x >= 1192 or Next.y <= 403 or Next.y >= 453 :      #On attend que le point Next soit aux coordonnées de la case afin de finir le tour du joueur
        Next=wait_clic()

def gagner():       #Fonction qui vérifie s'il y a un gagnant
    if CT1==0:      #Si le compteur du joueur 1 atteint 0 alors, celà signifie que le joueur 2 c'est fait toucher tous ces bateaux et le joueur 1 gagne
        draw_fill_rectangle(Point(675,427),1500,1000,black)
        aff_pol("LE JOUEUR 1 L'EMPORTE",50,Point(375,127),yellow)
        wait_escape()
        running_jeu = 0

    elif CT2==0:
        draw_fill_rectangle(Point(675,427),1500,1000,black)
        aff_pol("LE JOUEUR 2 L'EMPORTE",50,Point(375,127),yellow)
        wait_escape()
        running_jeu = 0

def debut():        #Fonction qui permet d'afficher le message de commencement de la partie et qui la démarre après un clique
    draw_fill_rectangle(Point(675,427),1500,1000,black)
    aff_pol("Clickez pour commencer la partie",35,Point(380,300),white)
    wait_clic()
    fond2()      #réaffichage du fond
