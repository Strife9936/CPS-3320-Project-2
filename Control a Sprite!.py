import sys, pygame
pygame.init()

#Variable for size of screen
SCREEN = pygame.display.set_mode((1280,720))

#Music player function in pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('gamemusic.mp3')
pygame.mixer.music.play()

#Variables/characteristics for character. Sets his height, width, and speed
x = 50
y = 50
width = 40
height = 60
vel = 50


#Set of functions that allows the program to know which keys are being pressed and how they should move the character
run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y-= vel
    if keys[pygame.K_DOWN]:
        y+= vel

#Fills/Updates the screen with the actual image we want to show
    SCREEN.fill((0,0,0))
    pygame.draw.rect(SCREEN,(0,250,0),(x,y,width,height))
    pygame.display.update()

#Properly ends program when user exits
pygame.quit()
