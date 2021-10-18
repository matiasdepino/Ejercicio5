# Import a library of functions called 'pygame'

import pygame
from main_functions import *

# Initialize the game engine
pygame.init()

#call main routine
size = [1300, 600] # Define size of windows
width = int(input("Ancho de la ventana:"))
height = int(input("Alto de la ventana:"))
size[0] = width
size[1] = height
color = BLUE, RED, GREEN (255, 255, 255)
title = input("Asignar titulo:")
main2(size, title, color)
