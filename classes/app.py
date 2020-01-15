from pygame.locals import *
import pygame
from classes.player import Player
from classes.balloon import Balloon
from time import sleep

class App:
  player = None
  balloon = None

  def __init__(self):
    self._running = True
    self._display = None
    self._image = None
    self._background = None
    self.player = Player() 
    self.balloon = Balloon() 
    self.sceneCount = 0

  def on_init(self):
    pygame.init()
    pygame.display.set_caption("Paint Escape Game")
    self._display = pygame.display.set_mode((1280,720))
    self._running = True
    self._background = pygame.image.load("assets/Images/background.png")
    self._image = self.player.image
    self._balloon = self.balloon.image
      
  def on_loop(self):
    pass
  
  def on_render(self, sprite, balloon_sprite):
    self._display.blit(self._background, (0,0))
    self._display.blit(sprite,(self.player.x,self.player.y))
    self._display.blit(balloon_sprite,(self.balloon.x,self.balloon.y))
    y_player = self.player.update()
    self.balloon.update(y_player)
    pygame.display.flip()
    sleep(0.02) 

  def on_cleanup(self):
    pygame.quit()

  def on_execute(self):
    if self.on_init() == False:
        self._running = False
    while( self._running ):
        pygame.event.pump()
        sprite = self.player.image
        balloon_sprite = self.balloon.image
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            self._running = False
            pygame.quit()
        keys = pygame.key.get_pressed() 
        if (keys[K_RIGHT]):
            sprite = self.player.moveRight()
            self.balloon.updatePosition(self.player.x)
        if (keys[K_LEFT]):
            sprite = self.player.moveLeft()
            self.balloon.updatePosition(self.player.x)        
        if (keys[K_UP]):
            self.player.jump()
            self.balloon.jump()
        if (keys[K_ESCAPE]):
            self._running = False
        self.on_loop()
        self.on_render(sprite, balloon_sprite)
    self.on_cleanup()