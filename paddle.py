import pygame


class Paddle(pygame.sprite.Sprite):
    def __init__(self, position, size, color, screen_height):
        super().__init__()
        self.image = pygame.Surface(size, pygame.SRCALPHA)
        self.image.fill(color)
        self.rect = self.image.get_rect(center=position)
        self.mask = pygame.mask.from_surface(self.image)
        self.screen_height = screen_height
        self.default_pos = position
        self.speed = 0

    def move(self, y):
        if self.rect.y + y >= 0 and self.rect.bottom + y <= self.screen_height - 1:
            self.rect.y += y
            self.speed = y

    def get_speed(self):
        return self.speed

    def set_default_pos(self):
        self.rect.center = self.default_pos
