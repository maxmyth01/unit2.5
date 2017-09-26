#Max Low
#9-26-17
#warmup5.py -- yellow dimond with name inside

from ggame import *

blue = Color(0x0000FF,1)
black = Color(0x000000,1)
yellow =Color(0xFFFF00,1)

blackOutline = LineStyle(5,black) # (pixels,colors)
yellowDiamond = PolygonAsset([(0,0), (-75,150), (0,300), (75,150)], blackOutline, yellow)
text = TextAsset('Max',fill=blue,style='bold 40pt Times')

Sprite(yellowDiamond,(350,100))
Sprite(text,(300,200))


App().run()
