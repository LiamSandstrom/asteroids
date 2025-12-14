import sys
import pygame
from src.shot import Shot
from src.asteroid import Asteroid
from src.player import Player
from src.asteroidfield import AsteroidField
from src.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event

def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    clock = pygame.time.Clock()
    dt = 0

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField();


    while True:
        if(player_is_quiting() == True): return

        update(updatable, dt)
        check_collision(asteroids, player, shots)
        render(screen, drawable)

        dt = clock.tick(144) / 1000


def render(screen, group):
    screen.fill("black")
    for i in group:
        i.draw(screen)
    pygame.display.flip()

def update(group, dt):
    log_state()
    for i in group:
        i.update(dt)


def check_collision(asteroids, player, shots):
    for a in asteroids:
        for s in shots:
            if a.collides_with(s):
                s.kill()
                a.split()

        if a.collides_with(player): 
            sys.exit()

def player_is_quiting():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return False

if __name__ == "__main__":
    main()
