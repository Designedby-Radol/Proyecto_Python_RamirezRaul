from .askUser import askAndVerify
from .ui import messages,util
from .core import addUser, checkFile, readFile, agregarPuntuacion,eliminarJugador,validEscudos
from .game import menuPrincipal
from .modules import partida, oneByOne, partida, ronda

juego = {
    'jugadores' : {},
    'ia': {}
}
checkFile(juego)
input(messages.inicio)
util.clear()

oneByOne()
# menuPrincipal()
# jugador = 1
# eliminarJugador(jugador)
# score = 2
# agregarPuntuacion(jugador, score)
# addUser()
# deleteJugador(messages.jugadores)
# print("Escogió", askAndVerify(jugadores))
# print("Escogió", askAndVerify(messages.opcionesPpt))
