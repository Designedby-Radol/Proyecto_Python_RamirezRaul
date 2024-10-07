from .askUser import askAndVerify,validateResponse
from .ui import messages, util
from .core import validJugadores,addUser,listarJugadores

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
                addUser()
                menuPrincipal()
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
                    player1 = askAndVerify(listarJugadores())
                    print(messages.segundo)
                    player2 = askAndVerify(listarJugadores())
                    if player1 is None or player2 is None:
                        print(messages.usuarioVacio)
                        util.clear()
                        return menuPrincipal()
                    else:
                        pass
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