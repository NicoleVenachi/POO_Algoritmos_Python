# Implementacion recursiva
import random
def busqueda_binaria(lista, inicio, final, objetivo):

    print(f'Buscado {objetivo} encontre {lista[inicio]},{inicio} y {lista[final-1]},{final}')
    if inicio >= final:  # No se encontro en la lista (Se llega a un punto en el que inicio y final son iguales, o inicio mayor que final, en caso de no hallar el elemento en la lista)
        print('hollla', inicio, final)
        return False
    mitad = (inicio + final) // 2

    if lista[mitad] == objetivo:
        return True
    elif lista[mitad] < objetivo:
        busqueda_binaria(lista,mitad +1, final, objetivo)
    else:
        busqueda_binaria(lista,inicio, mitad - 1, objetivo)
if __name__ == '__main__':

    list_size = int(input('De que tamano seraa la lista? \t'))

    objetivo = int(input('Que numero deseas encontrar? \t'))

    lista = sorted([random.randint(0, 100) for i in range(list_size)])

    encontrado = busqueda_binaria(lista, 0, len(lista)-1, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
