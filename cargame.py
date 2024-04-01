import pygame
import time
import random
pygame.init()
clock=pygame.time.Clock()
FPS=30
WIDTH=500
HEIGHT=600
CAR_X=random.choice([25,125,225,325,425])
CAR_Y=random.choice([-2, -50 , -134 , -232, -310 , -430 , -365])
SCORE=0
MYCAR_X=25
MYCAR_Y=500
CARSIZE=50
VEL_X=0
VEL_Y=0
font=pygame.font.Font("freesansbold.ttf",32)
text=font.render(f"{SCORE}",True,"green","blue")
textrect=text.get_rect()
textrect.center=(250,10)
display=pygame.display.set_mode((WIDTH,HEIGHT))
bgcolor=(255,255,255)
display.fill(bgcolor)
pygame.display.flip()

def cars():
    display.blit(text,textrect)
    pygame.display.update()
    for i in range(100,500,100):
        pygame.draw.line(display,"black",(i,0),(i,600),2)
    car=pygame.draw.rect(display,"red",[CAR_X,CAR_Y,CARSIZE,CARSIZE])
    rectangle_sprite = pygame.sprite.Sprite()
    recta=car.get_rect()
    rectangle_sprite.recta = pygame.Rect(10, 10, 20, 20)
    pygame.display.update()
    
    
    pygame.draw.rect(display,"green",[MYCAR_X,MYCAR_Y,CARSIZE,CARSIZE])
    pygame.display.update()
    clock.tick(FPS)
    

   

   

while True:
    
    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
         #setting event for cars
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                VEL_Y= 5
                VEL_X=0
            #setting mouse event for MYCAR
            if event.key == pygame.K_RIGHT:
                MYCAR_X +=100
                pygame.display.update()
                clock.tick(FPS)
            if event.key == pygame.K_LEFT:
                MYCAR_X -=100
                pygame.display.update()
                clock.tick(FPS)
         #checking for collide   
        if CAR_Y+CARSIZE > MYCAR_Y  and CAR_X == MYCAR_X:
            print("yes")   
            
            
        # increament score
        if CAR_Y + CARSIZE > MYCAR_Y:
            SCORE +=1
            print(SCORE)




    CAR_Y=CAR_Y+VEL_Y
    CAR_X=CAR_X+VEL_X
    display.fill(bgcolor)
   
   
    cars()
  
    pygame.display.update()
    
    