#Max Low
#9-22-17
#name.py -- prints name in middle and choose a backround color

from ggame import *

name = input('Enter your Name')
color = input('Enter a RGB color code')
color = Color(color,1)
black = Color(0x000000,1)

blackOutline = LineStyle(0.5,black)
redRectangle = RectangleAsset(1050,700,blackOutline,color)
text = TextAsset(name,fill=black,style='bold 70pt Times')

Sprite(redRectangle)
Sprite(text,(475,200))

App().run()

