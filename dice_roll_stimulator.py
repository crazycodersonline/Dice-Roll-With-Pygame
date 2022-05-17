import pygame
from sys import exit
import random

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Dice Roll Stimulator")

background_surf = pygame.image.load('graphics/background2.png')
font = pygame.font.Font('font/SunnyspellsRegular.otf', 50)
start_text = font.render("press SPACEBAR to start rolling", True, (255, 235, 193))

dice = []
roll_animation_images = []

# since there are 8 animation images
for num in range(1, 9):
    # since only six dice images
    if num <= 6:
        dice_image = pygame.image.load('graphics/dice/' + str(num) + '.png')
        dice.append(dice_image)

    roll_animation_image = pygame.image.load('graphics/animation/roll' + str(num) + '.png')
    roll_animation_images.append(roll_animation_image)

roll_aud = pygame.mixer.Sound('audio/roll_aud.mp3')
roll_stop_aud = pygame.mixer.Sound('audio/roll_stop_aud.mp3')

first = True
dice_num = dice[0]
is_rolling = False
rolling_counter = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background_surf, (0, 0))
    screen.blit(start_text, (50, 300))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not is_rolling:
        is_rolling = True
        roll_aud.play()
        roll_num = random.randint(1, 6)
        dice_num = dice[roll_num - 1]
        first = True
        screen.blit(roll_animation_images[rolling_counter], (250, 150))
        rolling_counter += 1
    else:
        if is_rolling:
            screen.blit(roll_animation_images[rolling_counter], (250, 150))
            rolling_counter += 1

            if rolling_counter >= 8:
                rolling_counter = 0
                is_rolling = False

        else:
            screen.blit(dice_num, (250, 150))
            if first:
                roll_stop_aud.play()
                first = False

    pygame.display.update()
    clock.tick(13)


