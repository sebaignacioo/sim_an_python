from random import randrange as random
from color_print import PrintService as PS

class Puesto:
    def __init__(self, largo: int, id: int):
        self.id = id
        self.largo = largo

class Solucion_Problema:
    def __init__(self, solucion, e: float):
        self.solucion = solucion
        self.esfuerzo = e

    def hacer_swap(self):
        rand_1 = random(0, len(self.solucion))
        rand_2 = random(0, len(self.solucion))
        while rand_1 == rand_2: rand_2 = random(0, len(self.solucion))
        n_sol = self.solucion[:]
        aux = n_sol[rand_1]
        n_sol[rand_1] = n_sol[rand_2]
        n_sol[rand_2] = aux
        return n_sol

class Instancia_Problema:
    def __init__(self, datos_archivo: dict, ps: PS):
        self.ps = ps
        self.datos = self.generar_datos_iniciales(datos_archivo)
        self.soluciones: list[Solucion_Problema] = []
        self.solucion_generada: Solucion_Problema
        self.sol_actual: int
        self.ps.datos_iniciales(self.datos)

    def generar_datos_iniciales(self, datos_archivo: dict) -> dict:
        puestos: list[Puesto] = []
        j = 1
        for largo_puestos in datos_archivo['l']:
            puestos.append(Puesto(largo_puestos, j))
            j += 1
        return {
            'n': datos_archivo['n'],
            'w': datos_archivo['w'],
            'puestos': puestos,
            'tInicial': 30.0,
            'tMin': 0.5,
            'alpha': 0.6
        }

    def calcular_distancia(self, i: int, j: int, puestos) -> float:
        sum = 0.0
        sum += (puestos[i - 1].largo)/2
        sum += (puestos[j - 1].largo)/2
        for i in range(i, j - 1):
            sum += puestos[i].largo
        return sum

    def calcular_esfuerzo(self, sol) -> float:
        sum = 0.0
        for i in range(1, len(sol)):
            for j in range(i + 1, len(sol) - 1):
                sum += self.calcular_distancia(i, j, sol) * self.datos['w'][i - 1
                                                                            ][j - 1]
        return sum

    def generar_solucion_inicial(self) -> None:
        puestos = self.datos['puestos'][:]
        solucionRandom: list[Puesto] = []
        while len(puestos) > 0:
            solucionRandom.append(puestos.pop(random(0, len(puestos))))
        esfuerzo = self.calcular_esfuerzo(solucionRandom)
        self.soluciones.append(Solucion_Problema(solucionRandom, esfuerzo))
        self.sol_actual = 0
        self.ps.solucion_inicial(self.soluciones[self.sol_actual])

    def generar_nueva_solucion(self) -> None:
        puestosSwap = self.soluciones[self.sol_actual].hacer_swap()
        self.solucion_generada = Solucion_Problema(puestosSwap, self.calcular_esfuerzo(
            puestosSwap))
        self.ps.swap(self.soluciones[self.sol_actual], self.solucion_generada)

    def aceptar_solucion(self) -> None:
        self.soluciones.append(self.solucion_generada)
        self.sol_actual += 1

    def reiniciar_soluciones(self) -> None:
        self.soluciones.clear()