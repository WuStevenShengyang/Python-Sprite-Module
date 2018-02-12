Python Sprite module (Develop with pygame)

#####Creat sprite object: 
sprite_name=sprite.Sprite(file_location,x_position,y_position,x_width,y_width,colomn,roll) #The last four parameters are optional, they are only used for sprite sheet (You don't have to enter them all the time, they are set ).

#####Change x & y (Variables):
sprite_name.x=#, sprite_name.y=#.

#####Change image (Class method):
sprite_name.image(new_file_location)
\\After this function was called, the sprite_name now has the image of 'new_file_location'

#####Change size (Class method):
sprite_name.scale(x_width,y_width)
\\The size sets to x_width*y_width

#####Rendering (Class method):
sprite_name.draw()
\\Draw the sprite on the screen with (x,y) as the position and the size of (x_width*y_width)

#####Flip image(Class method):
sprite.flip(x_flip,y_flip)
\\Both x_flip and y_flip are Boolean values. If 'x_flip==True', flips horizontally; If 'y_flip==True', flips vertically. 


##########SPRITE SHEET PART (Skip if you have no idea about what is a sprite sheet)#########
Last four parameters when creating a sprite object represents:
x_width:Each single picture's x width
y_width:Each single picture's y width

colomn: Numbers of single pictures horizontally
roll: Numbers of single pictures vertically.

\\Basically, you are entering a sprite sheet with (colomn*roll) of pictures and each picture has the size of (x_width*y_width).

#####Draw each frame
sprite_name.draw_sheet()

#####Update to next frame
sprite_name.update()


