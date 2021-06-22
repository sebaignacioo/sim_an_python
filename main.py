from problema import Instancia_Problema as Problema, Solucion_Problema as Solucion
from sim_an import Simulated_Annealing
from datos_archivo import leer_datos_desde_archivo
from statistics import mean as promedio, stdev as desv_est

from color_print import PrintService as PS

def obtener_esfuerzo(e: Solucion):
    return e.esfuerzo

def main():
    datos_iniciales = {
        't_inicial': 2000,
        't_min': 150,
        'alpha': 0.85
    }
    ps = PS()
    soluciones: list[Solucion] = []

    i = 2 # Elegir número de instancia
    p = Problema(leer_datos_desde_archivo(i), datos_iniciales, ps)
    s = Simulated_Annealing(p, ps)

    for x in range(10):
        ps.iteracion(x + 1)
        s.simular()
        soluciones.append(s.mejor_solucion)
        s.reiniciar()

    soluciones.sort(key = obtener_esfuerzo)
    ps.mejor_solucion(soluciones[0], p.datos['n'], promedio(list(map(obtener_esfuerzo, soluciones))), desv_est(list(map(obtener_esfuerzo, soluciones))))

if __name__ == '__main__':
    main()