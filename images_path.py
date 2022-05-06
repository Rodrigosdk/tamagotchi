from email.mime import image
import os


class Images_path:
    def __init__(self) -> None:
       self.acordar = os.path.join('images', 'acordado.jpg')
       self.dormir = os.path.join('image', 'dormindo.png')
       self.fome = os.path.join('image', 'fome.jpg')