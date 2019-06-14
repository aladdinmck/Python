# Boolean for ultrasonic sensor
ultraSonic = false

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

def angleCorr(angle):
    '''
    if angle is less than 90 - dynaX1(time, vel) for angle correction
    and dynaY1(time, -vel) & dynaY2(time, vel) up y-axis for shift correction
    
    if angle is greater than 90 - dynaX2(time, vel) for angle correction
    and dynaY1(time, vel) & dynaY2(time, -vel) down y-axis for shift correction
    '''
    # this still needs some equation that 
    # takes angle as input and outputs time 

    if (angle < 90):
        dynaX1(time,vel)
    if (angle > 90):
        dynaX2(time,vel)
    
def shiftCorr(shift):
    if (shift > 0):
        dynaY1(time,-vel)
        dynaY2(time,vel)
        

def shift_x():

def shift_y():

def angle_dist():

move_y(10)
