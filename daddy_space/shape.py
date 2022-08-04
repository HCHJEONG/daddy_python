import pygame
from math import pi

# 초기화
pygame.init()

# 화면 크기
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# 타이틀, 아이콘
pygame.display.set_caption("Polygon")

# FPS
clock = pygame.time.Clock()

# 폰트
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트, 크기)

# 색 상수
P_BLUE = (147, 214, 237)

##################################################

# 이벤트 루프
running = True
while running:
    dt = clock.tick(10) # fps

    for event in pygame.event.get():
        # 종료
        if event.type == pygame.QUIT:
            running = False

    # 화면
    screen.fill((255, 255, 255))

    # 사각형 (화면, 색상, [왼쪽 위 꼭짓점, 가로 길이, 세로 길이], 아웃라인의 두께)
    pygame.draw.rect(screen, P_BLUE, [0, 0, 50, 20])
    pygame.draw.rect(screen, P_BLUE, [50, 20, 50, 20], 10)

    # 삼각형 (화면, 색상, [꼭짓점 3개], 아웃라인의 두께)
    pygame.draw.polygon(screen, P_BLUE, [[590,0], [640, 0], [640, 50]])
    pygame.draw.polygon(screen, P_BLUE, [[0,430], [0, 480], [50, 480]], 10)

    # 원 (화면, 색상, 중심, 반지름, 아웃라인의 두께)
    pygame.draw.circle(screen, P_BLUE, [250, 240], 10)
    pygame.draw.circle(screen, P_BLUE, [390, 240], 10, 5)

    # 부채꼴 (화면, 색상, [둘러싸는 사각형의 왼쪽 위 꼭짓점, 가로 길이, 세로 길이], 시작 각도, 끝 각도, 아웃라인의 두께)
    pygame.draw.arc(screen, P_BLUE, [230, 220, 100, 100], 0, pi/3, 1)
    pygame.draw.arc(screen, P_BLUE, [230, 220, 100, 100], pi/2, pi, 2)
    pygame.draw.arc(screen, P_BLUE, [230, 220, 40, 40], 21*pi/20, 39*pi/20, 2)

    # 타원 (화면, 색상, [둘러싸는 사각형의 왼쪽 위 꼭짓점, 가로 길이, 세로 길이], 아웃라인의 두께)
    pygame.draw.ellipse(screen, P_BLUE, [100, 0, 50, 30])
    pygame.draw.ellipse(screen, P_BLUE, [150, 2, 50, 30], 5)


    pygame.display.update()

pygame.quit()