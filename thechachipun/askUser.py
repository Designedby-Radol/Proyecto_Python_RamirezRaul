from .ui import util,messages

"""
este modulo se va a encargar de preguntar todo lo que necesite al usuario y validar que lo que pregunte sea correcto
"""

#Con esta funcion pido y guardo una eleccion al usuario, dandole un mensaje con opciones para que pueda escoger
def ask(msg):
    try:
        selected = int(input(msg))
        util.clear()
        return selected
    except:
        return None

# esta funcion se en carga de validar que la eleccion del usuario este entre las opciones que previamente le otorgue
def verify(selected, lastOption):
    # print(type(selected))
    # print(type(lastOption))
    # if selected in range(1, lastOption):
    #     selected = True
    # else:
    #     selected = False
    # print (selected)
    return selected if selected in range(1, lastOption+1) else None

#esta funcion se encarga de anidar y dar funcionamiento a las funciones que que piden y verificar una eleccion del usuario
def askAndVerify(askStruct):
    selected = verify(ask(askStruct['msg']), askStruct['lastOption'])
    if selected:
        return selected
    else:
        util.clear()
        input(messages.incorrect)
        util.clear()
        return None

#esta funcion encarga de preguntarle al usuario si desea o no tomar una decision
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
