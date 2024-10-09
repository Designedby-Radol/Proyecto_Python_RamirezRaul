from .askUser import askAndVerify,validateResponse
from .ui import messages, util
from .core import validJugadores,addUser,listarJugadores,eliminarJugador,agregarPuntuacion,estadisticas
from .modules import oneByOne,oneByCpu,oneByCpuDificil

"""
este modulo se encarga de anidar los menus por los cuales el usuario podra navegar
para poder tener una mejor jugabilidad
"""

def menuPrincipal(): #el menu principal la parte principal donde el usuario va a navegar para jugar o gestionar la base de datos
    menuElec = None
    while menuElec != 5:
        menuElec = askAndVerify(messages.menuElec)
        util.clear()
        match menuElec:
            case 1:
                unoVersus()
            case 2:
                cpu()
            case 3:
                cpuDificil()
            case 4:
                gestion()
            case 5:
                if validateResponse(messages.salida):
                    util.clear()
                    break
                else:
                    util.clear()
                    menuElec = None

def gestion():# aca se encarga de gestionar los usuarios (crear, mirar, eliminar)
    playerElec = None
    while playerElec != 5:
        playerElec = askAndVerify(messages.playerElec)
        match playerElec:
            case 1:
                jugadores = listarJugadores() # hacer funcion wait para que se muestren jugadores
                print(jugadores['msg'])
                input()
                util.clear()
            case 2:
                addUser()
            case 3:
                eliminado = askAndVerify(listarJugadores())
                if eliminado:
                    eliminarJugador(eliminado)
            case 4:
                estadisticas()
                input()
                util.clear()
            case 5:
                if validateResponse(messages.salida):
                    util.clear()
                else:
                    util.clear()
                    playerElec = None

def unoVersus():#puede jugar contra otro jugador
    playerElec = None
    while playerElec != 2:
        playerElec = askAndVerify(messages.unoElec)
        match playerElec:
            case 1:
                if validJugadores():
                    oneByOne()
                else:
                    print(messages.noHayJugadores)
            case 2:
                if validateResponse(messages.salida):
                    util.clear()
                else:
                    util.clear()
                    playerElec = None

def cpu():#puede jugar contra ia(normal)
    playerElec = None
    while playerElec != 2:
        playerElec = askAndVerify(messages.cpuElec)
        match playerElec:
            case 1:
                if validJugadores():
                    oneByCpu()
                else:
                    print(messages.noHayJugadores)
            case 2:
                if validateResponse(messages.salida):
                    util.clear()
                else:
                    util.clear()
                    playerElec = None

def cpuDificil():#puede jugar contra la ia(dificil)
    playerElec = None
    while playerElec != 2:
        playerElec = askAndVerify(messages.cpuDificilElec)
        match playerElec:
            case 1:
                if validJugadores():
                    oneByCpuDificil()
                else:
                    print(messages.noHayJugadores)
            case 2:
                if validateResponse(messages.salida):
                    util.clear()
                else:
                    util.clear()
                    playerElec = None
