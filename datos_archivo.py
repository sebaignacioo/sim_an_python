def leer_datos_desde_archivo(i: int):
    """
    Función encargada de leer los datos de la instancia desde el archivo correspondiente.
    @type i: int
    @param i: Número de instancia de la que se desea leer sus datos.
    @rtype: dict
    @return: Diccionario con los valores 'n': cantidad de puestos, 'l': lista con el largo de los n puestos y 'w':
    Matriz con la cantidad de personas que desean ir desde el puesto i al puesto j, con i y j <= n.
    """

    path = f'data/instancia-{i}.txt' # Ruta del archivo
    file = open(path, 'rt') # Se abre el archivo

    # Primera linea: La cantidad de puestos a procesar
    cant_puestos = int(file.readline().rstrip('\n'))
    # Segunda linea: Largo de los n puestos, separados por coma
    largo_puestos = list(map(int, file.readline().rstrip('\n').rsplit(',')))
    w = [] # Matriz
    for i in range(cant_puestos):
        # Siguientes n lineas con el valor de Wij, separados por coma
        w.append(list(map(int, file.readline().rstrip('\n').rsplit(','))))

    # Retorna diccionario con la estructura definida.
    return {
        'n': cant_puestos,
        'l': largo_puestos,
        'w': w
    }