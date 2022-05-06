from pygame import Surface
import pygame
import pygame_menu
from images_path import Images_path
from tamagotchi.pet import Pet
from tamagotchi.attributes import Attributes
from tamagotchi.time import Time

# O tempo é formado por segundos * minutos * horas
TIME_EAT = 60*60*3
TIME_SLEEP = 60*60*15
TIME_RELOAD = 60*10
TIME_AGE = 60*60*24

class Game():
    def __init__(self, surface:Surface, pygames:pygame):
        self.name = 'algo'
        self.surface = surface
        self.pygames = pygames
        self.tamagotchi = Pet(self.name)

    def play(self, name):
        self.tamagotchi.name = name
        self.pygames.time.wait(1000)

        menu = pygame_menu.Menu(name, 600, 650,
                               theme=pygame_menu.themes.THEME_BLUE)

        image_path = Images_path()
        
        menu.add.label(f'fome: {self.tamagotchi.hungry - 1 }')
        menu.add.label(f'vida: {self.tamagotchi.life}' )
        menu.add.label(f'idade: {self.tamagotchi.age}' )

        menu.add.image(image_path.acordar, angle=0, scale=(0.70, 0.70))
        
        menu.add.button('Alimentar')
        menu.add.button('Dormir')
        menu.add.button('Exercitar')

        menu.mainloop(self.surface)


    def time(self, tamagotchi):
        #instância de propriedade
        tamagotchi_attributes = Attributes(tamagotchi)
        tamagotchi_time = Time(tamagotchi)
        
        while True:
        #Contador de tempo percorido
            time_count_eat = 0
            time_count_age = 0 
            time_count_sleep = 0
            
            tamagotchi_time.denigrate_attribut()
            #Mostar status
            print(tamagotchi_attributes.status())

            #Tempo para atualizar informções
            tamagotchi_time.sleep(TIME_RELOAD)

            # Verificar tempo gasto sem comer para se alimentar
            if time_count_eat >= TIME_EAT:
                ask_user = input('sim')
                tamagotchi_attributes.eat(ask_user)
                time_count_eat = -TIME_RELOAD

            # Verificar tempo acordado para poder dormir
            if time_count_sleep >= TIME_SLEEP:
                tamagotchi_attributes.sleep('sim')
                time_count_sleep = -TIME_RELOAD

            # Verificar tempo percorido para envelhecer
            if time_count_age >= TIME_AGE:
                tamagotchi_attributes.older(10)
                time_count_age = -TIME_RELOAD

            # Verificar se a vida é 0 caso sim ira morrer
            if tamagotchi.life == 0:
                break

            #adição de tempo percorido
            time_count_eat = time_count_eat + TIME_RELOAD
            time_count_sleep = time_count_sleep + TIME_RELOAD
            time_count_age = time_count_age + TIME_RELOAD 

        print('Game over')