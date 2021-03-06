import pygame
import os
import math 

class FlowerBotSim:
#      pygame.init()

      def __init__(self):
            self.width = 500
            self.height = 250
            self.win = pygame.display.set_mode((self.width, self.height))
            self.bg = pygame.image.load(os.path.join("white_bg.png"))
            self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
            self.clicks = [] # remove this
            self.path = [(30,190),(30,170),(75,170),(110,170),(150,170),
                         (180,175),(220,170),(255,170),(290,170),(325,170),
                         (365,170),(399,170),(399,145),(375,145),(375,125),
                         (375,75),(5,75),(375,75)]
            self.x = self.path[0][0]
            self.y = self.path[0][1]
            self.img = None
            self.dis = 0
            self.path_pos = 0
            self.move_count = 0
            self.move_dis = 0
            
            
      def run(self):
            run = True
            clock = pygame.time.Clock()
            while run:
                  clock.tick(60)
                  for event in pygame.event.get():
                        if event.type == pygame.QUIT:                              
                              run = False

                        pos = pygame.mouse.get_pos()
                              
                        if event.type == pygame.MOUSEBUTTONDOWN:
                              self.clicks.append(pos)
                              print(pos)
                              
                  self.draw()
            pygame.quit()
'''            
# Plant Line                                                                                        
canvas.create_line(75,170,399,170)                                              
# Plants                                                 
canvas.create_line(75,165,75,175)                                                         
canvas.create_line(111,165,111,175)                                                               
canvas.create_line(147,165,147,175)                                                           
canvas.create_line(183,165,183,175)                                           
canvas.create_line(219,165,219,175)                                      
canvas.create_line(255,165,255,175)                                    
canvas.create_line(291,165,291,175)                                                        
canvas.create_line(327,165,327,175)
canvas.create_line(363,165,363,175)                                                    
canvas.create_line(399,165,399,175) 
   '''         
      def draw(self):
            self.win.blit(self.bg, (0,0))
            pygame.draw.rect(self.win, (255,215,0), [30, 190, 50, 50])

            # Plants
            pygame.draw.line(self.win, (0,0,0), (75,170),(399,170) , 2)

            pygame.draw.line(self.win, (0,0,0), (111,165),(111,175) , 2)
            pygame.draw.line(self.win, (0,0,0), (147,165),(147,175) , 2)
            pygame.draw.line(self.win, (0,0,0), (183,165),(183,175) , 2)
            pygame.draw.line(self.win, (0,0,0), (219,165),(219,175) , 2)
            pygame.draw.line(self.win, (0,0,0), (255,165),(255,175) , 2)
            pygame.draw.line(self.win, (0,0,0), (291,165),(291,175) , 2)
            pygame.draw.line(self.win, (0,0,0), (327,165),(327,175) , 2)
            pygame.draw.line(self.win, (0,0,0), (363,165),(363,175) , 2)
            for p in self.clicks:
                  pygame.draw.circle(self.win, (255,0,0), (p[0], p[1], 5, 0))
            pygame.display.update()
            

            
      def move(self, change):
            x1, y1 = self.path[self.path_pos]
            if self.path_pos + 1 >= len(self.path):
                  x2, y2 = (-10, 355)
            else:
                  x2, y2 = self.path[self.path_pos + 1]            

            dirn = ((x2-x1), (y2-y1))
            length = math.sqrt((dirn[0])**2 + (dirn[1])**2)
            dirn = (dirn[0]/length, dirn[1]/length)
            
            
            
            move_x, move_y = ((self.x + dirn[0]), (self.y + dirn[1]))
            self.x = move_x
            self.y = move_y
            
            # Go to next point
            if dirn[0] >= 0: #moving right
                  if dirn[1] >= 0:
                        if self.x >= x2 and self.y >= y2:
                              self.path_pos += 1
                  else:
                        if self.x >= x2 and self.y <= y2:
                              self.path_pos += 1
            else: # moving left
                  if dirn[1] >= 0: # moving down
                        if self.x <= x2 and self.y >= y2:
                              self.path_pos += 1
                  else:
                        if self.x <= x2 and self.y <= y2:
                              self.path_pos += 1
            

            
f = FlowerBotSim()
f.run()


'''
# Track
# Left Vertical Line
canvas.create_line(25, 170, 25, 75)

# Top Line
canvas.create_line(0, 75, 375, 75)

# Bottom Line
canvas.create_line(25, 125, 375, 125)

# Right end vertical Line
canvas.create_line(375, 75, 375, 125)


# Plants
canvas.create_oval(50,130,60,140)
canvas.create_oval(85,130,95,140)
canvas.create_oval(120,130,130,140)
canvas.create_oval(155,130,165,140)
canvas.create_oval(195,130,205,140)
canvas.create_oval(230,130,240,140)
canvas.create_oval(265,130,275,140)
canvas.create_oval(300,130,310,140)
canvas.create_oval(335,130,345,140)
canvas.create_oval(370,130,380,140)

# Plant Line
canvas.create_line(75,170,399,170)
# Plants 
canvas.create_line(75,165,75,175)
canvas.create_line(111,165,111,175)
canvas.create_line(147,165,147,175)
canvas.create_line(183,165,183,175)
canvas.create_line(219,165,219,175)
canvas.create_line(255,165,255,175)
canvas.create_line(291,165,291,175)
canvas.create_line(327,165,327,175)
canvas.create_line(363,165,363,175)
canvas.create_line(399,165,399,175)


# Drop Zones
canvas.create_rectangle(1,1,200,40, fill = 'green', outline = 'green')
canvas.create_rectangle(200,1,400,40, fill = 'red', outline = 'red')

# Robot
canvas.create_rectangle(5, 150, 55, 200, fill = 'gold')
'''



