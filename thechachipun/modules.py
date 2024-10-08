from .askUser import askAndVerify, validateResponse
from .ui import messages, util
from .core import listarJugadores, agregarEscudos,agregarCpuPuntos,agregarCpuEscudos, agregarPuntuacion
import random
def oneByOne():
    print(messages.primero)
    player1 = None
    while player1 == None:
        player1 = askAndVerify(listarJugadores())
    player2 = None
    while player2 == None :
        print(messages.segundo)
        player2 = askAndVerify(listarJugadores())
        if player2 == player1:
            input(messages.repetidos)
            player2 = None
            util.clear()
    savedData1 = player1
    savedData2 = player2
    partida(savedData1, savedData2)

def oneByCpu():
    print(messages.primero)
    player1 = None
    while player1 == None:
        player1 = askAndVerify(listarJugadores())
    player2 = None
    savedData1 = player1
    savedData2 = 'ia'
    partida(savedData1, savedData2)

def partida(savedData1, savedData2):
    puntajePlayer1 = 0
    puntajePlayer2 = 0
    for i in range(3):
        print(messages.ppop1)
        player1 = None
        while player1 == None:
            player1 = askAndVerify(messages.opcionesPpt)
            util.clear()
        print(messages.ppop2)
        
        if savedData2 == 'ia':
            player2 = random.randint(1,3)
        else:
            player2 = None
            while player2 == None:
                player2 = askAndVerify(messages.opcionesPpt)
                util.clear()
        
        result = ronda(player1, player2)
        if result == "Jugador 1 gana":
            puntajePlayer1 += 1
        elif result == "Jugador 2 gana":
            puntajePlayer2 += 1
        if puntajePlayer1 == 2 :
            agregarEscudos(savedData1)
        if puntajePlayer2 == 2 :
            agregarEscudos(savedData2)
        print(f'jugador1 : {puntajePlayer1} - jugador2 : {puntajePlayer2}')
        input(f"Ronda {i+1}: {result}")
        util.clear()
    if  puntajePlayer1 > puntajePlayer2:
        agregarPuntuacion(savedData1,2)
    elif puntajePlayer2 > puntajePlayer1 and savedData2 == 'ia':
        agregarCpuPuntos(2)
    else:
        agregarPuntuacion(savedData2,2)

def ronda(player1Elec, player2Elec):
    if str(player1Elec) == str(player2Elec):
        return "Empate"
    elif (str(player1Elec) == "1" and str(player2Elec) == "3") or \
        (str(player1Elec) == "2" and str(player2Elec) == "1") or \
        (str(player1Elec) == "3" and str(player2Elec) == "2"):
        return "Jugador 1 gana"
    else:
        return "Jugador 2 gana"
