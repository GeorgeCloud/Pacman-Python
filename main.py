import pygame
from colors import colors

screen = pygame.display.set_mode([500, 500])

class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(GameObject, self).__init__()
        self.surf = pygame.image.load(image)
        self.x = x
        self.y = y

    def render(self, screen):
        screen.blit(self.surf, (self.x, self.y))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    # White background
    screen.fill(colors['black'])

    pacman = GameObject(225, 225, 'pacman-art/pacman-right/1.png')
    pacman.render(screen)

    apple = GameObject(250, 225, 'pacman-art/other/apple.png')
    apple.render(screen)

    strawberry = GameObject(275, 225, 'pacman-art/other/strawberry.png')
    strawberry.render(screen)

    # Update the display
    pygame.display.flip()

pygame.init()

# # Draw a circle
# starting_position = [100, 100]
# pygame.draw.circle(screen, colors['light_blue'], tuple(starting_position), 50)
# # Challenge 2
# item_count = 1
# for _ in range(8):
#     if item_count % 3 == 0:
#         starting_position[1] += 150
#         starting_position[0] = -50
#
#     starting_position[0] += 150
#     pygame.draw.circle(screen, colors['light_blue'], tuple(starting_position), 50)
#     item_count += 1