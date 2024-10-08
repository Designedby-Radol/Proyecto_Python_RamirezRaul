import os
import json
from .ui import messages
from .ui import util
from importlib.resources import files
from .askUser import validateResponse

MY_DATABASE = files('thechachipun.data').joinpath('juego.json')

def newFile(*param):
    with open(MY_DATABASE,"w") as wf:
        json.dump(param[0],wf,indent=4)

def readFile():
    with open(MY_DATABASE,"r") as rf:
        return json.load(rf)    

def checkFile(*param):
    data = list(param)
    if(os.path.isfile(MY_DATABASE)):
        if(len(param)):
            data[0].update(readFile())
    else:
        if(len(param)):
            newFile(data[0])

def addUser():
    with open(MY_DATABASE, "r+") as wtf:
        data = json.load(wtf)
        nombre = input(messages.nombre)
        util.clear()
        nickname = input(messages.nickname)
        util.clear()
        if nombre.strip() == "":
            input(messages.usuarioVacio)
            util.clear()   
        else:
            for juagdorId,jugadorData in data['jugadores'].items():
                if jugadorData['nombre'] == nombre:
                    print(f"El jugador '{nombre}' ya existe en la base de datos.\n")
                    break
            else:
                nuevoJugador = {
                    'nombre': nombre,
                    'nickname': nickname,
                    'puntuacion': 0,
                    'escudos': 0
                }
                nuevoId = str(len(data['jugadores']) + 1).zfill(3)
                data['jugadores'][nuevoId] = nuevoJugador
                wtf.seek(0)
                json.dump(data, wtf, indent=4)
                wtf.truncate()
                print(f"El jugador '{nombre}' ha sido agregado correctamente.")
        if validateResponse(messages.crear):
            util.clear()
            addUser()
        else:
            util.clear()
            return

def eliminarJugador(jugadorId):
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

def agregarCpuPuntos(nuevaPuntuacion):
    with open(MY_DATABASE, "r+") as f:
        data = json.load(f)
        jugador = data['ia']
        if 'puntuacion' in jugador:
            jugador['puntuacion'] += nuevaPuntuacion
        else:
            jugador['puntuacion'] = nuevaPuntuacion
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

def agregarCpuEscudos():
    with open(MY_DATABASE, "r+") as f:
        data = json.load(f)
        jugador = data['ia']
        if 'escudo' in jugador:
            jugador['escudos'] += 1
        else:
            jugador['escudos'] += 1
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

def agregarPuntuacion(jugadorId, nuevaPuntuacion):
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

def agregarEscudos(jugadorId):
    juagdorIdStr = f"{jugadorId:03d}"  
    with open(MY_DATABASE, "r+") as f:
        data = json.load(f)
        jugador = data['jugadores'][juagdorIdStr]
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

# def listarJugadores():
#     with open(MY_DATABASE, "r") as rsf:
#         data = json.load(rsf)
#         jugadores = data['jugadores']
#         listaJugadores = ""
#         ultimoId = 0
#         for jugadorId, jugadorData in jugadores.items():
#             listaJugadores += f"{int(jugadorId)} - {jugadorData['nombre']}\n"
#             ultimoId = int(jugadorId)
#         return {'msg' :f"""
#             OPCIONES A ELEGIR

# {listaJugadores}

# Elija el numero de jugador: """ ,
#             'lastOption' : ultimoId}

def listarJugadores():
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
