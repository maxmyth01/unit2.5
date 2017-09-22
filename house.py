#Max Low
#9-20-17
#house.py -- make a house looking house

from ggame import *

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)

blackOutline = LineStyle(5,black)
redRectangle = RectangleAsset(200,100,blackOutline,red)
blackTriangle = PolygonAsset([(0,0), (200,0), (100,-75)], blackOutline, black)
blueWindow = RectangleAsset(30,30,blackOutline,blue)
blackDoor = RectangleAsset(30,75,blackOutline, black)

Sprite(redRectangle,(75,100))
Sprite(blackTriangle,(75,100))
Sprite(blueWindow,(200,125))
Sprite(blackDoor,(125,125))


App().run()
