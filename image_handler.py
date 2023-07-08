import os, sys, pygame, config

pygame.init()


def get_image(image_name:str) -> pygame.Surface:
    return pygame.image.load(os.path.join('assets', image_name))

def get_icon_image(image_name:str) -> pygame.Surface:
    icon_size = int(config.get_value('icon_size'))
    return resize_image(get_image(image_name), (icon_size, icon_size))

def resize_image(image, size = (100, 100)):
    return pygame.transform.scale(image, size)