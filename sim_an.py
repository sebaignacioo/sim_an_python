"""
Este archivo contiene el código relacionado con la instancia y ejecución de la aplicación de la metaheurística
Simulated Annealing al la instancia del problema.
"""

# Importaciones
from problema import InstanciaProblema as Problema, SolucionProblema as Solucion # Instancias problema/solución
from color_print import PrintService as PS # Impresion por pantalla
from random import random # Número random
from math import exp # Para calcular el criterio metrópolis

class SimulatedAnnealing:
    def __init__(self, problema: Problema, ps: PS):
        """
        Objeto SimulatedAnnealing que permite instanciar y realizar la simulación, utilizando la metaheurística.

        @type problema: Problema
        @param problema: Instancia del problema
        @type ps: PS
        @param ps: Librería para hacer impresiones por pantalla
        """
        self.ps = ps
        self.mejor_solucion: Solucion
        self.problema = problema
        self.t: float

    def criterio_metropolis(self):
        """
        Función encargada de verificar si una solución es aceptada o no, utilizando el criterio de metrópolis.

        @rtype: bool
        @return: Valor de verdad, si es aceptada o no la solución generada.
        """

        # Se calcula el valor de p según fórmula
        p = exp(-((self.problema.solucion_generada.esfuerzo - self.problema.soluciones[self.problema.sol_actual].esfuerzo) /
                  self.t))

        num_ran = random() # Se genera un número aleatorio entre 0 y 1
        criterio = p > num_ran # Se guarda valor de verdad, si la solución es o no aceptada

        self.ps.criterio_metropolis(criterio, p, num_ran) # Impresión por pantalla
        return criterio # Se retorna el valor de verdad

    def reiniciar(self):
        """
        Función encargada de reiniciar la instancia del problema, para poder realizar una nueva simulación.
        """

        self.problema.reiniciar_soluciones() # Se reinician las soluciones de la instancia del problema.
        self.ps.reiniciar() # Impresión por pantalla

    def simular(self):
        """
        Función encargada de realizar la simulación de la metaheurística Simulated Annealing. Sigue la pauta del
        enunciado y del pseudocódigo explicado en el informe del trabajo, y la documentación del proyecto.
        """
        self.t = self.problema.datos['t_inicial']
        self.problema.generar_solucion_inicial()
        while self.t > self.problema.datos['t_min']:
            self.problema.generar_nueva_solucion()
            if self.problema.solucion_generada.esfuerzo < self.problema.soluciones[self.problema.sol_actual].esfuerzo:
                self.problema.aceptar_solucion()
                self.ps.acepta_solucion()
            else:
                if self.criterio_metropolis():
                    self.problema.aceptar_solucion()
            self.t *= self.problema.datos['alpha']
        self.mejor_solucion = self.problema.soluciones[self.problema.sol_actual]