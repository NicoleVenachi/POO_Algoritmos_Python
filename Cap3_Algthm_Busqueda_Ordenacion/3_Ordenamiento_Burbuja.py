import random

def ordenamiento_burbuja(lista, list_size):

    #  Por el tamano de la lista ('cada elemento'), hago la comparacion con el siguiente, si es menor, los cambio. En cada itearcion acorto la lista, pues tengo la certeza por el funcionamiento del algoritmo, que siempre deja el mayor al final
    #O(n)* O(n-i-1) = O(n)* O(n) = O(n^2)
    for i in range(list_size):  # Para cada elemento de la lista hago lo siguiete (comparacion)
        for j in range(0, list_size - i -1):  # Cada que termino, vuevlo a iniciar en el inicio de la lista. Pricipio, list_size-ya_recorrido-1(indices), pues el mayor siempre se va al final
            print lista
            if lista[j] > lista[j + 1]:  # Si el elemento anterior es mayr al superior
                lista[j], lista [j+1] = lista[j+1], lista [j]

    return lista


if __name__ == '__main__':
    list_size = int(input('De que tamano seraa la lista? \t'))


    lista = [random.randint(0, 100) for i in range(list_size)]
    print(lista)

    ordered_list = ordenamiento_burbuja(lista, list_size)
    print(lista)
