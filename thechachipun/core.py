import os
import json
from .ui import messages
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
        nombre = input(messages.nombre)
        for jugador_id, jugador_data in data['jugadores'].items():
            if jugador_data['nombre'] == nombre:
                print(f"El jugador '{nombre}' ya existe en el archivo JSON.")
                break
        else:
            nuevo_jugador = {
                'nombre': nombre,
                'puntuacion': ''
            }
            nuevo_id = str(len(data['jugadores']) + 1).zfill(3)
            data['jugadores'][nuevo_id] = nuevo_jugador
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
            print(f"El jugador '{nombre}' ha sido agregado correctamente.")