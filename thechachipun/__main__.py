from .askUser import askAndVerify
from .ui import messages,util
from .core import addUser, agregarPuntuacion,agregarCpuPuntos,agregarCpuEscudos,checkFile, readFile, eliminarJugador,validEscudos
from .game import menuPrincipal
from .modules import partida, oneByOne, partida, ronda

juego = {
    'jugadores' : {},
    'ia': {
        'puntuacion': 0,
        'escudos' : 0
    }
}
checkFile(juego)
input(messages.inicio)
util.clear()
menuPrincipal()

# agregarCpuPuntos(0)
# agregarCpuEscudos()
# oneByOne()
# jugador = 1
# eliminarJugador(jugador)
# score = 2
# agregarPuntuacion(jugador, score)
# addUser()
# deleteJugador(messages.jugadores)
# print("Escogió", askAndVerify(jugadores))
# print("Escogió", askAndVerify(messages.opcionesPpt))
