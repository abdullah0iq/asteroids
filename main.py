import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # creating groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    

    Asteroid.containers = (asteroids,updatable,drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (drawable , updatable, shots)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH/2 , SCREEN_HEIGHT/2)
    
    while True:
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(color=(0,0,0))
        
        for obj in drawable:
            obj.draw(screen)




        dt = clock.tick(60)/1000
        for obj in updatable:
            obj.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collision_detector(player):
                print("Game is over!\nBy the way, you suck, and you suck hard boy")
                raise SystemExit()
            for shot in shots:
                if shot.collision_detector(asteroid):
                    shot.kill()
                    asteroid.split()
                    
                    


        pygame.display.flip()
    


if __name__ == "__main__":
    main()