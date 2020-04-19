class Lavadora:

    def __init__(self):
        pass

    def lavar(self, temperatura = 'caliente'):
        self._llenar_tanque_de_agua(temperatura)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()  # Ciclo de lavado

    def _llenar_tanque_de_agua(self, temperatura):
        print(f'LLenando el tanque con agua a {temperatura} temperatura')

    def _anadir_jabon(self):
        print(f'Anadiendo jabon')

    def _lavar(self):
        print(f'Lavando lo ropa')

    def _centrifugar(self):
        print(f'Centrifugando ropa')

if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar()
