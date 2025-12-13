import pygame
from src.circleshape import CircleShape
from src.constants import LINE_WIDTH, PLAYER_ACCELERATION_AMOUNT, PLAYER_DEACCELERATION_AMOUNT, PLAYER_RADIUS, PLAYER_SPEED, PLAYER_TURN_SPEED


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.acceleration = 1
        self.forwardLast = True

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)


    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt * (1 + self.acceleration * 0.12)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt * - 1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            if self.forwardLast == True :
                self.inc_acceleration(dt)
            else:
                self.is_accelerating = False
                self.dec_acceleration(dt)
                

            self.move(dt)
            return

        if keys[pygame.K_s]:
            if self.forwardLast == False :
                self.inc_acceleration(dt)
            else:
                self.dec_acceleration(dt)


            self.move(dt * - 1)
            return

        self.dec_acceleration(dt)
        

    def inc_acceleration(self, dt):
        if self.acceleration >= 2:
            self.acceleration = 2
            return

        self.acceleration += PLAYER_ACCELERATION_AMOUNT * dt

    def dec_acceleration(self, dt):
        if self.acceleration <= 1:
            self.acceleration = 1
            self.forwardLast = not self.forwardLast
            return
        self.acceleration -= (PLAYER_DEACCELERATION_AMOUNT + (self.acceleration * 0.25 - 1)) *  dt 

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * self.acceleration * dt
        self.position += rotated_with_speed_vector
