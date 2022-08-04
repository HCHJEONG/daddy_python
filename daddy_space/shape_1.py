import pygame
from math import pi
import os

# 초기화
pygame.init()

# 화면 크기
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# 타이틀, 아이콘
pygame.display.set_caption("GUI_LAB")

# FPS
clock = pygame.time.Clock()

# 폰트
game_font = pygame.font.SysFont(None, 30)

# 색 상수
P_BLUE = (147, 214, 237)

##################################################

# 배경
background = pygame.image.load("./background.png")

##################################################

# 변수
mousex_start = 0
mousex_end = 0
mousey_start = 0
mousey_end = 0
mouse_num = 1

mapx = 0
mapy = 0

##################################################

# 이벤트 루프
running = True
while running:
    dt = clock.tick(60) # fps
    screen.fill((0, 0, 0))

    for event in pygame.event.get():

        # 종료
        if event.type == pygame.QUIT:
            running = False

        # 마우스
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_num = 0
            mousex_start = pygame.mouse.get_pos()[0]
            mousey_start = pygame.mouse.get_pos()[1]
        
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_num = 1
            mapx += mousex_end - mousex_start
            mapy += mousey_end - mousey_start
            mousex_end = mousex_start = 0
            mousey_end = mousey_start = 0

    # 마우스 현재 위치
    if mouse_num == 0:
        mousex_end = pygame.mouse.get_pos()[0]
        mousey_end = pygame.mouse.get_pos()[1]

##################################################

    # 화면
    screen.blit(background, (mapx + mousex_end - mousex_start, mapy + mousey_end - mousey_start))
    pygame.draw.circle(screen, P_BLUE, [320 + mapx + mousex_end - mousex_start, 240 + mapy + mousey_end - mousey_start], 10, 3)

    pygame.display.update()

pygame.quit()
