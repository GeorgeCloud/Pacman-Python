import pygame

class ScoreBoard(pygame.sprite.Sprite):
    def __init__(self):
        super(ScoreBoard, self).__init__()
        self.color = (255,255,255)
        self.score = 0
        self.font = pygame.font.SysFont('Comic Sans MS', 35)
        self.surf = self.font.render(f"{self.score}", False, self.color)
        self.x = 25
        self.y = 25

    def update(self, points):
        self.score += points

    def render(self, screen):
        self.surf = self.font.render(f"{self.score}", False, self.color)
        screen.blit(self.surf, (self.x, self.y))
