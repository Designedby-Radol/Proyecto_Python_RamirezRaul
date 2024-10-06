import os
import json
from .ui import messages
from .ui import util
from importlib.resources import files

MY_DATABASE = files('thechachipun.data').joinpath('juego.json')

def NewFile(*param):
    with open(MY_DATABASE,"w") as wf:
        json.dump(param[0],wf,indent=4)

def ReadFile():
    with open(MY_DATABASE,"r") as rf:
        return json.load(rf)    

def checkFile(*param):
    data = list(param)
    if(os.path.isfile(MY_DATABASE)):
        if(len(param)):
            data[0].update(ReadFile())
    else:
        if(len(param)):
            NewFile(data[0])

def addUser():
    with open(MY_DATABASE, "r+") as f:
        data = json.load(f)
        while True:
            nombre = input(messages.nombre)
            util.clear()
            if nombre.strip() == "":
                input(messages.usuarioVacio)
                util.clear()
            else:
                for jugador_id,jugadorData in data['jugadores'].items():
                    if jugadorData['nombre'] == nombre:
                        print(f"El jugador '{nombre}' ya existe en la base de datos.\n")
                        break
                else:
                    nuevoJugador = {
                        'nombre': nombre,
                        'puntuacion': ''
                    }
                    nuevoId = str(len(data['jugadores']) + 1).zfill(3)
                    data['jugadores'][nuevoId] = nuevoJugador
                    f.seek(0)
                    json.dump(data, f, indent=4)
                    f.truncate()
                    print(f"El jugador '{nombre}' ha sido agregado correctamente.")
                    break

def eliminar_jugador():
    with open(MY_DATABASE, "r+") as f:
        data = json.load(f)
        jugadores = data['jugadores']
        lista_jugadores = ""
        for jugador_id, jugador_data in jugadores.items():
            lista_jugadores += f"{int(jugador_id)} - {jugador_data['nombre']}\n"
        print(lista_jugadores)
        id_jugador_eliminar = input("Ingrese el ID del jugador que desea eliminar: ")
        if id_jugador_eliminar in [str(int(jugador_id)) for jugador_id in jugadores.keys()]:
            del data['jugadores'][list(jugadores.keys())[int(id_jugador_eliminar) - 1]]
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
            print("Jugador eliminado correctamente")
        else:
            print("ID de jugador no encontrado")

def listarJugadores():
    with open(MY_DATABASE, "r") as f:
        data = json.load(f)
        jugadores = data['jugadores']
        listaJugadores = ""
        ultimoId = 0
        for jugadorId, jugadorData in jugadores.items():
            listaJugadores += f"{int(jugadorId)} - {jugadorData['nombre']}\n"
            ultimoId = int(jugadorId)
        return listaJugadores,ultimoId

listaJugadores, ultimoId = listarJugadores()

jugadores = {
        'msg' :f"""
        OPCIONES A ELEGIR
    {listaJugadores}

Elija el numero de jugador:""" ,
    'lastOption' : ultimoId
}
