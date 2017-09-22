#Max Low
#9-22-17
#name.py -- prints name in middle and choose a backround color

from ggame import *
color = input('Enter a RGB color code')
color = Color(color,1)
black = Color(0x000000,1)

blackOutline = LineStyle(0.5,black)
redRectangle = RectangleAsset(1050,700,blackOutline,color)

Sprite(redRectangle)

App().run()

