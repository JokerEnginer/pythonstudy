import pygame
from pygame.locals import *
import random
import time
class BasePlane(object):
    def __init__(self, screen, x, y, image):
        self.screen = screen
        self.x = x
        self.y =y
        self.image = pygame.image.load(image)
        self.bullet_list = []

    def show(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullet_list:
            bullet.show()
            bullet.move()
            if bullet.judge_border():
                self.bullet_list.remove(bullet)

class BaseBullet(object):
    def __init__(self, screen, x, y, image):
        self.x = x + 40
        self.y = y - 20
        self.screen = screen
        self.image = pygame.image.load(image)

    def show(self):
        self.screen.blit(self.image, (self.x, self.y))


class HeroBullet(BaseBullet):
    def __init__(self, screen, x, y):
        super(HeroBullet, self).__init__(screen, x, y-20, r"F:\pythonstudy\feiji\bullet.png")

    def move(self):
        self.y -= 5

    def judge_border(self):
        if self.y < 0:
            return True
        else:
            return False

class EnemyBullet(BaseBullet):
    def __init__(self,screen, x, y):
        super(EnemyBullet, self).__init__(screen, x+20, y+35, r"F:\pythonstudy\feiji\bullet1.png")

    def move(self):
        self.y += 5

    def judge_border(self):
        if self.y > 630:
            return True
        else:
            return False

class HeroPlane(BasePlane):
    def __init__(self, screen):
        # 调用父类构造方法
        super().__init__(screen, 200,  500, r"F:\pythonstudy\feiji\hero1.png")
    def move_left(self):
        self.x -= 2

    def move_right(self,):
        self.x += 2

    def fire(self):
        self.bullet_list.append(HeroBullet(self.screen, self.x, self.y))

class EnemyPlane(BasePlane):
    def __init__(self,screen):
        super().__init__(screen, 200, 40, r"F:\pythonstudy\feiji\enemy0.png")
        self.direction = "right"

    def fire(self):
        random_num = random.randint(1, 100)
        if random_num == 9 or random_num == 50:
            self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y))

    def move(self):
        if self.direction == "right":
            self.x += 2
            if self.x > 430:
                self.direction = "left"
        elif self.direction == "left":
            self.x -= 2
            if self.x < 0:
                self.direction = "right"


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
    # 创建敌人飞机对象
    enemy_plane = EnemyPlane(screen)
    # 4.将背景放置在窗口
    while True:
        screen.blit(background, (0, 0))
        player_plane.show()
        enemy_plane.show()
        enemy_plane.move()
        enemy_plane.fire()
        key_judge(player_plane)


        # 更新显示的内容
        pygame.display.update()

        time.sleep(0.01)


if __name__ == '__main__':
    main()