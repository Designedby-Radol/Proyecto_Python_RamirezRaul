from .ui import util

def ask(msg):
    try:
        selected = int(input(msg))
        util.clear()
        return selected
    except:
        return None

def verify(selected, lastOption):
    # print(type(selected))
    # print(type(lastOption))
    # if selected in range(1, lastOption):
    #     selected = True
    # else:
    #     selected = False
    # print (selected)
    return selected if selected in range(1, lastOption+1) else None

def askAndVerify(askStruct):
    selected = verify(ask(askStruct['msg']), askStruct['lastOption'])
    if selected:
        return selected
    else:
        util.clear()
        print("Respuesta Incorrecta!\n")
        return None

def validateResponse(message):
    global isAllow
    flagFunction = True
    opciones = ('N','n','S','s')
    try:
        accion = input(f'{message}').upper()
        if (accion not in opciones):
            print('La opcion que ud ingreso no esta permitida.......')
            validateResponse()
        elif (accion == 'S' ):
            flagFunction = True
        elif  ((accion) == 'N'):
            flagFunction = False
        return flagFunction
    except TypeError:
        validateResponse(message)