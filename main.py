from problema import Instancia_Problema as Problema, Solucion_Problema as Solucion
from sim_an import Simulated_Annealing
from datos_archivo import leer_datos_desde_archivo

from color_print import PrintService as PS

def ordenar_soluciones(e: Solucion):
    return e.esfuerzo

def main():
    ps = PS()
    soluciones: list[Solucion] = []

    i = 1 # Elegir número de instancia
    p = Problema(leer_datos_desde_archivo(i), ps)
    s = Simulated_Annealing(p, ps)

    for x in range(10):
        ps.iteracion(x + 1)
        s.simular()
        soluciones.append(s.mejorSolucion)
        s.reiniciar()

    soluciones.sort(key = ordenar_soluciones)
    ps.mejor_solucion(soluciones[0], p.datos['n'])

if __name__ == '__main__':
    main()