#Max Low
#9-2-17
#germany.py -- make a german flag

from ggame import *

red = Color(0xFF0000,1)
yellow = Color(0xFFFF00,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black) # (pixels,colors)
redRectangle = RectangleAsset(200,100,blackOutline,red) # (width, height, outline, fill)
blackRectangle = RectangleAsset(200,33,blackOutline,black)
yellowRectangle = RectangleAsset(200,33,blackOutline,yellow)

Sprite(redRectangle)
Sprite(blackRectangle,(0,0))
Sprite(yellowRectangle,(0,66))


App().run()

