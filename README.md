[logowindows]: https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Windows_logo_-_2012.svg/25px-Windows_logo_-_2012.svg.png 'Windows'
[logomacos]: https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Apple_logo_grey.svg/25px-Apple_logo_grey.svg.png 'macOS'
[logolinux]: https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/TuxFlat.svg/25px-TuxFlat.svg.png 'Linux'

## Tarea 2 - INF 3144 Investigación de operaciones
* **Escuela de Ingeniería Informática | PUCV Chile**
* **1er semestre - 2021**

**Integrantes**:
* Sebastián García Delgadillqo
* Felipe Olivares Abarca
* Ignacio Tornquist Whittaker

**Tema:** Aplicación de metaheurísticas a problema de optimización, aplicando Simulated Annealing para un problema 
tipo TSP (Vendedor viajero).

## Indice

- [IDE de desarrollo](#ide)
- [Instrucciones de ejecución](#ejecucion)
  - [Entorno local](#entorno-local)
  - [Replit](#replit)
  - [Errores de print](#errores-print)
- [Descripción](#descripcion)
- [Documentación](#documetacion)

# IDE
Para el desarrollo de este código, se utilizó **PyCharm** como IDE local, y [Replit](https://replit.com/@SebaGarciaD/simanpython "Replit") como 
servicio colaborativo en linea.

## Ejecucion

### Entorno local

Para ejecutar el programa, es necesario tener instalado Python en el computador. Este programa fue escrito en la 
versión 3.9.4, y se recomienda tener al menos la versión 3.8.x.

Para saber la versión de Python (y si está instalado en el sistema), ejecutar el siguiente comando en el terminal:
* ![Windows][logowindows] o ![Linux][logolinux] `python --version`
* ![Windows][logomacos] `python3 --version`

Una vez revisados los requerimientos, para ejecutar el programa se debe ejecutar el siguiente comando en el terminal 
(se debe estar trabajando en el directorio de este repositorio):
* ![Windows][logowindows] o ![Linux][logolinux] `python main.py`
* ![Windows][logomacos] `python3 main.py`

### Replit

Para ejecutar el programa desde el servicio colaboratívo Replit, es necesario acceder a [este link](https://replit.com/@SebaGarciaD/simanpython "Repositorio Replit") y presionar el botón `run`. El repositorio está configurado para 
automatizar la tarea de ejecución del programa.

### Errores print

El programa, al ejecutarse en la terminal, posee la caracteristica de hacer algunos prints de colores, con el fin de 
mejorar el entendimiento del usuario al ejecutar el programa, pero a su vez puede dar a lugar a problemas visuales, 
si la terminal donde se ejecuta no posee las configuraciones necesarias. En caso de que hayan problemas para 
observar los resultados de la ejecución, el repositorio de git contiene una rama paralela a `main` llamada `nocolor`,
la que desactiva las impresiones a color.

Para acceder a la rama `nocolor`, basta con ejecutar el siguiente comando en la terminal (ubicado en el directorio 
de este repositorio):

```shell
> git checkout nocolor
```

## Descripcion
Programa en Python que realiza 10 ejecuciones de Simulated Annealing para encontrar la mejor combinación posible de
tiendas, tal que la distancia total que recorren todos los asistentes a la misma, sea la mínima, teniendo en cuenta
que se tiene el dato de la cantidad de personas que recorrerán las tiendas i y j.

* El enunciado de la tarea puede encontrarse en [la wiki del proyecto](https://github.com/sebaignacioo/sim_an_python/wiki/Descripcion "Descripción - Wiki")

## Documentacion
La documentación referente a este repositorio de Github se encuentra en la Wiki
* [Acceder a la documentación](https://github.com/sebaignacioo/sim_an_python/wiki "Wiki del proyecto")