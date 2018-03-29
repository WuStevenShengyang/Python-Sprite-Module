import pygame
pygame.init()


class ImageSheet:

    '''


        sheet                    -Sprite sheet
        colomn, row              -rows and colomn of a sprite sheet
        
        __frame_height,
        __frame_width            -height per frame & width per frame

        image_list               -list of seperate frames

        

    '''
    
    def __init__(self,sheet,colomn,row):
        self.sheet=sheet
        self.colomn=colomn
        self.row=row
        self.test=False

        #Convert sprite sheet and get width&height
        self.__image=pygame.image.load(sheet).convert_alpha()
        self.__width=self.__image.get_rect().width
        self.__height=self.__image.get_rect().height

        self.__frame_height=self.__height/self.row
        self.__frame_width=self.__width/self.colomn
        
        self.image_list=[]
        
        for i in range(self.row):
            y=i*self.__frame_height
            for j in range(self.colomn):
                x=j*self.__frame_width
                
                #####
                self.__image.set_clip(pygame.Rect(x,y,self.__frame_width,self.__frame_height))
                self.image_list.append(self.__image.subsurface(self.__image.get_clip()))
                #####




                
