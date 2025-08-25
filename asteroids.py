from circleshape import *

class Asteroid:
    
    def __init__(self, x, y, radius):
        self.x = (x)
        self.y = (y)
        self.radius = (radius)

    def draw(self, x, y, 2):
        pygame.draw.circle(screen, "white", self.circle(), radius=1)


    def update():
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt