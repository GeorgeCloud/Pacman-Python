import pygame
from random import randint
from cookie_cutter import Apple, Ghost, Player, Strawberry
from colors import colors

def random_coordinates():
    return randint(0, 400), randint(0, 400)


screen = pygame.display.set_mode([500, 500])
screen.fill(colors['black'])

clock = pygame.time.Clock()


ghost = Ghost()

player = Player()

fruits = []

points = 0

fruit_sprites = pygame.sprite.Group()

for _ in range(3):
    some_apple, some_strawberry = Apple(), Strawberry()

    fruit_sprites.add(some_apple)
    fruit_sprites.add(some_strawberry)

    fruits.append(some_apple)
    fruits.append(some_strawberry)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT:
                player.move_left()
                # player.change_image()
            elif event.key == pygame.K_RIGHT:
                player.move_right()
            elif event.key == pygame.K_UP:
                player.move_up()
            elif event.key == pygame.K_DOWN:
                player.move_down()

    # Clear the screen
    screen.fill(colors['black'])

    print(f'x: {player.x}, y: {player.y}')
    player.render(screen)

    for item in fruits:
        item.render(screen)
        item.move()

    ghost.render(screen)
    ghost.move()

    fruit = pygame.sprite.spritecollideany(player, fruit_sprites)
    if fruit:
        running = False

    # Update the display
    pygame.display.flip()
    clock.tick(240)

# pygame.mixer.pre_init(frequency=44100, size=-16, channels=1, buffer=512)
pygame.init()

# pygame.mixer.music.load('eating.mp3')
# pygame.mixer.music.set_volume(0.2)
# pygame.mixer.music.play(5)

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
