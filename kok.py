#Michael Baker

import pygame

pygame.init()

clock = pygame.time.Clock()

Height = 400
Width = 500
Window = pygame.display.set_mode((Width,Height))

Playerimage = pygame.image.load("ship1.png").convert_alpha()
PiSS = pygame.transform.scale_by(Playerimage, 0.15)
player = PiSS.get_rect()
player.y += 345
speed = 3
font = pygame.font.Font('freesansbold.ttf', 40)

OPPimage = pygame.image.load("OPP.png").convert_alpha()
OPPs = pygame.transform.scale_by(OPPimage, 0.075)
Opp = OPPs.get_rect()
Opp.y += 10
Opp.x += 100

shells = []

Enemies = 5
shots = 10
shooting = False
class Button:
    def __init__(joke, text, x, y):
        joke.text = text
        joke.x = x
        joke.y = y
        joke.draw()

    def draw(joke):
        butt_text = font.render(joke.text, True, 'white')
        Window.blit(butt_text, (joke.x+10 , joke.y+30))
        
winner = Button(("WINNER"), 65, 100 )
loser = Button(("LOSER"), 300, 120 )

running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shots -= 1
                shells.append(pygame.Rect(player.x + 15, 375, 10, 10))
                
    keys = pygame.key.get_pressed()


    if keys[pygame.K_RIGHT]:
        player.x += speed
    
    if keys[pygame.K_LEFT]:
        player.x -= speed

    player.left = max(player.left, 0)
    
    player.right = min(player.right, 500)
    
    if Opp.x < player.x or Opp.x < 50:
        Opp.x -= speed - 1
    if Opp.x > player.x or Opp.x > 550:
        Opp.x += speed - 1
    Opp.left = max(Opp.left, 50)
    Opp.right = min(Opp.right, 450)
    
    
    if Enemies == 0 or shots == 0:
        if shots == 0:
            loser.draw()
            pygame.display.update()
        elif Enemies == 0:
            winner.draw()
            pygame.display.update()
        pygame.time.wait(1000)
        running = False

    Background = (0, 0, 55)
    Window.fill(Background)
    Window.blit(PiSS, player)
    Window.blit(OPPs, Opp)
    for rect in shells:
        pygame.draw.rect(Window, 'white', rect)
    for rect in shells:
        rect.y -= speed
    pygame.display.update()
    pygame.display.flip()
    clock.tick(150)