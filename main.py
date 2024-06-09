import os
import pygame
import Graphic_Manager as gm
import game_2 as Game




def get_settings():
    #check if ther is json file
        #case true: open it and return the data(num of floors, num of elevators)
        #case False: calculats the dimentions of the screen - and returns the max of floors posible, and minus one elevators
    return (0,0)

    
num_floors, num_of_elevators = get_settings()

the_game = Game.Game(num_floors,num_of_elevators)
the_game.init()
the_game.play()

    
