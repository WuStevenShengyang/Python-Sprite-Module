import pygame
pygame.init()


class ImageSheet:
    def __init__(self,sheet,colomn,row):
        self.sheet=sheet
        self.colomn=colomn
        self.row=row
        self.test=False
        
class Sprite:
    
    #Constructor (Entering file location, x position, y position, screen surface)
    def __init__(self,img,x_position,y_position,screen):
        self.__img=img
        self.__is_sprite_sheet=True
        
        try:
            self.__img.test=False
        except Exception as e:
            self.__is_sprite_sheet=False
            
        self.__x_position=x_position
        self.__y_position=y_position
        
        #Load sprite
        if self.__is_sprite_sheet:
            self.__sprite=pygame.image.load(self.__img.sheet)
        else:
            self.__sprite=pygame.image.load(self.__img)
            
        self.__width=pygame.Surface.get_width(self.__sprite)
        self.__height=pygame.Surface.get_height(self.__sprite)
        
        self.__original_width=pygame.Surface.get_width(self.__sprite)
        self.__original_height=pygame.Surface.get_height(self.__sprite)
        
        self.__screen=screen

        self.__animation_rate=30
        
        #Set Rect parameters to 0 by default
        if not self.__is_sprite_sheet:
            self.__x_spam=0
            self.__y_spam=0
            self.__x_width=0
            self.__y_width=0

            self.__cen_x=self.__x_position+(self.__width/2)
            self.__cen_y=self.__y_position+(self.__height/2)
            
        else:
            self.__x_spam=self.__img.colomn
            self.__y_spam=self.__img.row
            
            self.__x_width=self.__width/self.__x_spam
            self.__y_width=self.__height/self.__y_spam
            
            self.__cen_x=self.__x_position+(self.__x_width/2)
            self.__cen_y=self.__y_position+(self.__y_width/2)
              
        self.__x_num=0
        self.__y_num=0
        self.__total_scale=1
        self.__center=(self.__cen_x,self.__cen_y)
        
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
        if self.__is_sprite_sheet:
            self.__screen.blit(self.__sprite,(self.__x_position,self.__y_position),(self.__x_num*self.__x_width,self.__y_num*self.__y_width,self.__x_width,self.__y_width))
        else:
            self.__screen.blit(self.__sprite,(self.__x_position,self.__y_position))
                
    #Change image function, enter new image location
    def image(self,image):
        self.__sprite=pygame.image.load(image)

##    def rect(self):
##        return pygame.Rect(self.__x_position,self.__y_position,self.__width,self.__height)
    
    #Change scale of the sprite
    @property
    def scale(self):
        return self.__total_scale
    @scale.setter
    def scale(self,new_scale):
        if self.__total_scale!=new_scale:

            self.__total_scale=new_scale
            self.__width=self.__total_scale*self.__original_width
            self.__height=self.__total_scale*self.__original_height
            
            self.__sprite=pygame.transform.scale(self.__sprite,(int(self.__width),int(self.__height)))

            if self.__x_spam!=0 and self.__y_spam!=0:
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

    #Change center_x
    @property
    def center_x(self):
        return self.__cen_x
    @center_x.setter
    def center_x(self,new_center_x):
        self.__cen_x=new_center_x
        if self.__x_spam!=0 and self.__y_spam!=0:
            self.__x_position=self.__cen_x-(self.__x_width/2)
        else:
            self.__x_position=self.__cen_x-(self.__width/2)
    #Get center
    @property
    def center(self):
        return self.__center
    @center.setter
    def center(self,new_center):
        self.__center=new_center
        
        self.__cen_x=new_center[0]
        self.__cen_y=new_center[1]
        
        if self.__x_spam!=0 and self.__y_spam!=0:
            self.__x_position=self.__cen_x-(self.__x_width/2)
        else:
            self.__x_position=self.__cen_x-(self.__width/2)

        if self.__x_spam!=0 and self.__y_spam!=0:
            self.__y_position=self.__cen_y-(self.__y_width/2)
        else:
            self.__y_position=self.__cen_y-(self.__height/2)
            
    #Change center_y
    @property
    def center_y(self):
        return self.__cen_y
    @center_y.setter
    def center_y(self,new_center_y):
        self.__cen_y=new_center_y
        if self.__x_spam!=0 and self.__y_spam!=0:
            self.__y_position=self.__cen_y-(self.__y_width/2)
        else:
            self.__y_position=self.__cen_y-(self.__height/2)

        
    #Change animation rate
    @property
    def animation_rate(self):
        return self.__animation_rate
    @animation_rate.setter
    def animation_rate(self,new_rate):
        self.__animation_rate=new_rate
        
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

              



