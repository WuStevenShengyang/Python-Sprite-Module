import pygame
pygame.init()

class Sprite(pygame.sprite.Sprite):

    '''

   
        __x_position             -sprite's x
        __y_position             -sprite's y
        
        __width                  -image's width according to rect
        __height                 -image's height according to rect
        
        __sprite                 -loaded sprite
        __img                    -sprite's image
        
        __center_x, __center_y         -center x and y of the sprite
        __center                 -center coordinate (return a tuple)

        __scale                  -size


        #Sprite Animation (Sprite Sheet)
        
            __animation_rate         -animate how many frames per second
            


    '''

    def __init__(self,img,x_position,y_position):

        pygame.sprite.Sprite.__init__(self)
        
        self.__sprite_list=[]
        self.__original_sprite_list=[]
        
        self.__img=img
        self.__is_sprite_sheet=True

        #Try if image is a ImageSheet object, if not, load the image if yes, create a new list.
        try:
            self.__img.test=False
        except Exception as e:
            self.__is_sprite_sheet=False

            
        if self.__is_sprite_sheet:
            self.__current_sprite=0
            self.__sprite_list=list(self.__img.image_list)
            self.__original_sprite_list=list(self.__img.image_list)
        else:
            self.__sprite_list.append(pygame.image.load(self.__img).convert_alpha())
            self.__original_sprite_list.append(pygame.image.load(self.__img).convert_alpha())

        #Get Rect configuration 
        self.rect=self.__sprite_list[0].get_rect()
        
        self.rect.x=x_position
        self.rect.y=y_position
        
        self.__width=self.rect.width
        self.__height=self.rect.height

        self.__original_width=self.rect.width
        self.__original_height=self.rect.height

        #Get center
        self.__center=self.rect.center
        self.__center_x=self.__center[0]
        self.__center_y=self.__center[1]

        
        self.__total_scale=1.0

        self.__screen=pygame.display.get_surface()
            
        #Set animation rate
        self.__animation_rate=30

        #Set flip
        self.__x_flip=False
        self.__y_flip=False
        self.__flip=False

    #Flip
    @property
    def flip_x(self):
        return self.__x_flip
    @flip_x.setter
    def flip_x(self,x_flip):
        self.__x_flip=x_flip

    @property
    def flip_y(self):
        return self.__y_flip
    @flip_x.setter
    def flip_y(self,y_flip):
        self.__y_flip=y_flip

    #Change image
    def image(self,image):
        self.__is_sprite_sheet=True
        self.__sprite_list=[]
        
        #Try if image is a ImageSheet object, if not, load the image; if yes, create a new list.
        try:
            image.test=False
        except Exception as e:
            self.__is_sprite_sheet=False

            
        if self.__is_sprite_sheet:
            self.__current_sprite=0
            self.__sprite_list=list(image.image_list)
        else:
            self.__sprite_list.append(pygame.image.load(image).convert_alpha())
            
    @property
    def scale(self):
        return self.__total_scale
    @scale.setter
    def scale(self,new_scale):
        if self.__total_scale!=new_scale:
            self.__total_scale=new_scale
            
            self.rect.width=self.__original_width*self.__total_scale
            self.rect.height=self.__original_height*self.__total_scale
            #Iterate through the sprite list to change the scale
            for sprite in range(len(self.__sprite_list)):
                self.__sprite_list[sprite]=pygame.transform.scale(self.__original_sprite_list[sprite],(self.rect.width,self.rect.height))
                
            
                       
    @property
    def x(self):
        return self.rect.x
    @x.setter
    def x(self,new_x):
        self.rect.x=new_x

    @property
    def y(self):
        return self.rect.y
    @y.setter
    def y(self,new_y):
        self.rect.y=new_y

    @property
    def center_x(self):
        return self.__center_x
    @center_x.setter
    def center_x(self,new_center_x):
        self.__center_x=new_center_x
        self.rect.center=(self.__center_x,self.__center_y)

    @property
    def center(self):
        return self.__center
    @center.setter
    def center(self,new_center):
        self.__center=new_center
        self.rect.center=self.__center
              
    @property
    def center_y(self):
        return self.__center_y
    @center_y.setter
    def center_y(self,new_center_y):
        self.__center_y=new_center_y
        self.rect.center=(self.__center_x,self.__center_y)

    @property
    def animation_rate(self):
        #Set animation rate based on frames per second 
        return self.__animation_rate
    
    @animation_rate.setter
    def animation_rate(self,new_rate):
        self.__animation_rate=new_rate

    def draw(self):
        if len(self.__sprite_list)==1:
            self.__current_image=self.__sprite_list[0]
            
            self.__current_image=pygame.transform.flip(self.__current_image,self.__x_flip,self.__y_flip)
            self.__screen.blit(self.__current_image,(self.rect.x,self.rect.y))    
        else:
            self.__current_image=self.__sprite_list[self.__current_sprite]
            
            self.__current_image=pygame.transform.flip(self.__current_image,self.__x_flip,self.__y_flip)
            self.__screen.blit(self.__current_image,(self.rect.x,self.rect.y))
    
    def update(self):
        if self.__animation_rate!=0:
                 
            delay=1/self.__animation_rate
            pygame.time.wait(int(delay*1000))
            self.__current_sprite+=1
            
            if self.__current_sprite>=len(self.__sprite_list):
                self.__current_sprite=0
    
              



