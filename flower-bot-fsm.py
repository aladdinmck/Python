import motors as motors
from random import randint
from time import clock 
import time as time

# ======= # 
# Globals #
# ======= #
nplants    = 1
spaces     = 0
Gcount     = 0
Rcount     = 0
up         = False
drop       = False
dropped    = False
horizontal = False
plants     = [0] * 10
pStr     = 'R G G G R R G R G R'

plants     = pStr.split(' ')

# Transition
class Transition(object):
    print('Starting up...')
    def __init__(self, toState):
        self.toState = toState
    def Execute(self):
        print('Transitioning...')

# States
class State(object):
    global nplants
    def __init__(self, FSM):
        self.FSM = FSM
        self.timer = 0
        self.startTime = 0
    def Enter(self):
        self.timer = randint(0, 5)
        self.startTime = int(clock())
    def Execute(self):
        pass
    def Exit(self):
        pass

class Correction(State):
    def __init__(self, FSM):
        super(Correction, self).__init__(FSM)
    def Enter(self):
        print('Correction Needed.')
        super(Correction, self).Enter()
    def Execute(self):
        print('Correcting...')
        self.FSM.ToTransition('toMoving')
    def Exit(self):
        print('Finished Correcting.')

class Moving(State):
    def __init__(self, FSM):
        super(Moving, self).__init__(FSM)
    def Enter(self):
        print('Preparing to move.')
        super(Moving, self).Enter()
    def Execute(self):
	global horizontal
        global up
        global drop
        global spaces
        # ///////////////////////////////////////////////////////
        # THESE TRUTHS WILL JUMP TO DROP - REMOVE THESE WHEN DONE 
        # ///////////////////////////////////////////////////////
        horizontal = False
        up         = False
        drop       = True
        nplants = 10
        if (nplants < 10):
            motors.move_lateral(-600, 4000)
            time.sleep(3)
            print('////////////////////////////////////')
            print('////////// MOVING FORWARD //////////')
            print('////////////////////////////////////')       
            self.FSM.ToTransition('toGrab')
            horizontal = True
        elif ((nplants == 10) and horizontal):
            motors.move_vertical(600, 14500)
            time.sleep(10)  
            print('################################')
            print('          MOVING UP ') 
            print('################################')
            horizontal = False
            up = True
        elif ((nplants == 10) and up):
            print('##################################')
            print('            MOVING BACK ')
            print('##################################')
            motors.move_lateral(600, 25000)
	    time.sleep(15)
            motors.move_lateral(600, 22000)
            time.sleep(12)
            up = False
            drop = True
        elif ((nplants == 10) and drop and ((Gcount + Rcount) < 10)):
            print('##################################')            
            print('          CREATING SPACE ')
            print('##################################')
            motors.move_lateral(-600, 2500)
            time.sleep(3)
            self.FSM.ToTransition('toDrop')
        else:
            print('##################################')
            print('             FINISHED ')
            print('##################################')
    def Exit(self):
        print('Stopped.')
        
class Grab(State):
    def __init__(self, FSM):
        super(Grab, self).__init__(FSM)
    def Enter(self):
        print('Stopped by ultra-sonic.')
        super(Grab, self).Enter()
    def Execute(self):
        global nplants
        global horizontal
        print('Grabbing...')
        nplants += 1
        # REMOVE THIS 10
        # nplants = 10
        print('GRABBED PLANT: ' + str(nplants))
        motors.open_grabber(0)
        time.sleep(2)
        motors.move_chain(800, 4000)
        time.sleep(2)
        motors.close_grabber(0)
        time.sleep(2)
        motors.move_chain(800, 4000)
        time.sleep(2)
        self.FSM.ToTransition('toMoving')
    def Exit(self):
        print('Grabbed plant.')
        

class Drop(State):
    global plants
    def __init__(self, FSM):
        super(Drop, self).__init__(FSM)
    def Enter(self):
        print('Stopped to drop.')
        super(Drop, self).Enter()
    def Execute(self):
        global plants
        global dropped
        global Gcount
        global Rcount
        print('Dropping...')
        print(plants)
        # drops 5 green plants and
        # replaces them with a 0
        for i, val in enumerate(plants):
            dropped = False
            if (val == 'G'):
                motors.open_grabber(i)
                time.sleep(2)
                print('##################################')
                print('  GREEN GRABBER', i ,' OPENED ')                 
                print('##################################')
                motors.move_lateral(-600, 4000)
                time.sleep(2)
                plants[i] = '0'
                print(plants)
                Gcount += 1
                if (Gcount == 5):
                    dropped = True 
            if (dropped):
                break

        print('##################################')
        print('        MOVE TO RED AREA')                 
        print('##################################')
        motors.move_lateral(-600, 2500)
        time.sleep(2)
        # drops 5 red plants and
        # replaces them with a 0
        for i, val in enumerate(plants):
            dropped = False
            if (val == 'R' and (Gcount == 5)):
                motors.open_grabber(i)
                time.sleep(2)
                print('##################################')
                print('  RED GRABBER ', i ,' OPENED ')                 
                print('##################################')                
                motors.move_lateral(-600, 4000)
                time.sleep(2)
                # move here
                plants[i] = '0'
                print(plants)
                Rcount += 1
                if (Rcount == 5):
                    dropped = True
            if (dropped):
                break
            self.FSM.ToTransition('toCorrection')
    def Exit(self):
        print('Finished dropping')

class Initial(State):
    def __init__(self, FSM):
        super(Initial, self).__init__(FSM)
        self.initialAmount = 0
        self.startTime = 0
    def Enter(self):
        print('Shutting down.')
        super(Sleep, self).Enter()
        
    def Execute(self):
        print('ON')
        
        motors.move_vertical(600, 2700)
        time.sleep(3)
        motors.move_lateral(-600, 8700)
        time.sleep(7)
        motors.open_grabber(0)
        time.sleep(2)
        motors.close_grabber(0)

