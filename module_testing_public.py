import sprite_public
import pygame
pygame.init()

w=pygame.display.set_mode((1000,300))
w.fill((255,255,255))

#256*512
game=True



explode=sprite_public.Sprite('C:/Users/s-wus/Desktop/man.jpg',0,0,w,7,3)
sp=pygame.image.load('C:/Users/s-wus/Desktop/runningcat.png')
c=pygame.time.Clock()

explode.animation_rate=30

x=1

c=pygame.time.Clock()

while game:
    for event in pygame.event.get():
          if event.type==pygame.QUIT:
                game=False
          if event.type==pygame.MOUSEBUTTONDOWN:
                explode.scale=0.5
            
           
                           
    explode.draw_sheet()
 
    explode.update()
    
    pygame.display.flip()
    #print(explode.x)
    w.fill((255,255,255))
    c.tick(30)

