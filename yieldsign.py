#Max Low
#9-26-17
#yieldsign.py -- yellow and black yield sign

from ggame import *

black = Color(0x000000,1)
yellow =Color(0xFFFF00,1)

blackOutline = LineStyle(5,black) # (pixels,colors)
yellowTriangle = PolygonAsset([(0,0), (300,0), (150,212)], blackOutline, yellow)
text = TextAsset('Yield',fill=black,style='bold 40pt Times')

Sprite(yellowTriangle,(350,100))
Sprite(text,(430,100))


App().run()
