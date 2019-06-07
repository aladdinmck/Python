from random import randint
from time import clock

# Transition
class Transition(object):
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
                        
                        class CleanDishes(State):
                            def __init__(self, FSM):
                                super(CleanDishes, slef).__init__(FSM)
                                	
                                def Enter(self):	
                                    print('Preparing to clean dishes.')
                                    super(CleanDishes, self).Enter()
                                    
                                    def Execute(self):
                                        print('Cleaning dishes')
                                        if (self.startTime + self.timer <= clock()):
                                            if not (randint(1,3) % 2):
                                                self.FSM.ToTransition('toVacuum')
                                            else:
                                                self.FSM.ToTransition('toSleep')
                                                
                                                def Exit(self):
                                                    print ('Finished cleaning dishes.')

                                                    class Vacuum(State):
                                                        def __init__(self, FSM):
                                                            super(Vacuum, self).__init__(FSM)
                                                            
                                                            def Enter(self):
                                                                print('Starting to Vacuum')
                                                                super(Vacuum).Enter()
                                                                
                                                                def Execute(self):
                                                                    print('Vacuuming')
                                                                    if (self.startTime + self.timer <= clock()):
                                                                        if not (randint(1,3) %2):
                                                                            self.FSM.ToTransition('toSleep')
                                                                        else:
                                                                            self.FSM.ToTransition('toCleanDishes')
                                                                            
                                                                            def Exit(self):
                                                                                print('Finished Vacuuming')
                                                                                
                                                                                class Sleep(State):
                                                                                    def __init__(self, FSM):
                                                                                        super(Sleep, self).__init__(FSM)
                                                                                        
                                                                                        def Enter(self):
                                                                                            print('Sleeping')
                                                                                            if (self.startTime + self.timer <= clock()):
                                                                                                if not (randint(1,3) %2):
                                                                                                    self.FSM.ToTransition('toVacuum')
                                                                                                else:
                                                                                                    self.FSM.ToTransition('toCleanDishes')
                                                                                                    
                                                                                                    def Exit(self):
                                                                                                        print('Waking up from Sleep')
                                                                                                        
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
                                                                                                                                        
                                                                                                                                        class RobotMaid(Char):
                                                                                                                                            def __init__(self):
                                                                                                                                                self.FSM = FSM(self)
                                                                                                                                                
# States
                                                                                                                                                self.FSM.AddState('Sleep', Sleep(self.FSM))
                                                                                                                                                self.FSM.AddState('CleanDishes', CleanDishes(self.FSM))
                                                                                                                                                self.FSM.AddState('Vacuum', Vacuum(self.FSM))
                                                                                                                                                
# Transitions
                                                                                                                                                self.FSM.AddTransition('toSleep', Transition('Sleep'))
                                                                                                                                                self.FSM.AddTransition('tovacuum', Transition('Vacuum'))
                                                                                                                                                self.FSM.AddTransition('toCleanDishes', Transition('Clean'))
                                                                                                                                                
                                                                                                                                                self.FSM.SetState('Sleep')
                                                                                                                                                
                                                                                                                                                def Execute(self):
                                                                                                                                                    self.FSM.Execute()
                                                                                                                                                    
                                                                                                                                                    if __name__ == '__main__':
                                                                                                                                                        r = RobotMaid()
                                                                                                                                                        for i in xrange(20):
                                                                                                                                                            startTime = clock()
                                                                                                                                                            timeInterval = 1
                                                                                                                                                            while (starTime + timeInterval > clock()):
                                                                                                                                                                pass 
                                                                                                                                                            r.Execute()
                                                                                                                                                            
