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
speed = 3
OPPspeed = 2
player = pygame.Rect(Width -490, Height/2 - 50, 10, 100)
OPP = pygame.Rect(Width - 20, Height/2 - 50, 10, 100)
TOP = pygame.Rect(0, 0 , 1, Width)
font = pygame.font.Font('freesansbold.ttf', 40)

Ball = pygame.Rect(Width/2 - 10, Height/2 -10, 20, 20)

class Button:
    def __init__(joke, text, x, y):
        joke.text = text
        joke.x = x
        joke.y = y
        joke.draw()

    def draw(joke):
        butt_text = font.render(joke.text, True, 'white')
        Window.blit(butt_text, (joke.x+10 , joke.y+30))

def run_logic():
    playing = True
    X_speed, Y_speed = 2, 2
    score , Oppscore = 0 , 0
    text = Button((f"{score}   {Oppscore}"), 200, 10)
    winner = Button(("WINNER"), 65, 100 )
    loser = Button(("LOSER"), 300, 120 )
    
    while playing == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing = False
            keys = pygame.key.get_pressed()

            if keys[pygame.K_UP]:
                player.y -= float( speed)
            if keys[pygame.K_DOWN]:
                player.y += float( speed)
            #GOING DOWN
            if Ball.y > (OPP.y - 10):
                OPP.y += OPPspeed
            #GOING UP
            if Ball.y < (OPP.y + 60):
                OPP.y -= OPPspeed
            player.top = max(player.top, 20)
            player.bottom = min(player.bottom, Height-30 )
            OPP.top = max(OPP.top, 20)
            OPP.bottom = min(OPP.bottom, Height-30 )
            
            if Ball.y >=Height - 45:
                Y_speed = -(speed)
            if Ball.y <= 20:
                Y_speed = (speed)
            if Ball.x >= Width:
                score += 1
                Ball.center = (Width/2 - 10, Height/2 -10)
                X_speed, Y_speed = random.choice([(speed), -(speed)]), random.choice([(speed), -(speed)])

            if Ball.colliderect(player) and X_speed < 0:
                X_speed = (speed)

            if Ball.colliderect(OPP) and X_speed > 0:
                X_speed = -(speed)

            if Ball.x <= 0:
                Oppscore += 1
                Ball.center = (Width/2 - 10, Height/2 -10)
                X_speed, Y_speed = random.choice([2, -2]), random.choice([2, -2])
            
            if score == 9 or Oppscore == 9:
                if score == 9:
                    winner.draw()
                    pygame.display.update()
                else:
                    loser.draw()
                    pygame.display.update()
                pygame.time.wait(1000)
                playing = False

            Ball.x += X_speed
            Ball.y +=  Y_speed

            Window.blit(Background_Scaled, Background_Rect)
            pygame.draw.rect(Window, "white", player)
            pygame.draw.rect(Window, "white", OPP)
            pygame.draw.circle(Window,'white', Ball.center, 10)
            clock.tick(150)
            text.draw()
            text.text = (f"{score}   {Oppscore}")
            pygame.display.update()
            pygame.display.flip()