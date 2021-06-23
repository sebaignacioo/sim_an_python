"""
Tarea 2 - INF3144 Investigación de Operaciones
1er semestre 2021

Programa en Python que realiza 10 ejecuciones de Simulated Annealing para encontrar la mejor combinación posible de
tiendas, tal que la distancia total que recorren todos los asistentes a la misma, sea la mínima, teniendo en cuenta
que se tiene el dato de la cantidad de personas que recorrerán las tiendas i y j.

@authors:
    - Sebastián García Delgadillo (P1)
    - Felipe Olivares Abarca (P2)
    - Ignacio Tornquist Whittaker (P2)

- Repositorio Github: https://github.com/sebaignacioo/sim_an_python.git
- Link Github: https://github.com/sebaignacioo/sim_an_python
- Documentación: https://github.com/sebaignacioo/sim_an_python/wiki
"""

# Importaciones propias
from problema import InstanciaProblema as Problema, SolucionProblema as Solucion
from sim_an import SimulatedAnnealing
from datos_archivo import leer_datos_desde_archivo

# Estadísticas
from statistics import mean as promedio, stdev as desv_est
# Impresiones por pantalla
from color_print import PrintService as PS

def obtener_esfuerzo(e: Solucion):
    """
    Función que retorna el esfuerzo de la solución entregada como parámetro.

    @type e: Solucion
    @param e: Solución de la que se desea obtener el esfuerzo.
    @rtype: float
    @return: Esfuerzo de la solución entregada como parámetro.
    """
    return e.esfuerzo

def main():
    """
    Función principal. Encargada de iniciar la ejecución del programa.
    """

    # Parámetros iniciales
    datos_iniciales = {
        't_inicial': 2000,
        't_min': 150,
        'alpha': 0.85
    }

    # Librería para mostrar por pantalla
    ps = PS()
    soluciones: list[Solucion] = []

    i = 2 # Elegir número de instancia
    cant_simulaciones = 10 # Elegir cantidad de simulaciones

    # Se leen los datos desde el archivo y se instancia el problema.
    p = Problema(leer_datos_desde_archivo(i), datos_iniciales, ps)

    s = SimulatedAnnealing(p, ps) # Se instancia Simulated Annealing

    # Se realizan las simulaciones
    for x in range(cant_simulaciones):
        ps.iteracion(x + 1) # Impresión por pantalla
        s.simular() # Se hace la simulación
        soluciones.append(s.mejor_solucion) # Se agrega la mejor solución de la simulación a la lista de soluciones
        s.reiniciar() # Se reinicia la simulación para realizar la siguiente

    # Se ordena la lista de soluciones según el esfuerzo requerido, de menor a mayor (ascendente).
    soluciones.sort(key = obtener_esfuerzo)

    # Impresión por pantalla
    ps.mejor_solucion(soluciones[0], p.datos['n'], promedio(list(map(obtener_esfuerzo, soluciones))), desv_est(list(map(obtener_esfuerzo, soluciones))))

# Se inicia la ejecución del programa
if __name__ == '__main__':
    main()