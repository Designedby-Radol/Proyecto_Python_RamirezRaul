from .ui import messages,util
from .core import checkFile,estadisticas
from .game import menuPrincipal
"""
modulo principal de ejecucion del archivo
"""

juego = {
    'jugadores' : {},
    'ia': {
        'puntuacion': 0,
        'escudos' : 0
    },
    'ia_dificil': {
        'puntuacion': 0,
        'escudos' : 0
    }
}
checkFile(juego)
input(messages.inicio)
util.clear()
menuPrincipal()
