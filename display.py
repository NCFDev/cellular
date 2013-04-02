import pygame, sys, threading
from pygame.locals import *
Thread = threading.Thread

pygame.init()
fpsClock = pygame.time.Clock()
display_width = 1000
display_height = 700
windowSurfaceObj = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Nautical Cell Force 2')

redColor = pygame.Color(255,0,0)
greenColor = pygame.Color(0,255,0)
blueColor = pygame.Color(0,0,255)
whiteColor = pygame.Color(255,255,255)
mousex, mousey = 0,0

def convert_to_display_loc(pos):
    return int(round((pos[0]*display_width))), int(round((pos[1]*display_height)))

# main display loop
class Display(Thread):
    def __init__(self,environment):
        Thread.__init__(self)
        self.environment = environment
    def run(self):
        while True:
            windowSurfaceObj.fill(whiteColor)
            for cell in self.environment.cell_list:
                # is the 20 width and the height?
                pygame.draw.circle(windowSurfaceObj, redColor, convert_to_display_loc((cell.pos.x, cell.pos.y)), 20, 0)
            # environment's food set is changing while the for loop runs, so we must make a copy of it so that we do not iterate over a chaning set
                food_set = self.environment.food_set.copy()
            for food in food_set:
                pygame.draw.circle(windowSurfaceObj, greenColor, convert_to_display_loc((food.pos.x, food.pos.y)), 10, 10)
        
            for event in pygame.event.get():
                if event.type ==QUIT:
                    pygame.quit()
                    return ()
                    
            pygame.display.update()
            fpsClock.tick(15)

def display(environment):
    dis = Display(environment)
    dis.start()
    # return the thread so that main can check if it is alive
    return(dis)
    

