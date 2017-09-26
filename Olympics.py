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
yellowDiamond = PolygonAsset([(0,0), (-75,150), (0,300), (75,150)], blackOutline, yellow)
text = TextAsset('Max',fill=blue,style='bold 40pt Times')

Sprite(yellowDiamond,(350,100))
Sprite(text,(300,200))


App().run()

