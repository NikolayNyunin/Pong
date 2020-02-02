import pygame


class ScoreCounter(pygame.sprite.Sprite):
    def __init__(self, position, score, font, color):
        super().__init__()
        self.image = font.render(str(score), 1, color)
        self.rect = self.image.get_rect(center=position)
        self.position = position
        self.score = score
        self.font = font
        self.color = color

    def change_score(self, new_score):
        self.score = new_score
        self.image = self.font.render(str(new_score), 1, self.color)
        self.rect = self.image.get_rect(center=self.position)

    def get_score(self):
        return self.score
