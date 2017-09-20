#Max Low
#9-20-17
#graphicsDemo.py -- into to ggame

from ggame import *

red = Color(0xFF0000,1)

green = Color(0x00FF00,1)

blue = Color(0x0000FF,1)

black = Color(0x000000,1)

blackOutline = LineStyle(5,black) # (pixels,colors)

redRectangle = RectangleAsset(200,100,blackOutline,red) # (width, height, outline, fill)

blueCircle = CircleAsset(50,blackOutline,blue)

greenEllipse = EllipseAsset(100,50,blackOutline,green)

Sprite(redRectangle)

Sprite(blueCircle,(50,50))

Sprite(greenEllipse,(200,400))


App().run()
