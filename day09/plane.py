import pygame
from pygame.locals import *
import time

class HeroPlane(object):
    def __init__(self, screen):
        self.x = 200
        self.y =y = 520
        self.screen = screen
        self.image = pygame.image.load(r"F:\pythonstudy\feiji\hero1.png")
        self.bullet_list = []    #  存储子弹对象

    def show(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullet_list:
            bullet.show()

    def move_left(self):
        self.x -= 2

    def move_right(self):
        self.x += 2

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))

class Bullet(object):
    def __init__(self, screen, x, y):
        self.x = x+40
        self.y =y-20
        self.screen = screen
        self.image = pygame.image.load(r"F:\pythonstudy\feiji\bullet.png").convert()

    def show(self):
        self.screen.blit(self.image, (self.x, self.y))


def key_judge(hero_temp):
    for event in pygame.event.get():
        # print(event.type)
        if event.type == QUIT:
            print("exit")
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                # 控制飞机让其向左移动
                hero_temp.move_left()
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                # 控制飞机让其向右移动
                hero_temp.move_right()
            elif event.key == K_SPACE:
                print('space')
                hero_temp.fire()


def main():
    # 1.初始化窗口
    pygame.init()

    # 2.创建窗口
    screen = pygame.display.set_mode((480, 660))
    # 3.创建一个跟窗口一样大小的图片,用来当背景
    background = pygame.image.load(r"F:\pythonstudy\feiji\background.png")
    # 创建玩家飞机对象
    player_plane = HeroPlane(screen)
    # 4.将背景放置在窗口
    while True:
        screen.blit(background, (0, 0))
        player_plane.show()
        key_judge(player_plane)


        # 更新显示的内容
        pygame.display.update()

        time.sleep(0.01)


if __name__ == '__main__':
    main()