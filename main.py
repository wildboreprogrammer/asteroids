# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
import os
from asteroidfield import *
from shot import *
#os.environ["SDL_VIDEODRIVER"] = "dummy"  # Forces software rendering
os.environ['SDL_VIDEO_CENTERED'] = '1'


def main():
    pygame.init()
    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    clock = pygame.time.Clock()
    dt = 0 #delta time
    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    #Setting static containers fields \/\/\/\/\/
    Player.containers = (updatable, drawable)  
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)

    #Creating instances of these objects \/\/\/\/
    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF)

   #Game Loop \/\/\/\/\/
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0))  # Clear the entire screen to black
        pygame.draw.rect(screen, "black", (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))  # Extra clear!
        #pygame.display.update()

        for object in updatable:
            object.update(dt)
        
        for asteroid in asteroids:
            if player.collided(asteroid):
                print("Game over!")
                return
        for asteroid in asteroids:
            print("I'm here!")
            for shot in shots:
                print("I'm here too!")
                print(shot.collided(asteroid))
                if shot.collided(asteroid):
                    asteroid.split()
                    shot.kill()

        for object in drawable:
            object.draw(screen)
        
        
        #pygame.display.update()
        pygame.display.flip()

        dt = clock.tick(60)/1000




if __name__ == "__main__":
    main()
