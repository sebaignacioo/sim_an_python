from problema import Instancia_Problema as Problema, Solucion_Problema as Solucion
from color_print import PrintService as PS
from random import random
from math import exp

class Simulated_Annealing:
    def __init__(self, problema: Problema, ps: PS):
        self.ps = ps
        self.mejorSolucion: Solucion
        self.problema = problema
        self.t: float

    def criterio_metropolis(self):
        p = exp(-((self.problema.solucion_generada.esfuerzo - self.problema.soluciones[self.problema.sol_actual].esfuerzo) /
                  self.t))
        nRan = random()
        criterio = p > nRan
        self.ps.criterio_metropolis(criterio, p, nRan)
        return criterio

    def reiniciar(self):
        self.problema.reiniciar_soluciones()
        self.ps.reiniciar()

    def simular(self):
        self.t = self.problema.datos['tInicial']
        self.problema.generar_solucion_inicial()
        while self.t > self.problema.datos['tMin']:
            self.problema.generar_nueva_solucion()
            if self.problema.solucion_generada.esfuerzo < self.problema.soluciones[self.problema.sol_actual].esfuerzo:
                self.problema.aceptar_solucion()
                self.ps.acepta_solucion()
            else:
                if self.criterio_metropolis():
                    self.problema.aceptar_solucion()
            self.t *= self.problema.datos['alpha']
        self.mejorSolucion = self.problema.soluciones[self.problema.sol_actual]