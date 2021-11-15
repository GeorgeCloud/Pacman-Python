import pygame
from random import randint, shuffle
from cookie_cutter import GameObject, Apple, Strawberry
from colors import colors


screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()

screen.fill(colors['black'])

pacman = GameObject(225, 225, 'pacman-art/pacman-right/1.png')

def random_coordinates():
    return randint(0, 400), randint(0, 400)


fruits = []

for _ in range(3):
    x, y = random_coordinates()  # Add error collision
    fruits.append(Apple())
    fruits.append(Strawberry())

apple = GameObject(250, 225, 'pacman-art/other/apple.png')

strawberry = GameObject(275, 225, 'pacman-art/other/strawberry.png')

some_apple = Apple()

some_strawberry = Strawberry()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    # Clear the screen
    screen.fill(colors['black'])

    for item in fruits:
        item.render(screen)
        item.move()

    # Update the display
    pygame.display.flip()
    clock.tick(15)

pygame.init()

# # Draw a circle
# starting_position = [100, 100]
# GameObject(starting_position[0], starting_position[1], 'pacman-art/other/apple.png').render(screen)
# # Challenge 2
# for item_count in range(1, 9):
#     if item_count % 3 == 0:
#         starting_position[1] += 150
#         starting_position[0] = -50
#
#     starting_position[0] += 150
#
#     if item_count % 2 == 0:
#         GameObject(starting_position[0], starting_position[1], 'pacman-art/other/apple.png').render(screen)
#     else:
#         GameObject(starting_position[0], starting_position[1], 'pacman-art/other/strawberry.png').render(screen)
#     item_count += 1