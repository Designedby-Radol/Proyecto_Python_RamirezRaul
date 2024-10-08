from .askUser import askAndVerify, validateResponse
from .ui import messages, util
from .core import listarJugadores, agregarEscudos

def oneByOne():
    print(messages.primero)
    player1 = None
    while player1 == None:
        player1 = askAndVerify(listarJugadores())
    print(messages.segundo)
    player2 = None
    while player2 == None and player2 == player1:
        if player2 == player1:
            input(messages.repetidos)
            util.clear()
        player2 = askAndVerify(listarJugadores())
    savedData1 = player1
    savedData2 = player2
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

def ronda(player1Elec, player2Elec):
    if str(player1Elec) == str(player2Elec):
        return "Empate"
    elif (str(player1Elec) == "1" and str(player2Elec) == "3") or \
        (str(player1Elec) == "2" and str(player2Elec) == "1") or \
        (str(player1Elec) == "3" and str(player2Elec) == "2"):
        return "Jugador 1 gana"
    else:
        return "Jugador 2 gana"
