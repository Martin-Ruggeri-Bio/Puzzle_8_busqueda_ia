import random
from grafos_puzzle import grafo_orden_3, grafo_orden_4


class PuzzleBoard():
    def __init__(self, size):
        self.size = size
        self.zero = size*size-1
        self.moves = ["U", "D", "L", "R"]
        self.generar_grafo()
    
    def generar_grafo(self):
        if self.size == 3:
            self.objetivo = [1,2,3,4,5,6,7,8,0] 
            self.puzzle = [1,2,3,4,5,6,7,8,0]
            self.grafo = grafo_orden_3
        elif self.size == 4:
            self.objetivo = [1,2,3,4,5,6,7,8,9,10,11,0]
            self.puzzle = [1,2,3,4,5,6,7,8,9,10,11,0]
            self.grafo = grafo_orden_4
        else:
            print("ese tamaño no esta permitido")

    def printPuzzle(self):
        fila_borde = ""
        k = 0
        for i in range(self.size + 2):
            fila_borde += "-"
        print(fila_borde)
        for i in range(0, self.size):
            fila = ""
            for j in range(0, self.size):
                fila += str(self.puzzle[k])
                k += 1
            print("|" + fila + "|")
        print(fila_borde)

    def swap(self, x1, x2):
        # intercambio los valores de las coord (x1) con la (x2)
        temp = self.puzzle[x1]
        self.puzzle[x1] = self.puzzle[x2]
        self.puzzle[x2] = temp

    def up(self):
        # solo puedo mover arriba si no estoy en la fila 0
        if self.zero not in (0, 1, 2):
            self.swap(self.zero, self.zero-3)
            self.zero = self.zero-3
            return 1
        else:
            print("No puedo mover en esa direccion")
            return 0

    def down(self):
        # solo puedo mover abajo si no estoy en la fila n-1
        if self.zero not in (6, 7, 8):
            self.swap(self.zero, self.zero+3)
            self.zero = self.zero+3
            return 1
        else:
            print("No puedo mover en esa direccion")
            return 0

    def left(self):
        # solo puedo mover a la izquierda si no estoy en la columna 0
        if self.zero not in (0, 3, 6):
            self.swap(self.zero, self.zero-1)
            self.zero = self.zero-1
            return 1
        else:
            print("No puedo mover en esa direccion")
            return 0

    def right(self):
        # solo puedo mover a la derecha si no estoy en la columna n-1
        if self.zero not in (2, 5, 8):
            self.swap(self.zero, self.zero+1)
            self.zero = self.zero+1
            return 1
        else:
            print("No puedo mover en esa direccion")
            return 0

    def mover(self, move):
        # mueve el 0 en la direccion que se indica con la inicial
        if move == "U" or move == "u":
            return self.up()
        if move == "D" or move == "d":
            return self.down()
        if move == "L" or move == "l":
            return self.left()
        if move == "R" or move == "r":
            return self.right()
        else:
            print("No puedo mover en esa direccion")
            return 0

    def moverEstaCantidad(self, cantidad):
        contador = 0
        contador_anterior = 0
        while contador != cantidad:
            contador += self.mover(self.moves[random.randrange(0, 4)])
            if contador > contador_anterior:
                print("intento numero: " + str(contador))
                contador_anterior = contador

    def busquedaRandom(self):
        contador = 0
        contador_anterior = 0
        while self.puzzle != self.objetivo:
            contador += self.mover(self.moves[random.randrange(0, 4)])
            if contador > contador_anterior:
                print("intento numero: " + str(contador))
                contador_anterior = contador

    def busquedaAnchura(self):
        listSoluciones = [self.puzzle.copy()]
        contador_nodos = 0
        while True:
            #obtengo el puzzle
            puzzle = listSoluciones[contador_nodos]          
            #obtengo la coord del 0
            zero = puzzle.index(0)
            #recorro los vecinos del zero
            for neighbour in self.grafo[zero]:
                #creo una nueva lista solucion
                neighbour_puzzle = puzzle.copy()
                aux = neighbour_puzzle[neighbour]
                indCero = neighbour_puzzle.index(0)
                neighbour_puzzle[neighbour] = 0
                neighbour_puzzle[indCero] = aux
                # solo agrego la solucion del puzzle si esta no ha sido encontrada antes
                if neighbour_puzzle not in listSoluciones:
                    listSoluciones.append(neighbour_puzzle)
                    self.puzzle = neighbour_puzzle.copy()
                    self.printPuzzle()
            #reviso si encontre la solucion objetivo
            if self.objetivo in listSoluciones:
                print('Objetivo hallado en la posicion: ', listSoluciones.index(self.objetivo), ' ', listSoluciones)
                break
            contador_nodos += 1

    def busquedaAnchuraBidireccional(self):
        listSolucionesOrdenando = [self.puzzle.copy()]
        listSolucionesDesordenando = [self.objetivo.copy()]
        contadorNodosOrdenados = 0
        contadorNodosDesordenados = 0
        coincidencia = False
        while not coincidencia:
            #obtengo el puzzle
            puzzleOrdenando = listSolucionesOrdenando[contadorNodosOrdenados]
            puzzleDesordenando = listSolucionesDesordenando[contadorNodosDesordenados]            
            #obtengo la coord del 0
            zeroOrdenando = puzzleOrdenando.index(0)
            zeroDesordenando = puzzleDesordenando.index(0)
            #recorro los vecinos del zero
            for neighbour in self.grafo[zeroOrdenando]:
                #creo una nueva lista solucion
                neighbour_puzzle = puzzleOrdenando.copy()
                aux = neighbour_puzzle[neighbour]
                indCero = neighbour_puzzle.index(0)
                neighbour_puzzle[neighbour] = 0
                neighbour_puzzle[indCero] = aux
                # solo agrego la solucion del puzzle si esta no ha sido encontrada antes
                if neighbour_puzzle not in listSolucionesOrdenando:
                    listSolucionesOrdenando.append(neighbour_puzzle)
                    self.puzzle = neighbour_puzzle.copy()
                
                #reviso si encontre la solucion objetivo
                if neighbour_puzzle in listSolucionesDesordenando:
                    posiciones = int(listSolucionesOrdenando.index(neighbour_puzzle)) + int(listSolucionesDesordenando.index(neighbour_puzzle))
                    print(f'''Objetivo hallado en un total de {posiciones} posiciones,
                        la lista ordenando es: {listSolucionesOrdenando} 
                        y la lista desordenando es: {listSolucionesDesordenando}''')
                    coincidencia = True
                    break
            contadorNodosOrdenados += 1
            for neighbour in self.grafo[zeroDesordenando]:
                #creo una nueva lista solucion
                neighbour_puzzle = puzzleDesordenando.copy()
                aux = neighbour_puzzle[neighbour]
                indCero = neighbour_puzzle.index(0)
                neighbour_puzzle[neighbour] = 0
                neighbour_puzzle[indCero] = aux
                # solo agrego la solucion del puzzle si esta no ha sido encontrada antes
                if neighbour_puzzle not in listSolucionesDesordenando:
                    listSolucionesDesordenando.append(neighbour_puzzle)
                    self.puzzle = neighbour_puzzle.copy()
                
                #reviso si encontre la solucion objetivo
                if neighbour_puzzle in listSolucionesOrdenando:
                    posiciones = int(listSolucionesOrdenando.index(neighbour_puzzle)) + int(listSolucionesDesordenando.index(neighbour_puzzle))
                    print(f'''Objetivo hallado en un total de {posiciones} posiciones,
                        la lista ordenando es: {listSolucionesOrdenando} 
                        y la lista desordenando es: {listSolucionesDesordenando}''')
                    coincidencia = True
                    break
            contadorNodosDesordenados += 1
