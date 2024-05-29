from turtle import position
from timer import timer
import Graphic_Manager as gm
import pygame


class UPM:
    _img = None
    _state = None

    def __init__ (self, floor, filename, position):
        self._floor = floor
        self._position = position                #tuple (x,y)
        #self._img = None # = pygame.image.load(filename).convert()
       
        self._timer = timer()
        
        
    def set_floor(self, floor):
         self._floor = floor

    def set_position(self, vertex):
        self._position  = position
      
    def set_state(self, state):
           self._state = state
           
    def set_img(self, filename):
          self._img = pygame.image.load(filename).convert()
      
    def update_(self):
        self._timer.update()
    
    def get(self):
        return self._img, self._position, self._timer.get_exact
    
    def get_state(self):
        return self._state
        
    def __repr__(self) -> str:
        return f'position:{self._position}, state:{self._state}' 
      
    def __str__(self) -> str:
        return f'position:{self._position}, state:{self._state}' 
      
  
      