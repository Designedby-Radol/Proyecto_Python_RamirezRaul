<div align="center">

# TheChachipun

</div>


"The Chachipun" (también conocido como piedra, papel o tijera), donde en cada ronda los dos competidores deben tomar una decisión estratégica entre las tres opciones posibles: piedra, papel o tijera. La dinámica del juego se basa en las siguientes reglas: la tijera corta el papel, el papel envuelve la piedra y la piedra rompe la tijera. Si ambos jugadores eligen la misma opción, la ronda se considera un empate.

Un juego sencillo donde un jugador podra jugar piedra papel o tijera con otro jugador o con 2 ia una en modo facil y otra en modo dificil, el jugador podra guardar su puntuacion y mostrarla o compoararla con la de otros jugadores

<div align="center">

# Comandos De Ejecucion

Este programa contiene archivos de configuracion que permiten que el programa sea mucho mas intuitivo de ejecutar de esta manera podemos encontrar diferentes comandos con los cuales podemos ejecutar el programa :

```
#shell
./run

[WINDOWS /LINUX]
python3 -m thechachipun

#PowerShell
./run.ps1
```

</div>

<div align="center">

# Funcionamiento

</div>

En el proyecto podremos encontrar diferentes modulos los cuales nos ayudaran a poder ejecutar el juego de manera correcta y ordenada para que tanto jugadores como otros desarrolladores puedan tener una buena experiencia disfrutando del juego (todos los modulos estan documentados para una mejor comprension y manejo del codigo. Cada modulo ha sido diseñado con principios de modularidad y cohesion, lo que facilita su mantenimiento y actualización.)

### modulos

> ### Funcionamiento principal

- _**main**_ (Modulo principal de ejecucion del programa )
- _**game**_ (Modulo donde encontraremos el menu principal del juego)
- _**modules**_ (Redundancia donde encontramos la logica interna del juego/programa y su funcionamiento en escencia)
- _**core**_ (Modulo donde encotraremos la logica de persistencias de datos del JSON)
- _**askUser**_ (Modulo donde le pediremos datos al usuario para poder naveegar en el programa)
- _**messages**_ (Modulo de utilidad para el programa donde guardamos mensajes preddeterminados que se mostraran durante el programa)
- _**util**_ (Modulo de utilidad usado para tareas monotonas al ejecutar el programa)
- _**data**_ (Modulo donde se anida el archivo de texto json parte de la ejecucion del programa principal)
- _**juego.json**_ (Archivo json que se creara al inicio de la ejecucion del programa, donde se guardara la persistencia del programa para su funcionamiento)

> ### Funcionamiento secundario: edicion/configuracion

- _**run**_ (Archivo tipo shell el cual se encarga de ejecutar programa con un comando llamado igual que el nombre del archivo de esta forma ./run "solo corre en terminales shell")
- _**run.ps1**_ (Archivo tipo PowerShell el cual se encarga de ejecutar programa con un comando llamado igual que el nombre del archivo de esta forma ./run "solo corre en terminales PowerShell")
- _**editorconfig**_ (como su nombre lo dice es un archivo de configuracion de editor)
- _**gitignore**_ (Archivo de configuracion de git que ignora archivos o directorios inecesarios a la hora de subir mi proyecto)

<div align="center">

# Estructura Json

</div>


```json
{
    "jugadores": {
        "001": {
            "nombre": "",
            "nickname": "",
            "puntuacion": 0,
            "escudos": 0,
            "partidasWia": 0,
            "paridasLia": 0
        },
        "002": {
            "nombre": "",
            "nickname": "",
            "puntuacion": 0,
            "escudos": 0,
            "partidasWia": 0,
            "paridasLia": 0,
            "partidasLia": 1
        },
        "003": {
            "nombre": "",
            "nickname": "",
            "puntuacion": 0,
            "escudos": 0,
            "partidasWia": 0,
            "paridasLia": 0
        }
    },
    "ia": {
        "puntuacion": 0,
        "escudos": 0
    },
    "ia_dificil": {
        "puntuacion": 0,
        "escudos": 0
    }
}
```


## Enlaces

_**importlib**_ https://docs.python.org/3/library/importlib.resources.html

_**lambda**_ https://www.freecodecamp.org/espanol/news/funciones-lambda-en-python-ejemplos-de-sintaxis/

_**random choices**_ https://www.geeksforgeeks.org/how-to-get-weighted-random-choice-in-python/

_**funcion max**_ https://interactivechaos.com/es/python/function/max

_**shell file**_ https://www.geeksforgeeks.org/shell-script-examples/

_**editorconfig**_ https://editorconfig.org/
