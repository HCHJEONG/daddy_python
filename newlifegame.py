import pygame
from random import *

# 초기화
pygame.init()

# 화면 크기
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# 타이틀, 아이콘
pygame.display.set_caption("Evolution")

# FPS
clock = pygame.time.Clock()

# 폰트
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트, 크기)

# 색
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
P_BLUE = (147, 214, 237)
RED = (255, 0, 0)

tilesize = 25
tilenumber = 16

size = 7
life = 20
death = 2
initbirthrate = 0.6
birthrate = 0.5
birthrestrict = 1.5

entity_list= []
##################################################

class Dots():
    def __init__(self, loc, life, color, leaping):
        self.loc = loc
        self.life = life
        self.color = color
        self.leaping = leaping


    def move(self):
        if self.color == P_BLUE:
            self.color = WHITE
        else:
            num = randrange(4)
            if num == 0:
                if self.loc[0] + self.leaping > tilenumber:
                    self.loc[0] = tilenumber
                else:
                    self.loc[0] = self.loc[0] + self.leaping
            if num == 1:
                if self.loc[0] - self.leaping < 0:
                    self.loc[0] = 0
                else:
                    self.loc[0] = self.loc[0] - self.leaping
            if num == 2:
                if self.loc[1] + self.leaping > tilenumber:
                    self.loc[1] = tilenumber
                else:
                    self.loc[1] = self.loc[1] + self.leaping
            if num == 3:
                if self.loc[1] - self.leaping < 0:
                    self.loc[1] = 0
                else:
                    self.loc[1] = self.loc[1] - self.leaping

    def draw(self):
        pygame.draw.circle(screen, self.color, \
        [screen_width/2 - tilesize*(tilenumber/2-self.loc[0]), screen_height/2 - tilesize*(tilenumber/2-self.loc[1])], size)

for m in range(0, tilenumber):
    for n in range(0, tilenumber):
        if random() > 0.5:
            if random() > initbirthrate:
                entity_list.append(Dots([m, n], life, WHITE, 1))
        else:
            if random() > initbirthrate:
                entity_list.append(Dots([m, n], life, RED, 2))
##################################################

# 이벤트 루프
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        mouse = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (mouse[0] - 50)**2 + (mouse[1] - 50)**2 <= 900:
                for entt in entity_list:
                    entt.life = entt.life - death
                    if entt.life <= 0:
                        entity_list.remove(entt)
                    
                    entt.move()
                    
                i = len(entity_list)
                for m in range(i - 1):
                    for n in range(m + 1, i):
                        if entity_list[m].loc == entity_list[n].loc and random() > birthrate and len(entity_list) < tilenumber*tilenumber/birthrestrict:
                            if entity_list[m].color == RED and entity_list[n].color == RED:
                                x = entity_list[m].loc[0]
                                y = entity_list[m].loc[1]
                                entity_list.append(Dots([x, y], life, RED, 2))

                            if entity_list[m].color == RED and entity_list[n].color == WHITE:
                                x = entity_list[m].loc[0]
                                y = entity_list[m].loc[1]
                                if random() > 0.5:
                                    entity_list.append(Dots([x, y], life, RED, 2))
                                else:
                                    entity_list.append(Dots([x, y], life, WHITE, 1))
                            if entity_list[m].color == WHITE and entity_list[n].color == WHITE:
                                x = entity_list[m].loc[0]
                                y = entity_list[m].loc[1]
                                entity_list.append(Dots([x, y], life, RED, 2))


##################################################

    screen.fill(BLACK)

    # world_time 버튼
    pygame.draw.circle(screen, WHITE, [50, 50], 30)

    # 그리드
    for m in range(0, tilesize*tilenumber + 1, tilesize):
        pygame.draw.line(screen, WHITE, [screen_width/2 - tilesize*tilenumber/2 + m, screen_height/2 - tilesize*tilenumber/2], [screen_width/2 - tilesize*tilenumber/2 + m, screen_height/2 + tilesize*tilenumber/2], 1)
    for n in range(0, tilesize*tilenumber + 1, tilesize):
        pygame.draw.line(screen, WHITE, [screen_width/2 - tilesize*tilenumber/2, screen_height/2 - tilesize*tilenumber/2 + n], [screen_width/2 + tilesize*tilenumber/2, screen_height/2 - tilesize*tilenumber/2 + n], 1)

    # 개체
    for entity in entity_list:
        if entity.life > 0:
            entity.draw()

    pygame.display.update() # 화면 다시 그리기

##################################################

# 종료
pygame.quit()

##################################################

# 결론 : 빨간 개체가 흰 개체보다 생존에 있어서 우월하다.
# 이유 : 활동력이 높다는 것은 상대적으로 공간이 작아지는 것이다. 따라서 인구밀도 높아지고, 번식에 유리한 것이다.
