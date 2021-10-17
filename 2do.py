def crearJugador(jugador:str,posicion:int,turno:int)->list:
    
    jugador: list = [jugador, posicion,turno] 
    return jugador

def buscarnombre(jugador,lista_jugadores)->bool:
    
    for nombre in lista_jugadores:
        if jugador in nombre[0]:
            estar = False
        else:
            estar = True
    return estar

def crearTurnos(lista_jugadores)->tuple:
    
    import random
    
    lista = lista_jugadores.copy()
    primero = random.choice(lista)
    primero[2] = 1
    lista.remove(primero)
    segundo = lista[0]

    return primero,segundo
    
def lanzarDado()->int:
    
    import random    
    pasos = random.randint (1,6)
    
    return pasos


def crearEstadistica(serpiente:int,escalera:int):
    
    contador: list= [serpiente,escalera]
    
    return contador

def estadistica(lista_estadistica,posicionNueva,posicionActualizada):
    
    if(posicionNueva<posicionActualizada):
        print("Serpiente")
        for serpiente in lista_estadistica:
            serpiente = lista_estadistica[0]
            serpienteNueva = serpiente+1
        lista_estadistica[0]=serpienteNueva
        #print(contador)
    elif(posicionNueva>posicionActualizada):
        print("Escalera")
        for escalera in lista_estadistica:
            escalera=lista_estadistica[1]
            escaleraNueva = escalera+1
        lista_estadistica[1]= escaleraNueva
        #print(contador)
    return lista_estadistica

def actualizarPosicion(pasos,jugador,diccionario,lista_estadistica):

        
    for posicion in jugador:
        posicion = jugador[1]
        posicionNueva= posicion+pasos
        
        if posicionNueva in diccionario:
            posicionActualizada = diccionario.get(posicionNueva)            
            estadistica(lista_estadistica,posicionNueva,posicionActualizada)
            jugador[1] = posicionActualizada
            
        else:
            jugador[1] = posicionNueva

        return jugador
    
def resetearEstadistica():
    pass


def imprimirTablero(diccionario):
    
    tablero = [ [100,99,98,97,96,95,94,93,92,91], [81,82,83,84,85,86,87,88,89,90], [80,79,78,77,76,75,74,73,72,71],[61,62,63,64,65,66,67,68,69,70],[60,59,58,57,56,55,54,53,52,51],[41,42,43,44,45,46,47,48,49,50],[40,39,38,37,36,35,34,33,32,31],[21,22,23,24,25,26,27,28,29,30],[20,19,18,17,16,15,14,13,12,11],[1,2,3,4,5,6,7,8,9,10] ]
    for lista in tablero :
        for elemento in range(len(lista)):
            if lista[elemento] in diccionario:
                if lista[elemento] > diccionario.get(lista[elemento]):
                    lista[elemento] = 'escalera'
                elif lista[elemento] < diccionario.get(lista[elemento]):
                    lista[elemento] = 'serpiente'
                    
    return tablero

def actualizarTablero(tablero_inicial,jugador):
    posicion = jugador[1]
    tablero = tablero_inicial
    for lista in tablero:
        for elemento in range(len(lista)):
            if lista[elemento] == posicion:
                lista[elemento] = jugador[0]
    return tablero

def main():
    opcion: str = ''
    jugador: str = ''
    boton:  str=''
    lista_jugadores = []
    posicion_jugador: int = 0
    turno: int = 2
    ULTIMO_CASILLERO: int = 100
    diccionario = {3: 18, 6: 67, 57: 83, 72: 89, 85: 96, 86: 45, 88: 31, 98: 79, 63: 22, 58: 37, 48: 12, 36: 17}
    partida: int=0
    serpiente: int=0
    escalera: int=0
    lista_estadistica = crearEstadistica(serpiente,escalera)

    
    print("Snakes & Ladders ""\n", end="\n")
    
    tablero_inicial = imprimirTablero(diccionario)
    
    for lista in tablero_inicial:
        print(lista,end='\n')
        
    while(opcion != '4'):
       
        print("Menu", end="\n")
        print("1.Iniciar Partida", end="\n")
        print("2.Mostrar estadísticas de casilleros", end="\n")
        print("3.Resetear estadísticas de casilleros", end="\n")
        opcion = input("4.Salir""\n")
        if (opcion == '1'):
            
            jugador = input("Ingrese nombre del primer jugador: ")
            lista_jugadores.append(crearJugador(jugador,posicion_jugador,turno))
            jugador = input("Ingrese nombre del segundo Jugador: ")
            if buscarnombre(jugador,lista_jugadores) == False:
                print("Ya esta el nombre")
                while (buscarnombre(jugador,lista_jugadores) != True):
                    jugador = input("Ingrese nombre del segundo Jugador: ")
            lista_jugadores.append(crearJugador(jugador,posicion_jugador,turno))

            tupla_retornada = crearTurnos(lista_jugadores)
            primer_jugador = tupla_retornada[0]
            segundo_jugador = tupla_retornada[1]
            
            posicionNueva = 0
            posicionActualizada = 0
            
            while (primer_jugador[1] < ULTIMO_CASILLERO) and (segundo_jugador[1] < ULTIMO_CASILLERO):                
                print(primer_jugador[0])
                boton = input("Presiona enter para lanzar dado: ")
                pasos=lanzarDado()
                print("dado: ",pasos)
                actualizarPosicion(pasos,primer_jugador,diccionario,lista_estadistica)
                tablero_inicial = actualizarTablero(tablero_inicial,primer_jugador)
                for lista in tablero_inicial:
                    print(lista,end='\n')
                if primer_jugador[1] < ULTIMO_CASILLERO :
                    print(primer_jugador[1])
                pasos = 0
                
                if(primer_jugador[1] < ULTIMO_CASILLERO):
                    print(segundo_jugador[0])
                    boton = input("Presiona enter para lanzar dado: ")
                    pasos=lanzarDado()
                    print("dado: ",pasos)
                    actualizarPosicion(pasos,segundo_jugador,diccionario,lista_estadistica)
                    tablero_inicial = actualizarTablero(tablero_inicial,segundo_jugador)
                    for lista in tablero_inicial:
                        print(lista,end='\n')
                    if(segundo_jugador[1] >= ULTIMO_CASILLERO):
                        print("Gano el segundo jugador: ",segundo_jugador[0])
                        segundo_jugador[1] = 100
                    else:
                        print(segundo_jugador[1])

                    pasos = 0
                    tablero_inicial = imprimirTablero(diccionario)                     
                elif(primer_jugador[1] >= ULTIMO_CASILLERO):
                    print("Gano el primer jugador: ",primer_jugador[0])
                    primer_jugador[1] = 100
            lista_estadistica = estadistica(lista_estadistica,posicionNueva,posicionActualizada)
            print(lista_estadistica)        
            lista_jugadores = []
            partida+=1
         
        elif(opcion == '2'):
            
            if partida == 0:
                print("No ha iniciado ninguna partida")
            else:
                print('lista estadistica')
                print("Casillero Serpiente: ",lista_estadistica[0])
                print("Casillero Escalera: ",lista_estadistica[1])
        
        elif(opcion == '3'):
            
            print('3')
            lista_estadistica = crearEstadistica(serpiente,escalera)
            print("Casillero Serpiente: ",lista_estadistica[0])
            print("Casillero Escalera: ",lista_estadistica[1])
        
        elif(opcion == '4'):
            
            print("Cordial Despedida")
        
        else:
            print("Debe ingresar un numero del 1 al 4")
            
    
main()