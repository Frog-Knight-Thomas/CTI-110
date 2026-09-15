#Michael Baker
#9/14/26
#Final Project
#This page will direct you to the different games using buttons and will allow you to access the different leaderboards

import pygame
import Pong_Game


pygame.init()

Window = pygame.display.set_mode((500, 400))
Background = pygame.image.load("Main_Screen.png").convert_alpha()
Background_Rect = Background.get_rect()
Background_Rect.topleft = (1,1)
Window.blit(Background, Background_Rect)
font = pygame.font.Font('freesansbold.ttf', 40)

class Button:
    def __init__(self, text, x, y, able):
        self.text = text
        self.x = x
        self.y = y
        self.able = able
        self.draw()

    def draw(self):
        butt_text = font.render(self.text, True, 'white')
        butt_rect = pygame.rect.Rect((self.x, self.y),(200, 100))
        pygame.draw.rect(Window , 'white', butt_rect, 5, 5)
        Window.blit(butt_text, (self.x+10 , self.y+30))

    def c_click(self):
        moose = pygame.mouse.get_pos()
        left = pygame.mouse.get_pressed()[0]
        butt_rect = pygame.rect.Rect((self.x, self.y),(200, 100))
        if left and butt_rect.collidepoint(moose) and self.able:
            return True
        else:
            return False
       
Pong = Button('TESTING', 40, 10, True)


running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if Pong.c_click():
        Pong_Game.run_logic()

    Window.blit(Background, Background_Rect)
    Pong.draw()
    pygame.display.flip()


