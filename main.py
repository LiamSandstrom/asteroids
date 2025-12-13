import pygame
from src.player import Player
from src.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state

def main():
    clock = pygame.time.Clock()
    dt = 0

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        log_state()

        render(screen, player, dt)

        dt = clock.tick(60) / 1000



def render(screen, player, dt):
    screen.fill("black")
    player.update(dt)
    player.draw(screen)
    pygame.display.flip()


if __name__ == "__main__":
    main()
