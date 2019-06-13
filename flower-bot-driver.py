

# Circumference in cm
circum = 17.954

# Movement in cm
def move_y(dist):
    rot = dist / circum
    time = rot / vel
    dynaY1(time, -vel)
    dynaY2(time, vel)

def move_x(dist):
    rot = dist / circum
    time = rot / vel
    dynaX1(time, vel)
    dynaX2(time, -vel)

def setAngle(angle):
    self.angle = angle
    
def setShift(shift):
    self.shift = shift

def getAngle():
    return angle

def getShift():
    return shift

def angleCorr():
    
def shiftCorr():
    

move_y(10)
