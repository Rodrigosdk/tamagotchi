import os
import time
import platform
from tamagotchi.pet import Pet
from tamagotchi.attributes import Attributes

print("""
1- iniciar
2- sair
""")

option = int(input(">>>"))

def clear_termianal():
    '''
    Vai verificar qual o tipo de sistem operacional e
    executar o comando de limpar tela.
    '''
    if platform.system() == 'Linux':
        os.system('clear')

    elif platform.system() == 'Windows':
        os.system('cls')

if option == 1:
    tamagotchi_name = input('Nome do tamagotchi: ')
    
    #instância de propriedade
    tamagotchi = Pet(tamagotchi_name)
    tamagotchi_attributes = Attributes(tamagotchi)

    # O tempo é formado por segundos * minutos * horas * dias
    TIME_EAT = 60*60*3
    TIME_SLEEP = 60*60*15
    TIME_RELOAD = 60*10
    TIME_AGE = 60*60*24

    #Contador de tempo percorido
    time_count_eat = 0
    time_count_age = 0 
    time_count_sleep = 0

    while tamagotchi.get_age() != 70:
        #Limpar a tela
        clear_termianal()
        
        #Mostar status
        tamagotchi_attributes.status()

        #Tempo para atualizar informções
        time.sleep(TIME_RELOAD)

        # Mudar valores dos status do tamagotchi
        tamagotchi.set_hungry(tamagotchi.get_hungry() - 1)
        tamagotchi.set_power(tamagotchi.get_power() - 0.5)

        # Verificar tempo gasto sem comer para se alimentar
        if time_count_eat >= TIME_EAT:
            tamagotchi_attributes.eat()
            time_count_eat = -TIME_RELOAD

        # Verificar tempo acordado para poder dormir
        if time_count_sleep >= TIME_SLEEP:
            tamagotchi_attributes.sleep()
            time_count_sleep = -TIME_RELOAD

        # Verificar tempo percorido para envelhecer
        if time_count_age >= TIME_AGE:
            age = tamagotchi_attributes.older(10)
            time_count_age = -TIME_RELOAD    
        
        if tamagotchi.get_hungry() == 0:
            break

        if tamagotchi.get_power() == 0:
            break

        #adição de tempo percorido
        time_count_eat = time_count_eat + TIME_RELOAD
        time_count_sleep = time_count_sleep + TIME_RELOAD
        time_count_age = time_count_age + TIME_RELOAD 
    
    print('Game over')
    
    if option == 2:
        exit()