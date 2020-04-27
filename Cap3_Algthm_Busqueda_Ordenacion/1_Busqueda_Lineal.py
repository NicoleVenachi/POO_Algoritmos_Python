import random
def busqueda_lineal(lista, objetivo):

    match = False
    for element in lista:
        if element == objetivo:
            match = True
            break

    return match  # O(n)

if __name__ == '__main__':

    list_size = int(input('De que tamano seraa la lista?'))

    objetivo = int(input('Que numero deseas encontrar?'))

    lista = [random.randint(0, 100) for i in range(list_size)]

    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
