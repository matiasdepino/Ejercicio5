# Import a library of functions called 'pygame'
import pygame
from main_functions import *
# Initialize the game engine
pygame.init()
# Set window size
size = [1300, 600]
width = int(input("Ancho de la ventana: "))
height = int(input("Alto de la ventana: "))
size[0] = width
size[1] = height
RED = int(input("RED :"))
GREEN = int(input("GREEN :"))
BLUE = int(input("BLUE :"))
n1 = (RED, GREEN, BLUE)
title = input("Ingresar titulo :")
# Call main routine
main2(size, title, n1)


