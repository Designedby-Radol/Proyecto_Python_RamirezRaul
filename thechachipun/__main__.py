from .askUser import askAndVerify
from .ui import messages
from .core import addUser, checkFile, ReadFile

juego = {
    'jugadores' : {},
    'ia': {}
}
addUser()
checkFile(juego)
# print("Escogió", askAndVerify(messages.opcionesPpt))
# print("Escogió", askAndVerify(messages.opcionesJugadores))
