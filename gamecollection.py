import pygame as p
from pygame.locals import *

#_______________________________________FUNCTIONS__________________________________
def load_image(src, size, x, y):
    image = p.image.load(src).convert()
    image = p.transform.scale(image, size)
    rect = image.get_rect(center=(x, y))

    transparent = image.get_at((0, 0))
    #image.set_colorkey(transparent)

    return image, rect


#_______________________________________VARIABLES__________________________________
screen_size = 1000, 600
game_is_running = True



#WINDOW
p.init()
window = p.display.set_mode(screen_size)
p.display.set_caption("Game Hub")

#IMAGES
connect_image = load_image("connect4.jpg", (150, 150), 100, 100)


#GAME LOOP
while game_is_running:
    for event in p.event.get():
        if event.type == QUIT:
            game_is_running = False
            p.quit

    window.blit(connect_image[0], connect_image[1])
    p.display.update()