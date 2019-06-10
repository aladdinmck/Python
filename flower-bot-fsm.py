from random import randint
from time import clock 
plants = 0

# Transition
class Transition(object):
    print('Starting up...')
    def __init__(self, toState):
        self.toState = toState
    def Execute(self):
        print('Transitioning...')

# States
class State(object):
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
        if (self.startTime + self.timer <= clock()):
            if not (randint(1,3) % 2):
                self.FSM.ToTransition('toMoving')
            else:
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
        if (plants < 10):
            print('Moving forward')
            if not (randint(1,3) % 2):
                self.FSM.ToTransition('toCorrection')
            if (randint(4, 6) % 2):
                self.FSM.ToTransition('toGrab')
        elif ((plants > 10) and horzontal):
            print('Moving up')
            if not (randint(1,3) % 2):
                self.FSM.ToTransition('toCorrection')
        elif ((plants > 10) and horzontal and up):
            print('Moving backward')
            if not (randint(1,3) % 2):
                self.FSM.ToTransition('toCorrection')
        elif ((plants > 10) and horizontal and up and drop):
            print('Moving forward')
            if not (randint(1,3) % 2):
                self.FSM.ToTransition('toCorrection')
            if (randint(4, 6) % 2):
                self.FSM.ToTransition('toDrop')
        else:
            print('Nothing')
    def Exit(self):
        print('Stopped.')
        
class Grab(State):
    
    def __init__(self, FSM):
        super(Grab, self).__init__(FSM)
    def Enter(self):
        print('Stopped by ultra-sonic.')
        super(Grab, self).Enter()
    def Execute(self):
        print('Grabbing...')
        self.FSM.ToTransition('toCorrection')
    def Exit(self):
        print('Grabbed plant.')
        

class Drop(State):
    def __init__(self, FSM):
        super(Drop, self).__init__(FSM)
    def Enter(self):
        print('Stopped to drop.')
        super(Drop, self).Enter()
    def Execute(self):
        print('Dropping...')
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
        if (self.startTime + self.timer <= clock()):
            if not (randint(1,3) %2):
                self.FSM.ToTransition('toCorrection')
            else:
                self.FSM.ToTransition('toCorrection')

    def Exit(self):
        print('Initial move up.')

# Finite State Machines
class FSM(object):
    def __init__(self, character):
        self.char = character
        self.states = {}
        self.transitions = {}
        self.curState = None
        self.prevState = None # Prevents two states from looping   
        self.trans = None

    def AddTransition(self, transName, transition):
        self.transitions[transName] = transition

    def AddState(self, stateName, state):
        self.states[stateName] = state

    def SetState(self, stateName):
        self.prevState = self.curState
        self.curState = self.states[stateName]

    def ToTransition(self, toTrans):
        self.trans = self.transitions[toTrans]

    def Execute(self):
        if (self.trans):
            self.curState.Exit()
            self.trans.Execute()
            self.SetState(self.trans.toState)
            self.curState.Enter()
            self.trans = None
        self.curState.Execute()

# Implementation                                                                                          
Char = type('Char', (object,), {})

class FlowerBot(Char):
    def __init__(self):
        self.FSM = FSM(self)

        # States                                                                                                
        self.FSM.AddState('Initial', Initial(self.FSM))
        self.FSM.AddState('Correction', Correction(self.FSM))
        self.FSM.AddState('Moving', Moving(self.FSM))
        self.FSM.AddState('Grab', Grab(self.FSM))
        self.FSM.AddState('Drop', Drop(self.FSM))

        # Transitions                                                                                           
        self.FSM.AddTransition('toInitial', Transition('Initial'))
        self.FSM.AddTransition('toCorrection', Transition('Correction'))
        self.FSM.AddTransition('toMoving', Transition('Moving'))
        self.FSM.AddTransition('toGrab', Transition('Grab'))
        self.FSM.AddTransition('toDrop', Transition('Drop'))

        self.FSM.SetState('Initial')

    def Execute(self):
        self.FSM.Execute()

if __name__ == '__main__':
    r = FlowerBot()
    for i in range(200):
        startTime = clock()
        timeInterval = 1
        while (startTime + timeInterval > clock()):
            pass
        r.Execute()


