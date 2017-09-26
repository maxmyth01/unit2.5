#Max Low
#9-26-17
#graphAPoint.py -- graphs a point between -10,10

from ggame import *

black = Color(0x000000,1)

blackOutline = LineStyle(5,black) # (pixels,colors)
blackLine = LineAsset(50,160,blackOutline) # x endpt, y endpt, linestyle
xaxis = LineAsset(50,160,blackOutline)
yaxis = LineAsset(50,160,blackOutline)

Sprite(xaxis,(50,50))
Sprite(yaxis,(100,100))
Sprite(blackLine,(150,50))



App().run()
