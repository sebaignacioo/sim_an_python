class ColorMessage:
    def __init__(self):
        self.__colorDict = {
            "reset": ""
        }

    def __resetColor(self) -> None:
        print(self.__colorDict["reset"], end="")

    def printColor(self, value, color = "", inicio = "", fin = "\n") -> None:
        if self.__colorDict.get(color) != None:
            print(f"{self.__colorDict.get(color)}{inicio}{value}", end = fin)
        else:
            print(f"{inicio}{value}", end = fin)
        self.__resetColor()

class PrintService:
    def __init__(self):
        self.colorMsg = ColorMessage()

    def iteracion(self, i: int) -> None:
        self.colorMsg.printColor(f'| Iteración No. {i} |', inicio = '\n\n' + '-' * 30, fin = '-' * (30 - len(str(i))
                                                                                                    + 2) + '\n\n')
    def datos_iniciales(self, datos: dict) -> None:
        self.colorMsg.printColor('-' * 80)
        self.colorMsg.printColor('|' + '-' * 5 + ' Datos iniciales ' + '-' * 6 + '|', inicio = '-' * 25,
                                 fin='-' * 25 + '\n')
        self.colorMsg.printColor('| ' + f'* Cant. Puestos: {datos["n"]}' + ' ' * (9 - len(str(datos['n'])) + 1) + '|', inicio='-' * 25,
                                 fin='-' * 25 + '\n')
        self.colorMsg.printColor('| ' + f'* T. inicial: {datos["t_inicial"]:.0f}' + ' ' * 9 + '|', inicio='-' * 25,
                                 fin='-' * 25 + '\n')
        self.colorMsg.printColor('| ' + f'* T. minima: {datos["t_min"]:.1f}' + ' ' * 9 + '|', inicio='-' * 25,
                                 fin='-' * 25 + '\n')
        self.colorMsg.printColor('| ' + f'* alpha: {datos["alpha"]:.2f}' + ' ' * 14 + '|', inicio='-' * 25,
                                 fin='-' * 25 + '\n')
        self.colorMsg.printColor('|' + '_' * 28 + '|', inicio='-' * 25, fin='-' * 25 + '\n')
        self.colorMsg.printColor('-' * 80)

    def solucion(self, sol, color: str = '') -> None:
        for p in sol.solucion:
            self.colorMsg.printColor(f'[{p.id}]', color = color, fin = '')

    def esfuerzo(self, sol, color: str = '') -> None:
        self.colorMsg.printColor(f' | Esfuerzo: {sol.esfuerzo}', color=color, fin='')

    def solucion_inicial(self, solucion) -> None:
        self.colorMsg.printColor('=> Solución inicial generada:', color = 'blue', fin = ' ')
        self.solucion(solucion, color = 'blue')
        self.esfuerzo(solucion, color = 'blue')
        print('\n')

    def swap(self, s1, s2) -> None:
        self.colorMsg.printColor('=> Haciendo Swap:', fin=' ', inicio=' ' * 2)
        self.solucion(s1)
        self.colorMsg.printColor('->', fin=' ', inicio=' ')
        self.solucion(s2)
        if s1.esfuerzo > s2.esfuerzo:
            estado_sol = 'mejora'
        elif s1.esfuerzo == s2.esfuerzo:
            estado_sol = 'iguales'
        else:
            estado_sol = 'peor'
        self.colorMsg.printColor(f'Esfuerzo: {s1.esfuerzo} -> {s2.esfuerzo} / {estado_sol}', inicio='\n' + ' ' * 10)

    def acepta_solucion(self) -> None:
        self.colorMsg.printColor('OK Se acepta la nueva solución', color = 'green', inicio=' ' * 10)

    def rechaza_solucion(self) -> None:
        self.colorMsg.printColor('X Se rechaza la nueva solución', color = 'red', inicio=' ' * 10)

    def criterio_metropolis(self, acepta: bool, p: float, rand: float) -> None:
        self.colorMsg.printColor(f'=> Criterio de metrópolis: p = {p:.4f} | rand = {rand:.4f}', color='yellow',
                                 inicio=' ' * 10)
        if acepta: self.acepta_solucion()
        else: self.rechaza_solucion()

    def reiniciar(self) -> None:
        self.colorMsg.printColor('-' * 80, inicio='\n\n', fin='\n\n')

    def mejor_solucion(self, solucion, n: int , m: float, de: float) -> None:
        self.colorMsg.printColor('| Mejor solución |', inicio='\n\n' + '-' * 30,
                                 fin='-' * 30 + '\n\n')
        self.colorMsg.printColor(f'=> Mejor solución encontrada en 10 iteraciones es:', color='green')
        self.solucion(solucion, color='green')
        self.esfuerzo(solucion, color='green')
        self.colorMsg.printColor(f'\nEstadísticas: Media = {m:.4f} | Desv. Est. = {de:.4f}', inicio = ' ' * 2,
                                 color='green', fin = '\n')