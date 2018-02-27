#Note: All the variables in this class sets to public except few particular ones.

import pygame
pygame.init()

class Sprite:
    
    #Constructor (Entering file location, x position, y position, screen surface)
    def __init__(self,img,x,y,screen,x_spam=0,y_spam=0):

        self.img=img
        self.x=x
        self.y=y
        
        self.sprite=pygame.image.load(self.img)
        self.width=pygame.Surface.get_width(self.sprite)
        self.height=pygame.Surface.get_height(self.sprite)
        
        self.__screen=screen

        self.animation_rate=30
        
        
        #Set Rect parameters to 0 by default
        if (x_spam == 0) or (y_spam == 0):
            self.x_spam=0
            self.y_spam=0
            self.x_width=0
            self.y_width=0
        else:
            self.x_spam=x_spam
            self.y_spam=y_spam
            self.x_width=self.width/self.x_spam
            self.y_width=self.height/self.y_spam
              
        self.x_num=0
        self.y_num=0
        
        self.__total_scale=1
          
    #Flip sprite, Enter True on x to flip horizontally; Enter True on y to flip vertically
    def flip(self,x_flip,y_flip):
        if x_flip:
            self.sprite=pygame.transform.flip(self.sprite,True,False)
        elif y_flip:
            self.sprite=pygame.transform.flip(self.sprite,False,True)
        else:
            self.sprite=pygame.transform.flip(self.sprite,True,True)

    #Draw function, draw sprite using blit function
    def draw(self):
        self.__screen.blit(self.sprite,(self.x,self.y))
                
    #Change image function, enter new image location
    def image(self,image):
        self.sprite=pygame.image.load(image)

    #Change scale of the sprite
    @property
    def scale(self):
        return self.total_scale
    @scale.setter
    def scale(self,new_scale):
        if self.total_scale!=new_scale:
            self.total_scale=new_scale
            self.width*=self.total_scale
            self.height*=self.total_scale

            self.sprite=pygame.transform.scale(self.sprite,(int(self.width),int(self.height)))

            self.x_width=self.width/self.x_spam
            self.y_width=self.height/self.y_spam
        
        
    #Draw sprite sheet
    def draw_sheet(self):
        self.__screen.blit(self.sprite,(self.x_,self.y),(self.x_num*self.x_width,self.y_num*self.y_width,self.x_width,self.y_width))
                
    #Update position
    def update(self):
        if self.animation_rate!=0:
            delay=1/self.animation_rate
            pygame.time.wait(int(delay*1000))
            
            if self.x_num<self.x_spam-1:
                self.x_num+=1

            else:
                self.x_num=0
                if self.y_num<self.y_spam-1:
                    self.y_num+=1
                else:
                    self.y_num=0
              
                



