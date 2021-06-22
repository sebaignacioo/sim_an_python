def leer_datos_desde_archivo(i: int):
    path = f'data/instancia-{i}.txt'
    file = open(path, 'rt')
    cant_puestos = int(file.readline().rstrip('\n'))
    largo_puestos = list(map(int, file.readline().rstrip('\n').rsplit(',')))
    w = []
    for i in range(cant_puestos):
        w.append(list(map(int, file.readline().rstrip('\n').rsplit(','))))
    return {
        'n': cant_puestos,
        'l': largo_puestos,
        'w': w
    }