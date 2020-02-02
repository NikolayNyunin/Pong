import pygame


class Line(pygame.sprite.Sprite):
    def __init__(self, start_point, end_point, thickness=1):
        super().__init__()
        x1, y1 = start_point
        x2, y2 = end_point
        if x1 == x2:
            self.image = pygame.Surface((thickness, abs(y2 - y1)))
        elif y1 == y2:
            self.image = pygame.Surface((abs(x2 - x1), thickness))
        else:
            raise ValueError
        x, y = min((x1, x2)), min((y1, y2))
        self.rect = self.image.get_rect(x=x, y=y)
