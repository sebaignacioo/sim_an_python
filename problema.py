"""
Este archivo contiene el código relacionado con la instancia del problema y sus soluciones.
"""

# Importaciones
from random import randrange as random # Número random
from color_print import PrintService as PS # Impresion por pantalla


class Puesto:
    def __init__(self, largo: int, id: int):
        """
        Objeto Puesto. Contiene los datos de cada puesto de la feria.

        @type largo: int
        @param largo: Largo del puesto
        @type id: int
        @param id: ID del puesto (números correlativos)
        """
        self.id = id
        self.largo = largo

class SolucionProblema:
    def __init__(self, solucion, e: float):
        """
        Objeto que representa una solución del problema.

        @type solucion: list[Puesto]
        @param solucion: Lista de puestos en el órden de la solución.
        @type e: float
        @param e: Esfuerzo calculado para la solución
        """
        self.solucion = solucion
        self.esfuerzo = e

    def hacer_swap(self):
        """
        Función encargada de realizar un swap desde la solución original, intercambiando 2 posiciones aleatorias.
        @return: Nueva solución, realizando un swap aleatorio desde la solución actual
        @rtype: list[Puesto]
        """
        rand_1 = random(0, len(self.solucion))
        rand_2 = random(0, len(self.solucion))
        while rand_1 == rand_2: rand_2 = random(0, len(self.solucion))
        n_sol = self.solucion[:]
        aux = n_sol[rand_1]
        n_sol[rand_1] = n_sol[rand_2]
        n_sol[rand_2] = aux
        return n_sol

class InstanciaProblema:
    def __init__(self, datos_archivo: dict, datos_iniciales: dict, ps: PS):
        """
        Objeto que representa la instancia del problema.

        @type datos_archivo: dict
        @param datos_archivo: Diccionario que contiene los datos extraídos desde el archivo que contiene los datos de la instancia.
        @type datos_iniciales: dict
        @param datos_iniciales: Diccionario que contiene los parámetros iniciales (establecidos en el programa principal)
        @type ps: PrintService
        @param ps: Librería para hacer impresiones por pantalla
        """
        self.ps = ps
        self.datos = self.generar_datos_iniciales(datos_archivo, datos_iniciales)
        self.soluciones: list[SolucionProblema] = []
        self.solucion_generada: SolucionProblema
        self.sol_actual: int
        self.ps.datos_iniciales(self.datos)

    def generar_datos_iniciales(self, datos_archivo: dict, datos_iniciales: dict) -> dict:
        """
        Función que se encarga de generar un diccionario con los datos de la instancia del problema. Estos datos son
        entregados como parámetros de la función, tanto los extraídos desde el archivo, como los establecidos en el
        programa principal.

        @type datos_archivo: dict
        @param datos_archivo: Diccionario que contiene los datos extraídos desde el archivo que contiene los datos de la instancia.
        @type datos_iniciales: dict
        @param datos_iniciales: Diccionario que contiene los parámetros iniciales (establecidos en el programa principal)

        @rtype: dict
        @return: Diccionario con los datos iniciales: 'n' (int): Numero de puestos, 'w' (list[list[int]]): Cantidad de
        personas que irán del puesto i al j, 'puestos' (list[Puesto]): Puestos de la feria. 't_inicial' (float):
        Temperatura inicial del SimAn. 't_min' (float):  Temperatura mínima del SimAn. 'alpha' (float): Valor de
        alpha de SimAn.
        """
        puestos: list[Puesto] = []
        j = 1
        for largo_puestos in datos_archivo['l']:
            puestos.append(Puesto(largo_puestos, j))
            j += 1
        return {
            'n': datos_archivo['n'],
            'w': datos_archivo['w'],
            'puestos': puestos,
            't_inicial': datos_iniciales['t_inicial'],
            't_min': datos_iniciales['t_min'],
            'alpha': datos_iniciales['alpha']
        }

    def calcular_distancia(self, i: int, j: int, puestos) -> float:
        """
        Función que se encarga de calcular la distancia total entre el puesto en las posiciones i y j. Toma en cuenta
        el largo de ambos puestos, y los largos de todos los puestos que están entre medio.

        @type i: int
        @param i: Posición o índice (parte desde 1) del origen.
        @type j: int
        @param j: Posición o índice (parte desde 1) del destino.
        @type puestos: list[Puesto]
        @param puestos: Lista de puestos de la solución.
        @rtype: float
        @return: Distancia total entre el puesto i y el puesto j
        """

        sum = 0.0 # Inicializa suma en cero

        # Suma la mitad del largo de los puestos i y j
        sum += (puestos[i - 1].largo)/2
        sum += (puestos[j - 1].largo)/2

        # Suma los largos de todos los puestos entre medio
        for k in range(i, j - 2):
            sum += puestos[k].largo
        return sum

    def calcular_esfuerzo(self, sol) -> float:
        """
        Función que se encarga de calcular el esfuerzo requerido según la solución entregada

        @type sol: list[Puesto]
        @param sol: Lista de puestos que contiene los datos de la solución a la que se desea calcular el
        esfuerzo.
        @rtype: float
        @return: Esfuerzo total calculado para la solución
        """

        sum = 0.0 # Inicializa la suma en cero

        # Aplica fórmula del enunciado
        for i in range(1, len(sol)):
            for j in range(i + 1, len(sol) - 1):
                sum += self.calcular_distancia(i, j, sol) * self.datos['w'][i - 1
                                                                            ][j - 1]
        return sum # Retorna el valor de la suma final

    def generar_solucion_inicial(self) -> None:
        """
        Función que se encarga de generar la solución inicial del problema. Utiliza números random para generar una
        solución aleatoria de puestos.
        """

        # Se hace una copia de la lista ordenada de puestos
        puestos = self.datos['puestos'][:]
        solucionRandom: list[Puesto] = [] # Lista con los puestos en órden aleatorio. Inicia vacía.

        # Ciclo de llenado de la solución aleatoria
        while len(puestos) > 0:
            # Se agrega un puesto random a la solución aleatoria
            solucionRandom.append(puestos.pop(random(0, len(puestos))))

        # Se calcula el esfuerzo de la solución propuesta
        esfuerzo = self.calcular_esfuerzo(solucionRandom)
        # Se agrega la solución generada a la lista de soluciones
        self.soluciones.append(SolucionProblema(solucionRandom, esfuerzo))
        self.sol_actual = 0 # Se actualiza el índice de la solución actual
        self.ps.solucion_inicial(self.soluciones[self.sol_actual]) # Impresión por pantalla

    def generar_nueva_solucion(self) -> None:
        """
        Función encargada de generar una nueva solución, a partir de una solución de origen. La solución se genera a
        partir de lo que indique el índice de solución actual, y la genera haciendo swap (intercambio) entre dos
        puestos aleatorios.
        """

        # Invoca el método de la solución actual para realizar swap
        puestosSwap = self.soluciones[self.sol_actual].hacer_swap()

        # Se guarda la nueva solución generada en la variable, y se calcula el esfuerzo total
        self.solucion_generada = SolucionProblema(puestosSwap, self.calcular_esfuerzo(
            puestosSwap))
        self.ps.swap(self.soluciones[self.sol_actual], self.solucion_generada) # Impresión por pantalla

    def aceptar_solucion(self) -> None:
        """
        Función que se encarga de aceptar la solución generada. Agrega la solución a la lista de soluciones,
        y actualiza el valor del índice de la solución actual.
        """
        self.soluciones.append(self.solucion_generada)
        self.sol_actual += 1

    def reiniciar_soluciones(self) -> None:
        """
        Función encargada de reiniciar la instancia del problema para permitir la ejecución de un nuevo ciclo de
        Simulated Annealing.
        """
        self.soluciones.clear()