#Max Low
#9-26-17
#olympics.py -- print olympic rings using colored and white circles

from ggame import *

blue = Color(0x0000FF,1)
yellow =Color(0xFFFF00,1)
black = Color(0x000000,1)
green = Color(0x00FF00,1)
red = Color(0xFF0000,1)

blackOutline = LineStyle(5,black) # (pixels,colors)
blueCircle = CircleAsset(50,blackOutline,blue) # radius, linestyle,color
yellowCircle = CircleAsset(50,blackOutline,yellow) # radius, linestyle,color
blackCircle = CircleAsset(50,blackOutline,black) # radius, linestyle,color
greenCircle = CircleAsset(50,blackOutline,green) # radius, linestyle,color
redCircle = CircleAsset(50,blackOutline,red) # radius, linestyle,color

Sprite(blueCircle,(50,50))
Sprite(yellowCircle,(50,50))
Sprite(blackCircle,(50,50))
Sprite(greenCircle,(50,50))
Sprite(redCircle,(50,50))


App().run()

