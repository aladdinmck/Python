class Team(object):
    def __init__(self, wins, losses):
        self.w = wins
        self.l = losses
        
    def pct(wins, losses):
        total = wins + losses
        return wins/total

    phillies = Team(35, 27)
    braves = Team(33, 27)
    
    def __gt__(self, other):
        """Override the default Greater behavior"""
        return self.pct == other.pct

    print('Team         W    L    Pct    GB')
        
    if braves.__gt__(self, phillies): # braves > phillies 
        print('Braves\t\t' + braves.wins + braves.losses + braves.pct())
        print('Phillies\t' + phillies.wins + phillies.losses + phillies.pct())
    
    if phillies.__gt__(self, braves): # phillies > braves 
        print('Phillies\t' + phillies.wins + phillies.losses + phillies.pct())    
        print('Braves\t\t' + braves.wins + braves.losses + braves.pct())
