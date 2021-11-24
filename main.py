import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame.locals import *

ticks = 20

width = 500
height = 500
origin = ((width/2, height/2))

equation = input("Enter a function:\n")
functionFile = open("function.py", "w")
functionFile.write("from math import *\ndef f(x):\n    try:\n        return " + equation + "\n    except:\n        return None")
functionFile.close()

from function import f
segIndex = 0
segments = [[]]
for pixelX in range(width):
    x = (pixelX - origin[0]) / (width / 2 / ticks)
    y = f(x)
    if y != None:
        pixelY = height - (y * (height / 2 / ticks) + origin[1])
        segments[segIndex].append((pixelX, pixelY))
    elif len(segments[segIndex]) > 0:
        segments.append([])
        segIndex += 1

# Just GUI stuff below
pygame.init()
fps = pygame.time.Clock()
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("Graphing Calculator")

def draw():
    for tick in range(ticks * 2):
        pygame.draw.line(surface, pygame.Color("black"), (width / (ticks * 2) * tick, origin[1] - 5), (width / (ticks * 2) * tick, origin[1] + 5))
        pygame.draw.line(surface, pygame.Color("black"), (origin[0] - 5, height / (ticks * 2) * tick), (origin[0] + 5, height / (ticks * 2) * tick))
    pygame.draw.line(surface, pygame.Color("black"), (origin[0], 0), (origin[0], height))
    pygame.draw.line(surface, pygame.Color("black"), (0, origin[1]), (width, origin[1]))
    for segment in segments:
        pygame.draw.lines(surface, pygame.Color("red"), False, segment, 1)

surface.fill((240, 240, 240))
draw()
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            pygame.quit()
            os.sys.exit()
    
    pygame.display.update()
    fps.tick(24)