from .askUser import askAndVerify,validateResponse
from .ui import messages, util
from .core import validJugadores,addUser,listarJugadores

def menuPrincipal():
    try:
        if validJugadores():
            playerElec = askAndVerify(messages.playerElec)
            match playerElec:
                case 1 :
                    player1 = askAndVerify(listarJugadores())
                    return player1
                case 2 :
                    addUser()
                    menuPrincipal()
                case 3:
                    pass
                case 4:
                    
                    if validateResponse(messages.salida):
                        return
                    else:
                        util.clear()
                        menuPrincipal()
        else:
            addUser()
            menuPrincipal()
    except:
        pass