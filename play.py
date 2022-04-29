import os
import platform
from tamagotchi.pet import Pet
from tamagotchi.attributes import Attributes
from tamagotchi.time import Time

def clear_termianal():
        '''
        Vai verificar qual o tipo de sistem operacional e
        executar o comando de limpar tela.
        '''
        if platform.system() == 'Linux':
            os.system('clear')
    
        elif platform.system() == 'Windows':
            os.system('cls')

# O tempo é formado por segundos * minutos * horas
TIME_EAT = 60*60*3
TIME_SLEEP = 60*60*15
TIME_RELOAD = 60*10
TIME_AGE = 60*60*24

def play():
    tamagotchi_name = input('Nome do tamagotchi: ')
    
    #instância de propriedade
    tamagotchi = Pet(tamagotchi_name)
    tamagotchi_attributes = Attributes(tamagotchi)
    tamagotchi_time = Time(tamagotchi)

    #Contador de tempo percorido
    time_count_eat = 0
    time_count_age = 0 
    time_count_sleep = 0

    while tamagotchi.age < 70:
        #Limpar a tela
        clear_termianal()

        # Mudar valores dos status do tamagotchi
        tamagotchi_time.denigrate_attribut()
        
        #Mostar status
        print(tamagotchi_attributes.status())

        #Tempo para atualizar informções
        tamagotchi_time.sleep(TIME_RELOAD)

        # Verificar tempo gasto sem comer para se alimentar
        if time_count_eat >= TIME_EAT:
            ask_user = input(f'Alimentar {tamagotchi_name} (sim ou não): ')
            tamagotchi_attributes.eat(ask_user)
            time_count_eat = -TIME_RELOAD

        # Verificar tempo acordado para poder dormir
        if time_count_sleep >= TIME_SLEEP:
            ask_user = input(f'Dormir {tamagotchi_name} (sim ou não): ')
            tamagotchi_attributes.sleep(ask_user)
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