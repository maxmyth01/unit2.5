#Max Low
#9-26-17
#olympics.py -- print olympic rings using colored and white circles

from ggame import *

blue = Color(0x0000FF,1)
yellow =Color(0xFFFF00,1)
black = Color(0x000000,1)
green = Color(0x00FF00,1)
red = Color(0xFF0000,1)
white = Color(0x000000,0)

blueOutline = LineStyle(5,blue) # (pixels,colors)
yellowOutline = LineStyle(5,yellow) # (pixels,colors)
blackOutline = LineStyle(5,black) # (pixels,colors)
greenOutline = LineStyle(5,green) # (pixels,colors)
redOutline = LineStyle(5,red) # (pixels,colors)
blueCircle = CircleAsset(50,blueOutline,white) # radius, linestyle,color
yellowCircle = CircleAsset(50,yellowOutline,white) # radius, linestyle,color
blackCircle = CircleAsset(50,blackOutline,white) # radius, linestyle,color
greenCircle = CircleAsset(50,greenOutline,white) # radius, linestyle,color
redCircle = CircleAsset(50,redOutline,white) # radius, linestyle,color

Sprite(blueCircle,(50,50))
Sprite(yellowCircle,(50,50))
Sprite(blackCircle,(50,50))
Sprite(greenCircle,(50,50))
Sprite(redCircle,(50,50))


App().run()

