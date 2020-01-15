import pygame

class Player:
  
    x = 580
    y = 540
    speed = 20
    isjump = 0   
    walkCount = 0  
    v = 8 
    m = 2
    image = pygame.image.load("assets/Images/Player/standing.png")
    walkRight = [
      pygame.image.load("assets/Images/Player/R1.png"),
      pygame.image.load("assets/Images/Player/R2.png"),
      pygame.image.load("assets/Images/Player/R3.png"),
      pygame.image.load("assets/Images/Player/R4.png"),
      pygame.image.load("assets/Images/Player/R5.png"),
      pygame.image.load("assets/Images/Player/R6.png")
    ]
    walkLeft = [
      pygame.image.load("assets/Images/Player/L1.png"),
      pygame.image.load("assets/Images/Player/L2.png"),
      pygame.image.load("assets/Images/Player/L3.png"),
      pygame.image.load("assets/Images/Player/L4.png"),
      pygame.image.load("assets/Images/Player/L5.png"),
      pygame.image.load("assets/Images/Player/L6.png")
    ]
            
    def moveRight(self):
        self.x = self.x + self.speed
        self.walkCount += 1
        return self.walkRight[self.walkCount % 6]
 
    def moveLeft(self):
        self.x = self.x - self.speed
        self.walkCount += 1
        return self.walkLeft[self.walkCount % 6]
 
    def jump(self):
        self.isjump = 1

    def update(self):
        if self.isjump:
            # Calculate force (F). F = 0.5 * mass * velocity^2.
            if self.v > 0:
                F = ( 0.5 * self.m * (self.v*self.v) )
            else:
                F = -( 0.5 * self.m * (self.v*self.v) )
    
            # Change position
            self.y = self.y - F

            # Change velocity
            self.v = self.v - 1

            # If ground is reached, reset variables.
            if self.y >= 540:
                self.y = 540
                self.isjump = 0
                self.v = 8              
          


 