from turtle import position
from timer import timer
import Graphic_Manager as gm
import pygame


class UPM:
    def __init__ (self, floor, filename, position):
        self.__floor = floor
        self.__position = position                #tuple (x,y)
        self.__img
        self.__state
        self.__timer = timer()
        self.__set_img(filename)
        
    def set_floor(self, floor):
         self.__floor = floor

    def set_position(self, vertex):
        self.__position  = position
      
    def set_state(self, state):
           self.__state = state
           
    def set_img(self, filename):
          self.__img = pygame.image.load(filename).convert()
      
    def update(self):
        self.__timer.update()
    
    def get(self):
        return self.__img, self.__position
    
    def get_state(self):
        return self.__state
    
 
      
  
      