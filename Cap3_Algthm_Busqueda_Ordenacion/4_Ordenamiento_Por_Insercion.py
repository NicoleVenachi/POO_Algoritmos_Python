import random
def ordenamiento_por_insercion(lista):

    for indice in range(1, len(lista)):
        #  Tomo pos y valor actual (lista desordenada)
        valor_actual = lista[indice]
        posicion_actual = indice

        #  Para la segunda posicion (lista desordenada), Ultimo elemento de lista ordeada sea mayor que el ultimo elemento lista desordenada, hasta el primero.
        #  Si el elemento de la lista ordenada, es mayor que el de la desordenadaordeada
        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            #  El el3mento de la Lista ordenada es igual al el3mento de la desordenada, porque este era mayor
            lista[posicion_actual] = lista[posicion_actual - 1]
            # Pruebo para cada elemento
            posicion_actual -= 1
            print('############')
            print(lista)

        #  Como cambio el elemento de la lista ordenada, el indice previo de la ordenada tendra el valor de la desordenada
        lista[posicion_actual] = valor_actual
        print('--------------------')
        print(lista)
    return lista


if __name__ == '__main__':

    list_size = int(input('De que tamano seraa la lista? \t'))


    lista = [random.randint(0, 100) for i in range(list_size)]
    print(lista)

    ordered_list = ordenamiento_por_insercion(lista)
    print(lista)
