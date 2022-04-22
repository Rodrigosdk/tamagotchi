from tamagotchi import pet

class Attributes:
    def __init__(self, pet: pet):
        self.pet = pet

    def eat(self):
        '''
        Esse componente  vai fazer com que seja 
        possivel modifcar o valor da fome. 
        '''

        print("Estou com fome")
        ask_user = input('alimentar?')

        if ask_user == 'sim':
            self.pet.set_hungry(100)

    def sleep(self):
        '''
        Esse componente  vai fazer com que seja 
        possivel recaregar o valor da energia.

        vai levar 20 segundos para cada ponto da enegia
        ser restaurado vai para quando o valor da energia
        for de 100.
        '''
        print("Estou com sono")
        ask_user = input("dormir? ")

        if ask_user == 'sim':
            while self.pet.get_power() != 100:
                self.pet.set_power(100)


    def older(self, age):
        '''
        Esse componente  vai fazer com que seja 
        somado a idade colocada com a idade atual. 
        '''
        return self.pet.set_age(self.pet.get_age() + age)

    def status(self):
        '''
        vai printar na tela as informações do
        tamagotchi.
        '''
        print(
            f'''
    Nome: {self.pet.get_name()}
    Fome: {self.pet.get_hungry()}
    Idade: {self.pet.get_age()}
    Energia: {self.pet.get_power()}
    ''')
