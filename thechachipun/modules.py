from .askUser import askAndVerify, validateResponse
from .ui import messages, util
from .core import listarJugadores, agregarEscudos,agregarCpuPuntos,agregarCpuEscudos, agregarPuntuacion, partidasGanadas,partidasPerdidas
import random

"""
en este modulo podras encontrar la logica interna del juego en si donde podras ver los juegos 1v1
o 1 vs ia(facil o dificil) se agregaran los puntos y estadisticas
"""

def oneByOne():# 1 versus 1
    print(messages.primero)
    player1 = None
    while player1 == None:
        player1 = askAndVerify(listarJugadores())#elegir jugador 1
    player2 = None
    while player2 == None :
        print(messages.segundo)
        player2 = askAndVerify(listarJugadores())#elegir jugador 2 y validar que no sea el mismo que el 1
        if player2 == player1:
            input(messages.repetidos)
            player2 = None
            util.clear()
    partida(player1, player2)# imgresar los dos jugadores ingresados a la partida

def oneByCpu():#juego solo contra CPU
    print(messages.primero)
    player1 = None
    while player1 == None:
        player1 = askAndVerify(listarJugadores())#elegir jugador 1
    partida(player1, 'ia')

def oneByCpuDificil():#juego solo contra CPU(Dificil)
    print(messages.primero)
    player1 = None
    while player1 == None:
        player1 = askAndVerify(listarJugadores())#elegir jugador 1
    partida(player1, 'ia_dificil')

def partida(savedData1, savedData2): #iniciar la partida
    puntajePlayer1 = 0
    puntajePlayer2 = 0
    for i in range(3):#validar 3 rondas
        print(messages.ppop1)
        player1 = None
        while player1 == None:
            player1 = askAndVerify(messages.opcionesPpt)#pedir que elijas piedra papel o tijera
            util.clear()
        print(messages.ppop2)

        if savedData2 == 'ia':#validar si se esta jugando contra ia facil o dificil o ninguna
            player2 = partidaCpu()
        elif savedData2 == 'ia_dificil':
            player2 = partidaCpuDificil(player1)
        else:
            player2 = None
            while player2 == None:
                player2 = askAndVerify(messages.opcionesPpt)# si no se juega contra ninguna ia se pide que el jugador 2 elija piedra papel o tijera
                util.clear()

        result = ronda(player1, player2) #juega la ronda con la funcion ronda() donde entregamos la variable player 1 y 2

        if result == "Jugador 1 gana":#le pedimos al programa que valide cual de los dos jugadores gano
            puntajePlayer1 += 1
        elif result == "Jugador 2 gana":
            puntajePlayer2 += 1# y en caso de que gane asignamos una puntuacion por ronda para luego determinar ganador de la partida

        if puntajePlayer1 == 2:#asignamos escudos comparando la puntuacion del jugador
            agregarEscudos(savedData1)
        if puntajePlayer2 == 2:
            if  savedData2 == 'ia' or savedData2 == 'ia_dificil' :
                agregarCpuEscudos(savedData2)
            else:
                agregarEscudos(savedData2)

        print(f'jugador1 : {puntajePlayer1} - jugador2 : {puntajePlayer2}')#imprimimos la puntuacion de los dos jugadores
        input(f"Ronda {i+1}: {result}")#y imprimimos el numero de la ronda mas el resultado de la ronda
        util.clear()
    if  puntajePlayer1 > puntajePlayer2:#definimos el ganador de la partida despues de las 3 rondas
        agregarPuntuacion(savedData1,2)
        if savedData2 == 'ia' or savedData2 == 'ia_dificil' :
            partidasGanadas(savedData1)# y asignamos puntos para la funcion de persistencia de JSON
    elif puntajePlayer2 > puntajePlayer1 and savedData2 == 'ia' or savedData2 == 'ia_dificil':
        agregarCpuPuntos(savedData2, 2)#puede que sea el bot el que gane
        partidasPerdidas(savedData1)# y de esta manera que el usuario pierda
    else:
        agregarPuntuacion(savedData2,2)# o asignamos puntos a los usuarios

def partidaCpu():
    return random.randint(1,3)

def partidaCpuDificil(player1):
    weights = [1, 1, 1]

    match player1:
        case 1: # Piedra
            weights = [0.2, 0.6, 0.2]
        case 2: # Papel
            weights = [0.2, 0.2, 0.6]
        case 3: # Tijera
            weights = [0.6, 0.2, 0.2]

    return random.choices([1, 2, 3], weights)[0]
"""
para la partida contra bot dicil decidi aplicar un sistema de probabilidades
dependiendo de el numero que escoja el usuario dandonde un 60% de probabilidades de ganar a la maquina todo
esto con la libreria random usando el metodo random.choices()
(toda la documentacion con la que me guie se encuentra en el archivo README.md)
"""

def ronda(player1Elec, player2Elec):#toda la logica de cada ronda
    if str(player1Elec) == str(player2Elec):# si son igaules empatan
        return "Empate"
    #si no son iguales compara cada una de las formas que tiene el jugador 1 de ganar
    elif (str(player1Elec) == "1" and str(player2Elec) == "3") or \
        (str(player1Elec) == "2" and str(player2Elec) == "1") or \
        (str(player1Elec) == "3" and str(player2Elec) == "2"):
        return "Jugador 1 gana"
    else:# si el jugador 1 no gana y no quedan empatados el jugador 2 por logica queda como ganador
        return "Jugador 2 gana"
