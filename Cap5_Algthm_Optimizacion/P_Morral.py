'''Un ladron solo tiene una mochila para cargoar cosas, tiene que escoger los articulos qeu gararantizan mayor valor posibles (Puede tomar o no tomar una cosa 0 1 nap-sack).'''

# Complejidad O(n), por cada llamado a funcion recursiva, lo llama una vez
def morral(morral_size, pesos, valores, item_number):
    # Casos Base
    if item_number == 0 or tamano_morral == 0:  # Morral se llena, o no hay mas cosas
        return 0
    if pesos[item_number - 1] > morral_size:  # Si elemento a incluir pesa mas que el tamano restante, sino cabe, voy al siguiente elemento
        return morral(morral_size, pesos, valores, item_number -1)

    # Cuando el elemento si cabe, decido, lo almaceno o no, y lo elige, si maximiza el el valor, si la opcion mejor es guardarolo o no, verifica esta o el siguiente elemento
    return max(valores[item_number-1] + morral(morral_size - pesos[item_number-1], pesos, valores, item_number -1), morral(morral_size,pesos, valores, item_number - 1))
    # Comparo, si tomo elemento que valor tendria, y sino que valor tendria,
    # Si escojo elmento, aumenta valor, y dsiminuye peso disponible
    # Si no lo escojo, no aumenta el vvalor, pero si voy al sgte elemento
if __name__ == '__main__':
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    tamano_morral = 50
    item_number = len(valores)  # Funcionara como indice paara valores/pesos

    resultado = morral(tamano_morral, pesos, valores, item_number)
    print(resultado)
