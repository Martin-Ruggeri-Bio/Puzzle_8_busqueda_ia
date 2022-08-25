from busquedaAnchura import PuzzleBoard


if __name__ == '__main__':
    size = int(input("Ingrese el tamaño del tablero (3 -> 3x3 o 4 -> 4x4): "))
    puzzle_board = PuzzleBoard(size)
    print("El tamaño de la matriz del puzle elegido es: " + str(puzzle_board.size) + "al cuadrado")
    print("La matriz a modificar es: " + str(puzzle_board.objetivo))
    print("La coordenada del 0 es: " + str(puzzle_board.zero))
    print("Los movimientos posibles son: " + str(puzzle_board.moves))
    print("El tablero de puzzle se ve de la siguiente manera:")
    puzzle_board.printPuzzle()

    option = input("Ingrese 'manual' o 'auto' para mezclar el puzzle: ")
    amount = int(input("Ingrese el numero de movimientos a efectuar en el tablero: "))
    if option == 'manual':
        for i in range(amount):
            move = input("Ingrese el movimiento a efectuar del tablero: ")
            print("Ejecutando movimiento manual")
            puzzle_board.mover(move)
            print("El tablero de puzzle se ve de la siguiente manera:")
            puzzle_board.printPuzzle()
    elif option == 'auto':
        print("Ejecutando movimientos ramdom automaticos")
        puzzle_board.moverEstaCantidad(amount)
        print("El tablero de puzzle se ve de la siguiente manera:")
        puzzle_board.printPuzzle()
    else:
        print("No ingreso una opcion valida")
    option = input("Ingrese 'random' o 'anchura' o 'bidireccional' para buscar la solucion del puzzle: ")
    if option == 'random':
        print("Ejecutando busqueda random")
        puzzle_board.busquedaRandom()
        print("El tablero de puzzle se ve de la siguiente manera:")
        puzzle_board.printPuzzle()
    elif option == 'anchura':
        print("Ejecutando busqueda en anchura")
        puzzle_board.busquedaAnchura()
        print("El tablero de puzzle se ve de la siguiente manera:")
        puzzle_board.printPuzzle()
    elif option == 'bidireccional':
        print("Ejecutando busqueda en anchura")
        puzzle_board.busquedaAnchuraBidireccional()
        print("El tablero de puzzle en el que convergen ambas busquedas se ve de la siguiente manera:")
        puzzle_board.printPuzzle()
    else:
        print("No ingreso una opcion valida")
