import random

ULTIMO_CASILLERO: int = 100
CANTIDAD_JUGADORES: int = 2
CANTIDAD_CASCARAS: int = 5
CANTIDAD_MAGICOS: int = 3
CANTIDAD_RUSHERO: int = 1
CANTIDAD_HONGOS: int = 1

DICCIONARIO = {3: 18, 6: 67, 57: 83, 72: 89, 85: 96, 86: 45, 88: 31, 98: 79, 63: 22, 58: 37, 48: 12, 36: 17}


def buscar_nombre(nombre: str, jugadores: list) -> bool:
    """
        Precondicion: La lista jugadores contiene elementos [nombre,posicion,turno]
        Postcondicion: Busca un jugador dentro del listado, si lo consigue retorna verdadero
                        hasta que se cumpla lo contrario
    """
    nombre_encontrado: bool = False
    i: int = 0

    while not nombre_encontrado and i < len(jugadores):

        if jugadores[i][0] == nombre:
            nombre_encontrado = True
        i += 1

    return nombre_encontrado


def ingreso_jugadores() -> list:
    """ Precondicion: se deben ingresar dos jugadores

        Postcondicion: retorna una lista de jugadores
    """
    jugadores: list = []
    posicion: int = 0
    turno: int = 2
    cantidad_jugadores: int = 0

    while cantidad_jugadores < CANTIDAD_JUGADORES:

        nombre: str = input("Ingrese nombre: ")
        if len(jugadores) > 0:

            while buscar_nombre(nombre, jugadores):
                print("Otro jugador tiene este nombre:")
                nombre = input("Ingrese otro nombre: ")

        cantidad_jugadores += 1

        jugador: list = [nombre, posicion, turno]
        jugadores.append(jugador)

    return jugadores


def crear_turno(lista_jugadores: list) -> list:
    """ Precondicion: lista jugadores contiene dos listas (jugador)
                        cada una de esas listas tiene un elemento tipo entero en la posicion [2]
                        inicializada en 2
        Postcondicion: escoge una lista al azar, se modifica el elemento[2] (turno) a 1.
                     si esa lista no esta en la primera posicion de la lista_jugadores, se invierte
                     retorna la lista jugadores ordenada por turno
    """
    primero = random.choice(lista_jugadores)
    primero[2] = 1

    if primero != lista_jugadores[0]:
        lista_jugadores.reverse()

    print('empieza: ', lista_jugadores[0])

    return lista_jugadores


def esta_en_diccionario(numero: int) -> bool:
    """ Precondicion: numero es una variable de tipo entero que seria la clave a validar

        Postcondicion: valida si esta en el DICCIONARIO
    """
    numero_encontrado: bool = False

    if (numero in DICCIONARIO) or (numero in DICCIONARIO.values()):
        numero_encontrado = True

    return numero_encontrado


def crear_diccionario_cascara_de_banana() -> dict:
    """ Precondicion: DICCIONARIO contiene items de numeros enteros, compuesto por
                    una clave que seria la cabeza de serpiente o primer escalon y un valor que seria
                    la cola de la serpiente o ultimo escalon (todos enteros)

        Postcondicion: crea llaves aleatorias mientras no exceda el numero de casilleros a crear y
                        tambien mientras no este en la cola,cabeza,primer escalon o ultimo
                        escalon retorna diccionario del casillero banana
    """
    cascara_de_banana: dict = {}
    casillero_cascaras: int = 0

    while casillero_cascaras < CANTIDAD_CASCARAS:

        llave: int = random.randrange(21, 99)
        valor: int = llave - 20

        if not esta_en_diccionario(llave):
            cascara_de_banana[llave] = valor
            casillero_cascaras += 1

    return cascara_de_banana


def esta_en_diccionario_completo(posicion: int, completo: dict) -> bool:
    """ Precondicion: posicion es una variable de tipo entero y completo es un diccionario
                        que contiene items tipo entero
                        recibe un diccionario que incluye los casilleros que se han creado

        Postcondicion: valida si posicion esta en el diccionario "completo" retorna un
                        bool 
    """
    numero_encontrado: bool = False

    if (posicion in completo) or (posicion in completo.values()):
        numero_encontrado = True

    return numero_encontrado


def crear_diccionario_magico(completo: dict) -> dict:
    """ Precondicion: completos diccionario con items de tipo entero 
        Postcondicion: retorna el diccionario casillero magico
    """
    diccionario_casillero_magico: dict = {}
    cantidad_casilleros: int = 0

    while cantidad_casilleros < CANTIDAD_MAGICOS:

        llave: int = random.randrange(2, 99)
        valor: int = random.randrange(2, 99)

        if not esta_en_diccionario_completo(llave, completo):
            diccionario_casillero_magico[llave] = valor
            cantidad_casilleros += 1

    return diccionario_casillero_magico


def crear_matriz() -> list:
    """ Precondicion: numero enteros del 1 al 100
        Postcondicion: retorna lista de listas (matriz) que es el tablero
    """
    tablero: list = []
    n = 100
    for i in range(10):
        tablero.append([])
        for j in range(n, n - 10, -1):
            tablero[i].append(j)
        n -= 10
    return tablero


def crear_casillero_rushero(completo: dict) -> dict:
    """ Precondicion: completo es un diccionario con items de tipo entero que incluye todos
                    los casilleros creados
        Postcondicion: genera una lista restringida con todos los ultimos elemento de cada lista
                    valido que las llave a crear no este en esa lista ni en el diccionario completo y
                    retorna el diccionario casillero rushero
    """
    diccionario_rushero: dict = {}
    matriz = crear_matriz()
    casillero_max: list = []
    casillero_rushero: int = 0

    for piso in matriz:
        casillero_max.append(piso[0])

    while casillero_rushero < CANTIDAD_RUSHERO:

        llave: int = random.randrange(2, 99)

        if not esta_en_diccionario_completo(llave, completo):
            valor: int = 0

            for piso in matriz:
                if llave in piso:
                    valor = piso[0]
            diccionario_rushero[llave] = valor
            casillero_rushero += 1

    return diccionario_rushero


def crear_casillero_hongos_locos(completo: dict) -> dict:
    """ Precondicion: completo es un diccionario con items de tipo entero que incluye todos
                    los casilleros creados
        Postcondicion: genera una lista restringida con todos los ultimos elemento de cada lista
                    valido que las llave a crear no este en esa lista ni en el diccionario completo y
                    retorna el diccionario casillero hongos locos
    """

    diccionario_hongos_locos: dict = {}
    matriz = crear_matriz()
    casillero_min: list = []
    casillero_hongos: int = 0

    for piso in matriz:
        casillero_min.append(piso[9])

    while casillero_hongos < CANTIDAD_HONGOS:

        llave = random.randrange(2, 99)

        if not esta_en_diccionario_completo(llave, completo):
            valor = 0
            for piso in matriz:
                if llave in piso:
                    valor = piso[9]

            diccionario_hongos_locos[llave] = valor
            casillero_hongos += 1

    return diccionario_hongos_locos


def modificar_estadistica(estadistica: dict, posicion: int, cascara: dict, magico: dict, rushero: dict,
                          hongo: dict) -> dict:
    """ Precondicion: recibo un diccionario con items de tipo {cadena:entero} la cadena es el tweak
                        y el entero es el contador

        Postcondicion: retorna lista  estadistica actualizada
    """
    if posicion in cascara:
        contador_cascara = estadistica.get("cascara", 0)  # type: dict[str, int]
        contador_cascara += 1
        estadistica['cascara'] = contador_cascara

        print(contador_cascara)

    elif posicion in magico:
        contador_magico: int = estadistica.get('magico')  # type: dict[str, int]
        contador_magico += 1
        estadistica['magico'] = contador_magico

        print(contador_magico)

    elif posicion in rushero:

        contador_rushero: int = estadistica.get("rushero")
        contador_rushero = contador_rushero + 1
        estadistica['rushero'] = contador_rushero

        print(contador_rushero)

    elif posicion in hongo:

        cantidad: int = estadistica.get("hongos")
        cantidad = cantidad + 1
        estadistica['hongos'] = cantidad

        print(cantidad)

    elif posicion in DICCIONARIO:

        valor: int = DICCIONARIO.get(posicion)

        if posicion > valor:
            cantidad_serpientes = estadistica.get("serpiente")
            cantidad_serpientes += 1
            estadistica['serpiente'] = cantidad_serpientes
            print(cantidad_serpientes)

        elif posicion < valor:
            cantidad_escaleras = estadistica.get("escalera")
            cantidad_escaleras += 1
            estadistica['escalera'] = cantidad_escaleras

            print(cantidad_escaleras)

    return estadistica


def resetear_estadistica(estadistica: dict) -> dict:
    estadistica['serpiente'] = 0
    estadistica['escalera'] = 0
    estadistica['cascara'] = 0
    estadistica['magico'] = 0
    estadistica['rushero'] = 0
    estadistica['hongos'] = 0

    return estadistica


def crear_tablero(cascara:dict, magico:dict, rushero:dict, hongo:dict) -> list:
    """ Precondicion: los diccionarios cascara, magico, rushero, y hongo contienen items de tipo entero
                    {entero:entero} donde la clave (key) el tipo de tweak
        Postcondicion: retorna un tablero -matriz, o lista de listas-
    """
    tablero = crear_matriz()

    for piso in range(1, 10, 2):
        piso_zigzag = tablero[piso]
        piso_zigzag.reverse()

    for lista in tablero:
        for elemento in range(len(lista)):

            if lista[elemento] in rushero:
                lista[elemento] = 'Rush'
            elif lista[elemento] in hongo:
                lista[elemento] = 'HoLo'
            elif lista[elemento] in cascara:
                lista[elemento] = 'CasB'
            elif lista[elemento] in magico:
                lista[elemento] = 'Magic'
            elif lista[elemento] in DICCIONARIO:
                if lista[elemento] > DICCIONARIO.get(lista[elemento]):
                    lista[elemento] = 'Serp'
                elif lista[elemento] < DICCIONARIO.get(lista[elemento]):
                    lista[elemento] = 'Escal'

    return tablero


def imprimir_tablero(tablero:list) -> None:
    """ Es un procedimiento
        Precondicion: tablero es una lista que contiene elementos tipo enteros son los casilleros del tablero
        Postcondidicon: imprime
    """
    for lista in tablero:
        for elemento in lista:
            print(elemento, end="\t")
        print(end='\n')


def actualizar_tablero(tablero_inicial: list, jugador: list) -> None:
    """ Es un procedimiento
        Precondicion: tablero_inicial es una lista de listas contiene elementos de tipo entero numeros
                    y otros de tipo cadena,la lista jugador contiene datos tipo (cadena,entero,entero)
                    que serian (nombre posicion turno)
        Postcondicion: recorre el tablero y reemplaza el casillero por el jugador
                      imprime el movimiento del jugador sobre el tablero
    """
    posicion = jugador[1]
    tablero = tablero_inicial
    for lista in tablero:
        for elemento in range(len(lista)):
            if lista[elemento] == posicion:
                lista[elemento] = jugador[0]

    imprimir_tablero(tablero)


def validar_posicion(jugador: list, cascara: dict, magico: dict, rushero: dict, hongo: dict, estadistica: dict) -> list:
    """ Precondicion: la lista jugador contiene en su segundo elemento (posicion 1) un entero que es la posicion
                    cascara,magico,rushero,hongo son diccionarios de los tweaks que contienen elementos de tipo
                    {entero:entero}
                
        Postcondicion: busca la posicion del jugador en los diccionarios, si esta actualiza la posicion de ese jugador
                    retorna la lista jugador 
    """
    posicion = jugador[1]
    print(posicion)

    if posicion in DICCIONARIO:
        posicion_actualizada = DICCIONARIO.get(posicion)
        modificar_estadistica(estadistica, posicion, cascara, magico, rushero, hongo)
        if posicion_actualizada < posicion:
            print("serpiente")
        elif posicion_actualizada > posicion:
            print("escalera")
    elif posicion in cascara:
        print("cascara de banana")
        posicion_actualizada = cascara.get(posicion)
        modificar_estadistica(estadistica, posicion, cascara, magico, rushero, hongo)
    elif posicion in magico:
        print("casillero magico")
        posicion_actualizada = magico.get(posicion)
        modificar_estadistica(estadistica, posicion, cascara, magico, rushero, hongo)
    elif posicion in rushero:
        print("casillero rushero")
        posicion_actualizada = rushero.get(posicion)
        modificar_estadistica(estadistica, posicion, cascara, magico, rushero, hongo)
    elif posicion in hongo:
        print("casillero hongo")
        posicion_actualizada = hongo.get(posicion)
        modificar_estadistica(estadistica, posicion, cascara, magico, rushero, hongo)

    else:
        print('casillero normal')
        posicion_actualizada = posicion

    jugador[1] = posicion_actualizada

    return jugador


def definir_ganador(jugador: list) -> bool:
    """ Precondicion: jugador es una lista que contiene elementos de tipo [cadena,entero,entero]
                    en el indice 1 se encuentra la posicion 
                
        Postcondicion: si la posicion del jugador es mayor o igual al ultimo casillero
                    retorna verdadero 
    """    
    ganador: bool = False

    if jugador[1] > ULTIMO_CASILLERO:
        jugador[1] = 100
        ganador = True

    return ganador


def mover_pieza(jugador: list, tablero: list, cascara: dict, magico: dict, rushero: dict, hongo: dict,
                estadistica: dict) -> None:
    """ es un procedimiento que se repite por cada turno que se genere
        Precondicion: jugador es una lista que contiene elementos de tipo [cadena,entero,entero]
                    en el indice 1 se encuentra la posicion, tbalero es una "matriz" o listas de listas
                    que contiene elementos de tipo entero y tipo cadena que serian los casillero
                    
        Postcondicion: genera los pasos de manera aleatoria entre 1 y 6 modifica la posicion del jugador
                        comprueba si esta en algun tweak, verifica si gana, actualiza el tablero
    """ 
    pasos = random.randint(1, 6)
    print("dado: ", pasos)
    indice_posicion = jugador[1]
    posicion = indice_posicion + pasos
    jugador[1] = posicion
    validar_posicion(jugador, cascara, magico, rushero, hongo, estadistica)

    if definir_ganador(jugador):
        print('Ganaste ', jugador[0])

    print('posicion ', jugador[1])
    actualizar_tablero(tablero, jugador)


def turnos_partida(jugadores: list, tablero: list, cascara: dict, magico: dict, rushero: dict, hongo: dict,
                   estadistica: dict)->None:
    """ es un procedimiento de la opcion 1 del menu, es el partido
        Precondicion: jugadores es una lista de listas o "matriz" que contiene la lista jugador que contiene
                    elementos de tipo [cadena,entero,entero] representa [nombre,posicion,turno]
                    tabalero es una "matriz" o listas de listas
                    que contiene elementos de tipo entero (casilleros) y tipo cadena (tweaks)
                    los diccionarios cascara, magico, rushero, y hongo contienen items de tipo entero
                    {entero:entero} donde la clave (key) el tipo de tweak y el valor es la translacion
                    estadistica es un diccionario que contiene items de tipo {cadena:entero} representando
                    {tweak:contador} 
                    
        Postcondicion: mientras la posicion del jugador sea menor jugador al ultimo jugador
                    se va a "jugar"
        
    """
    boton: str = ''
    primer_jugador = jugadores[0]
    segundo_jugador = jugadores[1]
    turno = 1

    while (primer_jugador[1] < ULTIMO_CASILLERO) and (segundo_jugador[1] < ULTIMO_CASILLERO) and (boton==''):

        if (primer_jugador[1] < ULTIMO_CASILLERO) and (turno % 2 != 0):
            print("Le toca a: ", primer_jugador[0])
            boton = input("Presiona enter para lanzar dado, culquier otro caracter para terminar partida: ")
            mover_pieza(primer_jugador, tablero, cascara, magico, rushero, hongo, estadistica)

        else:
            print("Le toca al jugador 2", segundo_jugador[0])
            boton = input("Presiona enter para lanzar dado, culquier otro caracter para terminar partida: ")
            mover_pieza(segundo_jugador, tablero, cascara, magico, rushero, hongo, estadistica)
        tablero = crear_tablero(cascara, magico, rushero, hongo)
        turno += 1


def imprimir_estadistica(contador_partida: int, estadistica: dict) -> None:
    """ Procedimiento
        Precondicion: contador_partida numero de veces que se ha iniciado la partida
                    estadistica es un diccionario que contiene items de tipo {cadena:entero} representando
                    {tweak:contador} 
        Postcondicion: si se ha iniciado al menos una partida imprime los valores del diccionario estadistica
    
    """
    if contador_partida == 0:
        print("No ha iniciado ninguna partida")
    else:

        print("Casillero Serpiente: ", estadistica.get("serpiente"))
        print("Casillero Escalera: ", estadistica.get("escalera"))
        print("Casillero Cascara de banana: ", estadistica.get("cascara"))
        print("Casillero Magico: ", estadistica.get("magico"))
        print("Casillero Rushero: ", estadistica.get("rushero"))
        print("Casillero Hongos Locos: ", estadistica.get("hongos"))


def main():
    opcion: str = ''
    estadistica: dict = {'serpiente': 0, 'escalera': 0, 'cascara': 0, 'magico': 0, 'rushero': 0, 'hongos': 0}
    contador_partida: int = 0
    posicion: int = 0

    #print("diccionario original", DICCIONARIO)
    dicionario_validacion = {}
    dicionario_validacion.update(DICCIONARIO)
    cascara = crear_diccionario_cascara_de_banana()
    #print("diccionario cascaraas", cascara)
    dicionario_validacion.update(cascara)
    magico = crear_diccionario_magico(dicionario_validacion)
    #print("diccionario magico", magico)
    dicionario_validacion.update(magico)
    rushero = crear_casillero_rushero(dicionario_validacion)
    #print('diccionario_rushero', rushero)
    hongo = crear_casillero_hongos_locos(dicionario_validacion)
    #print("diccionario hongos locos: ", hongo)
    dicionario_validacion.update(hongo)
    #print('diccionario completo:', dicionario_validacion)

    print("Snakes & Ladders ""\n", end="\n")

    tablero = crear_tablero(cascara, magico, rushero, hongo)
    imprimir_tablero(tablero)

    while opcion != '4':

        print("Menu", end="\n")
        print("1.Iniciar Partida", end="\n")
        print("2.Mostrar estadísticas de casilleros", end="\n")
        print("3.Resetear estadísticas de casilleros", end="\n")
        opcion = input("4.Salir""\n")

        if opcion == '1':

            jugadores: list = ingreso_jugadores()
            print(jugadores)
            jugadores: list = crear_turno(jugadores)
            print(jugadores)

            turnos_partida(jugadores, tablero, cascara, magico, rushero, hongo, estadistica)

            estadistica = modificar_estadistica(estadistica, posicion, cascara, magico, rushero, hongo)
            contador_partida += 1

        elif opcion == '2':

            imprimir_estadistica(contador_partida, estadistica)

        elif opcion == '3':

            resetear_estadistica(estadistica)
            imprimir_estadistica(contador_partida, estadistica)

        elif opcion == '4':

            print("Cordial Despedida")

        else:
            print("Debe ingresar un numero del 1 al 4")


main()
