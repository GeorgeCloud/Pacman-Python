import pygame
from random import randint

image_names = ['1.png', '2.png', '3.png']

pacman_left  = ['pacman-art/pacman-left/' + i for i in image_names]
pacman_right = ['pacman-art/pacman-right/' + i for i in image_names]
pacman_up    = ['pacman-art/pacman-up/' + i for i in image_names]
pacman_down  = ['pacman-art/pacman-down/' + i for i in image_names]

facing_positions = [pacman_left, pacman_right, pacman_up, pacman_down]

class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path):
        super(GameObject, self).__init__()
        self.surf = None
        self.update_image(image_path)
        self.x = x
        self.y = y
        self.rect = self.surf.get_rect()

    def update_image(self, image_path):
        resized_image = pygame.image.load(image_path)
        self.surf = pygame.transform.scale(resized_image, (30, 30))

    def render(self, screen):
        self.rect.x = self.x
        self.rect.y = self.y
        screen.blit(self.surf, (self.x, self.y))

class Player(GameObject):
    player_speed = 30

    def __init__(self):
        super(Player, self).__init__(250, 250, 'pacman-art/pacman-right/1.png')
        self.x = 250
        self.y = 250
        self.image_count = 0
        self.current_direction = 1
        self.img_idx = 0

    def move_left(self):
        self.x -= self.player_speed
        if self.x < 0:
            self.x = 470

        self.current_direction = 0

    def move_right(self):
        self.x += self.player_speed
        if self.x >= 500:
            self.x = 0

        self.current_direction = 1

    def move_up(self):
        self.y -= self.player_speed
        if self.y < 0:
            self.y = 470

        self.current_direction = 2

    def move_down(self):
        self.y += self.player_speed
        if self.y >= 500:
            self.y = 0

        self.current_direction = 3

    def render(self, screen):
        self.image_count += 1
        if self.image_count > 3:
            self.image_count = 0
            current_direction = facing_positions[self.current_direction]
            self.update_image(current_direction[self.img_idx])
            self.img_idx += -2 if self.img_idx == 2 else 1

        self.rect.x = self.x
        self.rect.y = self.y
        screen.blit(self.surf, (self.x, self.y))


class Apple(GameObject):
    def __init__(self):
        super(Apple, self).__init__(0, 0, 'pacman-art/other/apple.png')
        self.dx = 0
        self.dy = (randint(0, 200) / 100) + 1
        self.reset()
        self.rect = self.surf.get_rect()

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


class Ghost(GameObject):
    def __init__(self):
        super(Ghost, self).__init__(0, 0, 'pacman-art/ghosts/inky.png')
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
