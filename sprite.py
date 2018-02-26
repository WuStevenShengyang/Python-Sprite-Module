import pygame
pygame.init()

class Sprite:
    
    #Constructor (Entering file location, x position, y position, screen surface)
    def __init__(self,img,x_position,y_position,screen,x_spam=0,y_spam=0):

        self.__img=img
        self.__x_position=x_position
        self.__y_position=y_position
        
        self.__sprite=pygame.image.load(self.__img)
        self.__width=pygame.Surface.get_width(self.__sprite)
        self.__height=pygame.Surface.get_height(self.__sprite)
        
        self.__screen=screen

        self.__animation_rate=30
        
        
        #Set Rect parameters to 0 by default
        if (x_spam == 0 ) or (y_spam == 0):
            self.__x_spam=0
            self.__y_spam=0
            self.__x_width=0
            self.__y_width=0
        else:
            self.__x_spam=x_spam
            self.__y_spam=y_spam
            self.__x_width=self.__width/self.__x_spam
            self.__y_width=self.__height/self.__y_spam
              
        self.__x_num=0
        self.__y_num=0
        self.__total_scale=1
          
    #Flip sprite, Enter True on x to flip horizontally; Enter True on y to flip vertically
    def flip(self,x_flip,y_flip):
        if x_flip:
            self.__sprite=pygame.transform.flip(self.__sprite,True,False)
        elif y_flip:
            self.__sprite=pygame.transform.flip(self.__sprite,False,True)
        else:
            self.__sprite=pygame.transform.flip(self.__sprite,True,True)
       
    #Draw function, draw sprite using blit function
    def draw(self):
        self.__screen.blit(self.__sprite,(self.__x_position,self.__y_position))
                
    #Change image function, enter new image location
    def image(self,image):
        self.__sprite=pygame.image.load(image)

    #Change scale of the sprite
    @property
    def scale(self):
        return self.__total_scale
    @scale.setter
    def scale(self,new_scale):
        if self.__total_scale!=new_scale:
            self.__total_scale=new_scale
            self.__width*=self.__total_scale
            self.__height*=self.__total_scale

            self.__sprite=pygame.transform.scale(self.__sprite,(int(self.__width),int(self.__height)))

            self.__x_width=self.__width/self.__x_spam
            self.__y_width=self.__height/self.__y_spam
        
    #Change x_position
    @property
    def x(self):
        return self.__x_position
    @x.setter
    def x(self,new_x):
        self.__x_position=new_x

    #Change y_position
    @property
    def y(self):
        return self.__y_position
    @y.setter
    def y(self,new_y):
        self.__y_position=new_y

    #Change animation rate
    @property
    def rate(self):
        return self.__animation_rate
    @rate.setter
    def rate(self,new_rate):
        self.__animation_rate=new_rate
        
    #Draw sprite sheet
    def draw_sheet(self):
        self.__screen.blit(self.__sprite,(self.__x_position,self.__y_position),(self.__x_num*self.__x_width,self.__y_num*self.__y_width,self.__x_width,self.__y_width))
                
    #Update position
    def update(self):
        if self.__animation_rate!=0:
            delay=1/self.__animation_rate
            pygame.time.wait(int(delay*1000))
            
            if self.__x_num<self.__x_spam-1:
                self.__x_num+=1

            else:
                self.__x_num=0
                if self.__y_num<self.__y_spam-1:
                    self.__y_num+=1
                else:
                    self.__y_num=0
              
                



