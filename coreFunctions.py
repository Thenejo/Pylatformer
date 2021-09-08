import math
def angle_to(pos1,pos2):
    return math.atan2(pos2[1] - pos1[1], pos2[0] - pos1[0])

def distanceBetweem(pos1,pos2):
    return math.sqrt(math.pow(abs(pos1.x-pos2.x), 2)+math.pow(abs(pos1.y-pos2.y), 2))

def sign(num):
    if num>0:
        return 1
    elif num<0:
        return -1
    return 0

def lerp(a,b,t):
    return a + t * (b - a)
