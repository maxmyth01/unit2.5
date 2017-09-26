#Max Low
#9-26-17
#warmup5.py -- yellow dimond with name inside

from ggame import *

blue = Color(0x0000FF,1)
black = Color(0x000000,1)
yellow =Color(0xFFFF00,1)

blackOutline = LineStyle(5,black) # (pixels,colors)
yellowDiamond = PolygonAsset([(0,0), (-150,300), (0,600), (150,300)], blackOutline, yellow)
text = TextAsset('Max',fill=blue,style='bold 40pt Times')

Sprite(yellowDiamond,(300,200))
Sprite(text,(300,200))


App().run()
