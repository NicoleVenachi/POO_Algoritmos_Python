import random
# Implementacion recursiva
def ordenamiento_por_mezcla(lista):

    # Dividir listas
    if len(lista) > 1:  # Caso base, =1, Subdivido listas hasta que su longitud no sea mas grande que 1. Crecimiento long(n)
        medio = len(lista) // 2
        izquierda = lista[:medio]  # Final no inclusivo
        derecha = lista[medio:]  # Inicio si inclusivo
        print(izquierda, '*' * 5, derecha)

        # LLamada recursiva en cada mitad, crea resto de marcos
        ordenamiento_por_mezcla(izquierda)
        ordenamiento_por_mezcla(derecha)


        # Cuando ya tenemos listas pequenas, las comparamos
        # Iteradores para recorrer sublistas
        i = 0
        j = 0
        # Iterador lista principal
        k = 0

        # Comparaciones entre listas, esto lo hace en cada macro, o sea cada par de listas
        while i < len(izquierda) and j < len(derecha):  # Mientras pueda seguir coomparando, extremos

            # Comparo extremos, y veo cual es menor o mayor
            if izquierda[i] < derecha[j]:  # Si lista izq es menor
                lista[k] = izquierda [i]
                i += 1
            else:  # Si lista der es mayor
                lista[k] = derecha [j]
                j += 1
            k += 1
        while  i < len(izquierda):  # Si sobra lista en la izq, la copio
            lista[k] = izquierda[i]
            i += 1
            k += 1
        while  j < len(derecha):  # Si sobra lista en la izq, la copio
            lista[k] = derecha[j]
            j += 1
            k += 1
        print(f'izquierda{izquierda}, derecha {derecha}')
        print(lista)
        print('*' * 50)
    return lista


if __name__ == '__main__':
    list_size = int(input('De que tamano seraa la lista? \t'))


    lista = [random.randint(0, 100) for i in range(list_size)]
    print(lista)
    print('*' * 20)

    ordered_list = ordenamiento_por_mezcla(lista)
    print(lista)
