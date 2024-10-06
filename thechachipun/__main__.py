from .askUser import askAndVerify
from .ui import messages
from .core import addUser, checkFile, ReadFile,jugadores
from .game import menuPrincipal

juego = {
    'jugadores' : {},
    'ia': {}
}
checkFile(juego)


menuPrincipal()


# print("Escogió", askAndVerify(jugadores))
# print("Escogió", askAndVerify(messages.opcionesPpt))

