#Michael Baker


import pygame
import random
pygame.init()

clock = pygame.time.Clock()
Height = 400
Width = 500
Window = pygame.display.set_mode((Width, Height))
Background = pygame.image.load("Pong_Background.png").convert_alpha()
Background_Scaled = pygame.transform.scale_by(Background, 0.32)
Background_Rect = Background_Scaled.get_rect()
Background_Rect.topleft = (-10,0)
Window.blit(Background_Scaled, Background_Rect)
font = pygame.font.Font('freesansbold.ttf', 40)
speed = 2
OPPspeed = 1
player = pygame.Rect(Width -490, Height/2 - 50, 10, 100)
OPP = pygame.Rect(Width - 20, Height/2 - 50, 10, 100)
TOP = pygame.Rect(0, 0 , 1, Width)

Ball = pygame.Rect(Width/2 - 10, Height/2 -10, 20, 20)


def run_logic():
    running = True
    X_speed, Y_speed = 2, 2
    while running == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            keys = pygame.key.get_pressed()

            if keys[pygame.K_UP]:
                player.y -= float( speed)
            if keys[pygame.K_DOWN]:
                player.y += float( speed)

            if Ball.y > OPP.y:
                OPP.y += OPPspeed
            if Ball.y < OPP.y:
                OPP.y -= OPPspeed
            score , Oppscore = 0,0
            player.top = max(player.top, 20)
            player.bottom = min(player.bottom, Height-30 )
            OPP.top = max(OPP.top, 20)
            OPP.bottom = min(OPP.bottom, Height-30 )
            
            if Ball.y >=Height - 45:
                 Y_speed = -2
            if Ball.y <= 45:
               Y_speed = 2
            if Ball.x >= Width:
                score += 2
                Ball.center = (Width/2 - 10, Height/2 -10)
                X_speed, Y_speed = random.choice([2, -2]), random.choice([2, -2])

            if Ball.colliderect(player) and X_speed < 0:
                X_speed = 2

            if Ball.colliderect(OPP) and X_speed > 0:
               X_speed = -2

            if Ball.x <= 0:
                Oppscore += 1
                Ball.center = (Width/2 - 10, Height/2 -10)
                X_speed, Y_speed = random.choice([2, -2]), random.choice([2, -2])

            Ball.x += X_speed
            Ball.y +=  Y_speed

            Window.blit(Background_Scaled, Background_Rect)
            pygame.draw.rect(Window, "white", player)
            pygame.draw.rect(Window, "white", OPP)
            pygame.draw.circle(Window,'white', Ball.center, 10)
            clock.tick(150)
            pygame.display.update()
            pygame.display.flip()
