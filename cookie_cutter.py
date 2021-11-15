import pygame
from random import randint

class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(GameObject, self).__init__()
        resized_image = pygame.image.load(image)
        self.surf = pygame.transform.scale(resized_image, (30, 30))
        self.x = x
        self.y = y

    def render(self, screen):
        screen.blit(self.surf, (self.x, self.y))


class Apple(GameObject):
    def __init__(self):
        super(Apple, self).__init__(0, 0, 'pacman-art/other/apple.png')
        self.dx = 0
        self.dy = (randint(0, 200) / 100) + 1
        self.reset()

    def move(self):
        self.x += self.dx
        self.y += self.dy

        if self.y > 500:
            self.reset()

    def reset(self):
        self.x = randint(0, 470)
        self.y = -64


class Strawberry(GameObject):
    def __init__(self):
        super(Strawberry, self).__init__(0, 0, 'pacman-art/other/strawberry.png')
        self.dx = (randint(0, 200) / 100) + 1
        self.dy = 0
        self.reset()

    def move(self):
        self.x += self.dx
        self.y += self.dy

        if self.x > 500:
            self.reset()

    def reset(self):
        self.x = -64
        self.y = randint(0, 470)
