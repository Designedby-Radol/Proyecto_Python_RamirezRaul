from .askUser import askAndVerify,validateResponse
from .ui import messages, util
from .core import validJugadores,addUser,listarJugadores,eliminarJugador,agregarPuntuacion
from .modules import oneByOne

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
                pass
            case 3:
                if validateResponse(messages.salida):
                    return
                else:
                    util.clear()
                    menuPrincipal()
    except:
        pass

def unoVersus():
    try:
        if validJugadores():
            playerElec = askAndVerify(messages.playerElec)
            match playerElec:
                case 1 :
                    oneByOne()
                    unoVersus()
                case 2 :
                    addUser()
                    unoVersus()
                case 3:
                    eliminado = askAndVerify(listarJugadores())
                    eliminarJugador(eliminado)
                    unoVersus()
                case 4:
                    if validateResponse(messages.salida):
                        util.clear()
                        return menuPrincipal()
                    else:
                        util.clear()
                        return unoVersus()
        else:
            addUser()
            menuPrincipal()
    except:
        pass
