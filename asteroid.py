from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
       

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width = 2)


    def update(self, dt):
        self.position += self.velocity * dt 

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        #creates the resulting split angle
        random_angle = random.uniform(20,50)

        #create new movement directions for resulting Asteroids
        velocity_1 = self.velocity.rotate(random_angle)
        velocity_2 = self.velocity.rotate(-random_angle)

        #calculate new radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        #Create and configure asteroids
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1.velocity = velocity_1 * 1.2

        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2.velocity = velocity_2 * 1.2
        

