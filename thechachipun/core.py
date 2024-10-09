import os
import json
from .ui import messages
from .ui import util
from importlib.resources import files
from .askUser import validateResponse

"""
modulo encargado de guardar y cargar persistencia del juego
"""

MY_DATABASE = files('thechachipun.data').joinpath('juego.json')
"""
gracias a la libreria importlib.resources puedo usar la funcion files() para acceder a la carpeta
donde esta anidado el archivo JSON al cual accedo con la funcion .joinpath(). anidandolo en la constante
MY_DATABASE
"""

def newFile(*param):#crear el archivo JSON
    with open(MY_DATABASE,"w") as wf:
        json.dump(param[0],wf,indent=4)

def readFile():#leer el archivo JSON
    with open(MY_DATABASE,"r") as rf:
        return json.load(rf)

def checkFile(*param):#mirar si existe archivo existente JSON
    data = list(param)
    if(os.path.isfile(MY_DATABASE)):# En este caso el archivo se encuentra anidado en MY_DATABASE
        if(len(param)):
            data[0].update(readFile())
    else:
        if(len(param)):
            newFile(data[0])

def addUser():# agregar jugadores al JSON
    with open(MY_DATABASE, "r+") as wtf:
        data = json.load(wtf)
        nombre = input(messages.nombre)#guardar el nombre del nuevo jugador
        util.clear()
        nickname = input(messages.nickname)# y su nickname
        util.clear()
        if nombre.strip() == "":#validar si no se coloca un nombre
            input(messages.usuarioVacio)
            util.clear()
        else:
            for juagdorId,jugadorData in data['jugadores'].items():#validar si el jugador ya esiste dentro del JSON
                if jugadorData['nombre'] == nombre:
                    print(f"El jugador '{nombre}' ya existe en la base de datos.\n")
                    break
            else:
                nuevoJugador = { #propiedades de los jugadores
                    'nombre': nombre,
                    'nickname': nickname,
                    'puntuacion': 0,
                    'escudos': 0,
                    'partidasWia':0,
                    'paridasLia': 0
                }
                nuevoId = str(len(data['jugadores']) + 1).zfill(3)
                data['jugadores'][nuevoId] = nuevoJugador
                wtf.seek(0)# cambia la posición del identificador de archivo a una posición específica dada en este caso la poscicion 0
                json.dump(data, wtf, indent=4)
                wtf.truncate()
                print(f"El jugador '{nombre}' ha sido agregado correctamente.")
        if validateResponse(messages.crear):#pregunta si se quiere crear otro usuario
            util.clear()
            addUser()
        else:
            util.clear()
            return

def eliminarJugador(jugadorId):#elimina jugador pidiendo el id del jugador
    with open(MY_DATABASE, "r+") as f:
        data = json.load(f)
        jugadorIdStr = f"{jugadorId:03d}"
        if jugadorIdStr in data['jugadores']:
            del data['jugadores'][jugadorIdStr]
            jugadores = data['jugadores']
            nuevosJugadores = {}
            for i, (idx, jugadorData) in enumerate(jugadores.items()):
                nuevosJugadores[f"{i+1:03d}"] = jugadorData
            data['jugadores'] = nuevosJugadores
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
            print(messages.eliminado)
        else:
            print(messages.errorEliminado)

def agregarCpuPuntos(nombre, nuevaPuntuacion):#agrega puntos a la pidiendo nombre y puntuacion el nombre depende si la ia es dificil o facil
    with open(MY_DATABASE, "r+") as f:
        data = json.load(f)
        jugador = data[nombre]
        if 'puntuacion' in jugador:
            jugador['puntuacion'] += nuevaPuntuacion
        else:
            jugador['puntuacion'] = nuevaPuntuacion
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

def agregarCpuEscudos(nombre):
    with open(MY_DATABASE, "r+") as f:
        data = json.load(f)
        jugador = data[nombre]
        if 'escudo' in jugador:
            jugador['escudos'] += 1
        else:
            jugador['escudos'] += 1
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

def agregarPuntuacion(jugadorId, nuevaPuntuacion):#agrega puntuacion a usuario pidiendo id y puntos
    juagdorIdStr = f"{jugadorId:03d}"
    with open(MY_DATABASE, "r+") as f:
        data = json.load(f)
        jugador = data['jugadores'][juagdorIdStr]
        if 'puntuacion' in jugador:
            jugador['puntuacion'] += nuevaPuntuacion
        else:
            jugador['puntuacion'] = nuevaPuntuacion
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

def partidasPerdidas(jugadorId): # asigna partidas perdidas contra la ia
    juagdorIdStr = f"{jugadorId:03d}"
    with open(MY_DATABASE, "r+") as f:
        data = json.load(f)
        jugador = data['jugadores'][juagdorIdStr]
        if 'partidasLia' in jugador:
            jugador['partidasLia'] += 1
        else:
            jugador['partidasLia'] = 1
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

def partidasGanadas(jugadorId): # asigna partidas ganadas contra la ia
    juagdorIdStr = f"{jugadorId:03d}"
    with open(MY_DATABASE, "r+") as f:
        data = json.load(f)
        jugador = data['jugadores'][juagdorIdStr]
        if 'partidasWia' in jugador:
            jugador['partidasWia'] += 1
        else:
            jugador['partidasWia'] = 1
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

def agregarEscudos(jugadorId):
    jugadorIdStr = f"{jugadorId:03d}"
    with open(MY_DATABASE, "r+") as f:
        data = json.load(f)
        jugador = data['jugadores'][jugadorIdStr]
        if 'escudo' in jugador:
            jugador['escudos'] += 1
        else:
            jugador['escudos'] += 1
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

def validJugadores():
    with open(MY_DATABASE, "r+") as vl:
        data = json.load(vl)
        if data.get('jugadores', {}):
            return True
        else:
            return False

def validEscudos(jugadorId):
    juagdorIdStr = f"{jugadorId:03d}"
    with open(MY_DATABASE, "r+") as vl:
        data = json.load(vl)
        jugador = data['jugadores'][juagdorIdStr]
        escudo = jugador['escudos']
        if escudo >= 1 :
            return True
        else:
            return False

def estadisticas(): #muestra las estadisticas
    with open(MY_DATABASE, "r") as rsf:
        data = json.load(rsf)
        jugadores = data['jugadores']
        sortedPlayers = sorted(jugadores.items(), key=lambda x: x[1]["puntuacion"], reverse=True)
        print("Ranking de Jugadores:")
        print("----------------------------")
        print("Posición | Nombre | Nickname | Puntuación")
        print("----------------------------")
        for i, (player_id, player_data) in enumerate(sortedPlayers):
            print(f"{i+1} | {player_data['nombre']} | {player_data['nickname']} | {player_data['puntuacion']}")
        print("----------------------------")

        partidasGanadas = max(jugadores.items(), key=lambda x: x[1]["partidasWia"])
        print(f"\nJugador que más ha ganado contra IA: {partidasGanadas[1]['nombre']} ({partidasGanadas[1]['nickname']}) - {partidasGanadas[1]['partidasWia']} partidas")

        partidasPerdidas = max(jugadores.items(), key=lambda x: x[1]["paridasLia"])
        print(f"Jugador que más ha perdido contra IA: {partidasPerdidas[1]['nombre']} ({partidasPerdidas[1]['nickname']}) - {partidasPerdidas[1]['paridasLia']} partidas")
"""
la funcion sorted ordena los numeros de mayor a menor con el parametro reverse = True
donde le pasamos la lista jugadores y apuntamos a la puntuacion con la funcion anonima lambda

las variables  partidasGandadas partidasPerdias se encargan de contener la funcion max que lo que hace es buscar el valor mayor en este caso
entero dentro de lo que apunta la funcion anonima lambda partidas ganadadas y perdidas en su respectivo orden

(en la documentacion README.md se encuentran las documentaciones que use para guiarme y aprender)
"""


def listarJugadores(): #guarda los usuarios y sus nicknames para mostrarlos y guardar el que el usuario elija por medio de la funcion askAndVerify
    with open(MY_DATABASE, "r") as rsf:
        data = json.load(rsf)
        jugadores = data['jugadores']
        listaJugadores = ""
        ultimoId = 0
        for jugadorId, jugadorData in jugadores.items():
            listaJugadores += f"{int(jugadorId)} - {jugadorData['nombre']}  : {jugadorData['nickname']}  \n"
            ultimoId = int(jugadorId)
        return {'msg' :f"""
            OPCIONES A ELEGIR

{listaJugadores}

Elija el numero de jugador: """ ,
            'lastOption' : ultimoId}
