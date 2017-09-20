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
blueCircle = CircleAsset(50,blackOutline,blue) # radius, linestyle,color
greenEllipse = EllipseAsset(100,50,blackOutline,green) # major axis, minor axis, linestyle, color
blackLine = LineAsset(50,160,blackOutline) # x endpt, y endpt, linestyle
redTriangle = PolygonAsset([(0,0), (120,180), (60,300), blackOutline, red])


Sprite(redRectangle)
Sprite(blueCircle,(50,50))
Sprite(greenEllipse,(200,400))
sprite(blackLine)
sprite(redTriangle)


App().run()
