# Write the necessary code calculate the volume and surface area
# of a cylinder with a radius of 3.14 and a height of 5.
# Print out the result.
import math
math.pi

def calcCylinderVolume(radius = 3.14, height = 5):
    return math.pi * radius ** 2 * height

def calcCylinderSurfaceArea(radius = 3.14, height = 5):
    side = 2 * math.pi * radius * height
    topbottom = 2 * math.pi * (radius ** 2)

    return(side + topbottom)

calcCylinderVolume()
calcCylinderSurfaceArea()
