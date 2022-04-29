from tamagotchi import pet

class Attributes:
    def __init__(self, pet: pet):
        self.pet = pet

    def eat(self, feed):
        '''
        Esse componente  vai fazer com que seja 
        possivel modifcar o valor da fome. 
        '''
        if feed == 'sim':
            self.pet.hungry = 100

    def sleep(self, sleep):
        '''
        Esse componente  vai fazer com que seja 
        possivel recaregar o valor da energia.
        '''
        if sleep == 'sim':
            if self.pet.power != 100:
                self.pet.power = 100
            
    def older(self, age):
        '''
        Esse componente  vai fazer com que seja 
        somado a idade colocada com a idade atual. 
        '''
        self.pet.age += age
        return self.pet.age

    def status(self):
        '''
        vai retornar informações do
        tamagotchi.
        '''
        return (
            f'''
    Nome: {self.pet.name}
    vida: {self.pet.life}
    Fome: {self.pet.hungry}
    Idade: {self.pet.age}
    Energia: {self.pet.power}
    ''')