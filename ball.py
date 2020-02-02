import pygame
from random import choice, randint

# from load_image import load_image


class Ball(pygame.sprite.Sprite):
    def __init__(self, position, speed, radius, color):
        super().__init__()

        self.image = pygame.Surface((2 * radius, 2 * radius))
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.image.set_colorkey(self.image.get_at((0, 0)))

        # self.image = pygame.transform.scale(load_image('ball.png'), (2 * radius, 2 * radius))
        # self.image.set_alpha(None)
        # self.image.set_colorkey(self.image.get_at((0, 0)))

        self.rect = self.image.get_rect(center=position)
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = choice(([speed, 0], [-speed, 0]))
        self.default_speed = speed
        self.default_pos = position
        self.max_speed = 24

    def update(self, paddle_group, border_group, gate_group):
        super().update()
        left_paddle, right_paddle = paddle_group.sprites()
        if pygame.sprite.collide_mask(self, left_paddle):
            new_y_speed = self.speed[1] + left_paddle.get_speed() // 2
            if new_y_speed <= self.max_speed:
                self.speed = [abs(self.speed[0]), new_y_speed]
            else:
                self.speed = [abs(self.speed[0]), self.speed[1]]
            if randint(1, 10) == 1:
                self.speed[0] += 1
        elif pygame.sprite.collide_mask(self, right_paddle):
            new_y_speed = self.speed[1] + right_paddle.get_speed() // 2
            if new_y_speed <= self.max_speed:
                self.speed = [-abs(self.speed[0]), new_y_speed]
            else:
                self.speed = [-abs(self.speed[0]), self.speed[1]]
            if randint(1, 10) == 1:
                self.speed[0] -= 1
        if pygame.sprite.spritecollideany(self, border_group):
            self.speed[1] *= -1
        if pygame.sprite.spritecollideany(self, gate_group):
            left_gate, right_gate = gate_group.sprites()
            if pygame.sprite.collide_rect(self, left_gate):
                res = -1
                self.speed = [-self.default_speed, 0]
            else:
                res = 1
                self.speed = [self.default_speed, 0]
            self.rect.center = self.default_pos
            return res

        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]
