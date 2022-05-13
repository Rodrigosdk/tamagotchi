import os
import pygame, sys
from button import Button
from tamagotchi.attributes import Attributes
from tamagotchi.pet import Pet
from tamagotchi.time import Time

pygame.init()

SCREEN = pygame.display.set_mode((1280, 520))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")


TIME_RELOAD = 60*10

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)


def play():
    pygame.display.set_caption("Game")

    #instância de propriedade
    tamagotchi = Pet('majin boo')
    tamagotchi_attributes = Attributes(tamagotchi)
    tamagotchi_time = Time(tamagotchi)

    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        name = get_font(15).render(f'Nome: {tamagotchi.name}', True, "White")
        #age = get_font(15).render(f'Idade: {tamagotchi.age}', True, "White")
        hungry = get_font(15).render(f'Fome: {tamagotchi.hungry}', True, "White")
        life = get_font(15).render(f'Vida: {tamagotchi.life}', True, "White")
        power = get_font(15).render(f'Energia: {tamagotchi.power}', True, "White")
        hygiene = get_font(15).render(f'Higiene: {tamagotchi.hygiene}', True, "White")
        force = get_font(15).render(f'Força: {tamagotchi.force}', True, "White")

        name_react = name.get_rect(center=(120, 50))
        #age_react = age.get_rect(center=(65, 100))
        hungry_react = hungry.get_rect(center=(75, 150))
        life_react = life.get_rect(center=(75, 200))
        power_react = power.get_rect(center=(100, 250))
        hygiene_react = hygiene.get_rect(center=(100, 300))
        force_react = force.get_rect(center=(90, 350))

        SCREEN.blit(name, name_react)
        #SCREEN.blit(age, age_react)
        SCREEN.blit(hungry, hungry_react)
        SCREEN.blit(life, life_react)
        SCREEN.blit(power, power_react)
        SCREEN.blit(hygiene, hygiene_react)
        SCREEN.blit(force, force_react)

        # Mudar valores dos status do tamagotchi
        tamagotchi_time.denigrate_attribut()
        
        img = pygame.image.load(os.path.join('assets', 'tamagochi.jpeg'))
        SCREEN.blit(img, (500, 80))

        #Tempo para atualizar informções
        pygame.time.wait(TIME_RELOAD)
        
        play_food = Button(image=None, pos=(1100, 50), 
                            text_input="Alimentar", font=get_font(25), base_color="White", hovering_color="Green")
        play_sleep = Button(image=None, pos=(1100, 120), 
                            text_input="Dormir", font=get_font(25), base_color="White", hovering_color="Green")
        play_exercise = Button(image=None, pos=(1100, 180), 
                            text_input="Exercitar", font=get_font(25), base_color="White", hovering_color="Green")
        play_hygiene = Button(image=None, pos=(1100, 240), 
                            text_input="Tomar banho", font=get_font(25), base_color="White", hovering_color="Green")
        play_back = Button(image=None, pos=(1100, 300), 
                            text_input="BACK", font=get_font(25), base_color="White", hovering_color="Green")


        play_food.changeColor(PLAY_MOUSE_POS)
        play_sleep.changeColor(PLAY_MOUSE_POS)
        play_back.changeColor(PLAY_MOUSE_POS)
        play_exercise.changeColor(PLAY_MOUSE_POS)
        play_hygiene.changeColor(PLAY_MOUSE_POS)

        play_food.update(SCREEN)
        play_sleep.update(SCREEN)
        play_back.update(SCREEN)
        play_hygiene.update(SCREEN)
        play_exercise.update(SCREEN)

        if tamagotchi.life == 0:
            death()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_food.checkForInput(PLAY_MOUSE_POS):
                    tamagotchi_attributes.eat()
                
                if play_sleep.checkForInput(PLAY_MOUSE_POS):
                    tamagotchi_attributes.sleep()

                if play_exercise.checkForInput(PLAY_MOUSE_POS):
                    tamagotchi_attributes.exercise()
                
                if play_hygiene.checkForInput(PLAY_MOUSE_POS):
                    tamagotchi_attributes.shower()
                
                if play_back.checkForInput(PLAY_MOUSE_POS):
                    main_menu()


        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Tamagotchi", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 370), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        

def death():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")


        PLAY_TEXT = get_font(35).render("Que pena seu bixinho morreu! :/", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()
main_menu()