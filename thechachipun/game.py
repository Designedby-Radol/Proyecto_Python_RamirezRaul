from .askUser import askAndVerify,validateResponse
from .ui import messages, util
from .core import validJugadores,addUser,listarJugadores,eliminarJugador,agregarPuntuacion
from .modules import oneByOne,oneByCpu

def menuPrincipal():
    try:
        menuElec = askAndVerify(messages.menuElec)
        util.clear()
        if menuElec == None:
            menuPrincipal()
        match menuElec:
            case 1 :
                unoVersus()
            case 2 :
                cpu()
            case 3 : 
                gestion()
            case 4 :
                if validateResponse(messages.salida):
                    util.clear()
                    pass
                else:
                    util.clear()
                    menuPrincipal()
    except ValueError:
        menuPrincipal()

def gestion():
    try:
        while True :
            playerElec = askAndVerify(messages.playerElec)
            match playerElec:
                case 1 :
                    jugadores = listarJugadores() #hacer funcion wait para que se muestren jugadores
                    print(jugadores)
                    input()
                    util.clear()
                case 2 :
                    addUser()
                    gestion()
                case 3:
                    eliminado = askAndVerify(listarJugadores())
                    if not eliminado:
                        unoVersus()
                    else:
                        eliminarJugador(eliminado)
                    gestion()
                case 4:
                    if validateResponse(messages.salida):
                        util.clear()
                        return menuPrincipal()
                    else:
                        util.clear()
                        return gestion()
    except ValueError:
        gestion()

def unoVersus():
    try:
        while True :
            playerElec = askAndVerify(messages.unoElec)
            match playerElec:
                case 1 :
                    if validJugadores():
                        oneByOne()
                        unoVersus()
                    else:
                        print(messages.noHayJugadores)
                        unoVersus()
                case 2:
                    if validateResponse(messages.salida):
                        util.clear()
                        return menuPrincipal()
                    else:
                        util.clear()
                        return unoVersus()
    except ValueError:
        unoVersus()

def cpu():
    try:
        while True:
                playerElec = askAndVerify(messages.cpuElec)
                match playerElec:
                    case 1 :
                        if validJugadores():
                            oneByCpu()
                            cpu()
                        else:
                            print(messages.noHayJugadores)
                            cpu()
                    case 2:
                        if validateResponse(messages.salida):
                            util.clear()
                            return menuPrincipal()
                        else:
                            util.clear()
                            return unoVersus()
    except ValueError:
        cpu()