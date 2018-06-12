Python-Sprite-Module


# How to Import (Make sure 'sprite' is in the same folder as your python script)

in the .py:
```
from sprite import *
```

# How to Use

Create a sprite object
```
name = sprite.Sprite(image, xpos, ypos)
```

Position
```
sprite.x = new_x
sprite.y = new_y

sprite.center_x = new_center_x
sprite.center_y = new_center_y
sprite.center = center
```

Size (Based on percentage)
```
sprite.scale = scale 
```

Rotation
```
sprite.rotation = angle (in degrees)
```
(Rotation looks weird with some unintended offsets with the collide box. I don't recommend using this function unless necessary)

Flip
```
sprite.flip_x = True/ False
sprite.flip_y = True/ False
```

Change Image
```
sprite.image = new_image
```

Draw
```
sprite.draw()
```

### Imagesheet (For Animiation)
Create Imagesheet Object
```
name = Imagesheet.Imagesheet(img, row, col)
```

Import Imagesheet Object into Sprite class
```
name = sprite.Sprite(Imagesheet, xpos, ypos)
```

Animate
```
name.draw()
name.update()
```

Animation Rate (Based on frames per second)
```
name.animation_rate = new_animation_rate
```
