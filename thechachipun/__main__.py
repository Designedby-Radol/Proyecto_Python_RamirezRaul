from .askUser import askAndVerify
from .ui import messages,util
from .core import addUser, checkFile, readFile
from .game import menuPrincipal

juego = {
    'jugadores' : {},
    'ia': {}
}
checkFile(juego)
input(messages.inicio)
util.clear()
menuPrincipal()
# addUser()
# deleteJugador(messages.jugadores)
# print("Escogió", askAndVerify(jugadores))
# print("Escogió", askAndVerify(messages.opcionesPpt))
