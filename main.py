import pygame
from src.player import Player
from src.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state

def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    clock = pygame.time.Clock()
    dt = 0

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    while True:
        if(player_is_quiting() == True): return

        update(updatable, dt)
        render(screen, drawable)
        print(player.acceleration)

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

def player_is_quiting():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return False




if __name__ == "__main__":
    main()
