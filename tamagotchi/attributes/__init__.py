from typing import Type
from tamagotchi.interfaces.pet import PetInterface

class Attributes:
    def __init__(self, pet: Type[PetInterface]):
        self.pet = pet

    def eat(self):
        '''
        Esse componente  vai fazer com que seja 
        possivel modifcar o valor da fome. 
        '''
        self.pet.hungry = 100

    def sleep(self):
        '''
        Esse componente  vai fazer com que seja 
        possivel recaregar o valor da energia.
        '''
        if self.pet.power != 100:
                self.pet.power = 100
            
    def older(self, age):
        '''
        Esse componente  vai fazer com que seja 
        somado a idade colocada com a idade atual. 
        '''
        self.pet.age += age
        return self.pet.age

    def shower(self):
        self.pet.hygiene = 100
        return self.pet.hygiene
    
    def exercise(self):
        self.pet.force += 1
        self.pet.hygiene -= 10
        self.pet.power -= 3
        return self.pet.force

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