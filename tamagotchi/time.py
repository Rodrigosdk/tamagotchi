import os
import platform
import time
from typing import Type
from tamagotchi.interfaces.pet import PetInterface

from tamagotchi.pet import Pet


class Time():
    def __init__(self, pet: Type[PetInterface]) -> None:
        self.pet = pet

    def sleep(self, time_reload):
        '''
        vai fazer o programa pausar
        pelo tempo informado ao
        time_reload.

        time_reload: segundo
        '''
        time.sleep(time_reload)
    
    def denigrate_hungry(self):
        '''
        Esse componete vai subitrair 1 caso o valor
        da fome seja maior que 0. Caso contrario ele
        vai subitrair 1 da vida
        '''
        if self.pet.hungry > 0:
            self.pet.hungry -=  1
        else:
            if self.pet.life > 0:
                self.pet.life -= 1

    def denigrate_power(self):
        '''
        Esse componente vai subtrair 0.5 da energia 
        caso o valor da energia seja maior que 0. 
        Caso contrario ele vai subitrair 10 da vida
        '''
        if self.pet.power > 0:
            self.pet.power -=  0.5
        else:
            if self.pet.life > 0:
                self.pet.life -= 10

    def denigrate_hygiene(self):
        if self.pet.hygiene > 0:
            self.pet.hygiene -=  1.5
        else:
            if self.pet.life > 0:
                self.pet.life -= 1

    def denigrate_attribut(self):
        '''
        vai chamar os componente 
        denigrate_hungry e denigrate_power.
        '''
        self.denigrate_hungry()
        self.denigrate_power()
        self.denigrate_hygiene()