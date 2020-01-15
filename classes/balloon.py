import pygame

class Balloon:

    x = 580
    y = 340
    image = pygame.image.load("assets/Images/Balloon/balloon.png")
    isMoving = 0  
    isjump = 0  
    v = 14
    m = 2

    def isMoving(self):
        self.isMoving = 1

    def updatePosition(self, x_player):
        self.x = x_player

    def jump(self):
        self.isjump = 1

    def update(self, y_player):
        print("Y PLAYER: ", y_player)
        if self.isjump:
            if self.v > 0:
                F = ( 0.5 * self.m * self.v )
                print(0)
            elif y_player - self.y >= 200:
                F = -( 0.5 * self.m * (self.v * self.v) )
                print(1)
            else:
                F = -( 0.5 * self.m * (self.v * self.v) )
                print(2)
            self.y = self.y - F
            self.v = self.v - 1
            if self.y >= 340:
                self.y = 340
                self.isjump = 0
                self.v = 14     