
import pygame
import pygame_menu
from images_path import Images_path

from play import Game

pygame.init()

surface = pygame.display.set_mode((600, 650))

font = pygame.font.SysFont('Courier New', 25)
font_rb = pygame.font.SysFont('Courier New', 15)


def name_pet():
    game = Game(surface, pygame)

    menu = pygame_menu.Menu('Nome do tamagotchi', 600, 400,
                           theme=pygame_menu.themes.THEME_BLUE)
    menu.add.text_input('Nome: ', maxchar=10, input_underline='_', onreturn=game.play)
    menu.add.button('Voltar', main)
    menu.mainloop(surface)

def main():
    menu = pygame_menu.Menu('Tamagotchi', 600, 400,
                           theme=pygame_menu.themes.THEME_BLUE)

    menu.add.button('Iniciar', name_pet)
    menu.add.button('Sair', pygame_menu.events.EXIT)

    menu.mainloop(surface)

main()