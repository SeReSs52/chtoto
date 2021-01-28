import pygame, sys, random
from pygame import *

H = 640
W = 840

YELLOW = (210, 206, 116)
BLUE = (0, 110, 4)

block_color = "#FF0000"

DISPLAY = pygame.display.set_mode((W, H))
pygame.display.set_caption("2019")
vinni = pygame.image.load('vinni-pukh-v-png.png')
vinni = pygame.transform.scale(vinni, (20, 20))
exit = pygame.image.load('exit.jpg')
exit = pygame.transform.scale(exit, (20, 20))
vinni_pos = vinni.get_rect()
vinni_pos.x = 35
vinni_pos.y = 590

SPEED = 1000
SIZE = 20
FPS = 10
fpsClock = pygame.time.Clock()

pygame.mixer.init()
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        level = [
            "------------------------------------------",
            "-------------------   -   -          - *--",
            "----              - - - - - - - -- - -  --",
            "---- ------------ - - - - - - - -- - -   -",
            "---- ------------ - - - - - - - -  ----- -",
            "---- -+           - - - - - - - -      - -",
            "---- -------------- - - - - --- - ----   -",
            "----                - - - - --  -    -----",
            "------------------- - - - -  -- - -- -----",
            "-                   - - - - ---   --     -",
            "------------------- - - - - --  -       --",
            "------------------- - - - - -   ---- -----",
            "-------   --------- - - - - --  ---  -----",
            "------- - -   -   - - - - -  --  --  -----",
            "------- -   -   - - - - - -   --  -  -----",
            "------- --------- - - - - ---  --    -----",
            "-     - -       - - - - - -   ------ -----",
            "- --- - - ----- - - - - - - --- - -  -----",
            "- -   - -     -   - -   - - --- -   ------",
            "- - --- - --- ----- --- - -   - - --------",
            "- -   - -  -- -   -   --- -   -     ------",
            "- --- - -     - - --- --- ---     - ---  -",
            "- -   - --- --- -   - ---   --    - ---  -",
            "- - ---   -   - - --- -----  -    -      -",
            "- - ---   - -   -     ------ ----------- -",
            "- - -   - - -  -- ----------          -- -",
            "- -   - - - ----- ------ ------ ----     -",
            "- --- - - - -   - ------ ------ ----------",
            "-   - - - - - - - ------ ------ ----------",
            "-   - - - - - - - ------ ------ ----------",
            "--@ - - - -   -   -                     +-",
            "------------------------------------------"
        ]

        platforms = []

        DISPLAY.fill(YELLOW)
        x = y = 0
        for row in level:
            for col in row:
                if col == "-":
                    block = pygame.Rect(x, y, 20, 20)
                    pygame.draw.rect(DISPLAY, BLUE, block)
                    platforms.append(block)
                if col == "*":
                    exit_pos = pygame.Rect(x, y, 20, 20)
                    pygame.draw.rect(DISPLAY, (0, 0, 0), exit_pos)
                    DISPLAY.blit(exit, (x, y))
                if col == "+":
                    pashalka_pos = pygame.Rect(x, y, 20, 20)
                    pygame.draw.rect(DISPLAY, (255, 0, 146), pashalka_pos)
                x += SIZE
            y += SIZE
            x = 0

        vinni_x = 0
        vinni_y = 0
        direction = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            vinni_x = -5
            direction = 1
        elif keys[pygame.K_RIGHT]:
            vinni_x = 5
            direction = 2
        elif keys[pygame.K_UP]:
            vinni_y = -5
            direction = 3
        elif keys[pygame.K_DOWN]:
            vinni_y = 5
            direction = 4

        vinni_pos.x += vinni_x
        vinni_pos.y += vinni_y

        if vinni_pos.colliderect(exit_pos):
            break

        for p in platforms:
            if vinni_pos.colliderect(p):  # если есть пересечение платформы с игроком
                if direction == 1:  # если движется влево
                    vinni_x = 5
                elif direction == 2:  # если движется вправо
                    vinni_x = -5
                elif direction == 3:  # если движется вверх
                    vinni_y = 5
                elif direction == 4:  # если падает вниз
                    vinni_y = -5
                vinni_pos.x += vinni_x
                vinni_pos.y += vinni_y


        DISPLAY.blit(vinni, (vinni_pos.x, vinni_pos.y))
        pygame.display.update()
        fpsClock.tick(FPS)

main()
pygame.quit()
sys.exit(0)