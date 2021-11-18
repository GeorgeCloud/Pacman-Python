import pygame
from random import randint
from time import sleep
from cookie_cutter import Apple, Ghost, Player, Strawberry
from colors import colors

screen = pygame.display.set_mode([500, 500])
screen.fill(colors['black'])

clock = pygame.time.Clock()

score = 0

pygame.mixer.init()
eating_sound_effect = pygame.mixer.Sound("eating.mp3")
died_sound_effect = pygame.mixer.Sound("died.mp3")

eating_sound_effect.play(-1)

player = Player()

all_ghosts = []
fruits = []
ghost_sprites = pygame.sprite.Group()
fruit_sprites = pygame.sprite.Group()

every_three_renders = 0
# Create list of items to populate screen
for _ in range(20):
    if every_three_renders > 3:
        ghost = Ghost()
        ghost_sprites.add(ghost)
        all_ghosts.append(ghost)
        every_three_renders = 0

    some_apple, some_strawberry = Apple(), Strawberry()

    fruit_sprites.add(some_apple)
    fruit_sprites.add(some_strawberry)

    fruits.append(some_apple)
    fruits.append(some_strawberry)

    every_three_renders += 1

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
            elif event.key == pygame.K_RIGHT:
                player.move_right()
            elif event.key == pygame.K_UP:
                player.move_up()
            elif event.key == pygame.K_DOWN:
                player.move_down()

    screen.fill(colors['black'])

    player.render(screen)

    for item in fruits:
        item.render(screen)
        item.move()

    for ghost in all_ghosts:
        ghost.render(screen)
        ghost.move()

    fruit = pygame.sprite.spritecollideany(player, fruit_sprites)
    if fruit:
        score += 1
        fruit.reset()

    check_ghost_collision = pygame.sprite.spritecollideany(player, ghost_sprites)
    if check_ghost_collision:
        eating_sound_effect.stop()
        died_sound_effect.play()
        for _ in range(50):
            screen.fill(colors['green'])
            pygame.display.flip()
            screen.fill(colors['black'])
            pygame.display.flip()
        running = False

    pygame.display.flip()
    clock.tick(240)

sleep(1.3)
print("SCORE:", score)

pygame.init()
