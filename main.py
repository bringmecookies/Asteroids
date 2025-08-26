import pygame
from constants import *
from player import *
from asteroidfield  import *
from shot import *
import sys


def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2 

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player1 = Player(x, y)
    asteroidfield = AsteroidField()
    

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #This updates all Objects
        updatable.update(dt)
        
        #This renders the background in black
        screen.fill("black")
        
        #This checks playercollision with Asteroids
        for asteroid in asteroids:
            if player1.collides_with(asteroid):
                print("Game Over!")
                pygame.time.wait(2000)
                sys.exit()

        #check for shot collision with Asteroid

        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    asteroid.split()
                    shot.kill()

        #This renders all objects in the window
        for objects in drawable:
            objects.draw(screen)

        #refresh the screen with new information
        pygame.display.flip()
        

        #limit framerate to 60 fps and return delta time to dt
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
