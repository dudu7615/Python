import random
import sys
import time as t

import config
from files import PixMap
from pygame import *


class Main:
    """游戏主类"""

    def __init__(self):
        self.initGame()
        self.startGame()

    @classmethod
    def initGame(cls):
        cls.bulletList: list[Bullet] = []
        cls.explodeList: list[Explode] = []
        cls.enemyTankList: list[EnemyTank] = []
        cls.wallList: list[Wall] = []

    @classmethod
    def startGame(cls):
        """开始游戏"""
        display.init()
        # 设置窗口大小
        cls.window = display.set_mode((config.WIDTH, config.HEIGHT))
        # 设置窗口标题
        cls.setText("坦克大战")
        # 实例化我方坦克
        cls.myTank = Tank(200, 200)
        # 实例化敌方坦克

        for _ in range(config.ENEMY_TANK_NUM):
            cls.enemyTankList.append(EnemyTank())

        # 实例化墙
        for _ in range(config.WALL_NUM):
            cls.wallList.append(Wall())

        while True:
            # 设置背景颜色
            cls.window.fill(Color(0, 0, 0))
            # 获取事件
            cls.getEvent()
            # 设置文字
            cls.window.blit(cls.setText(f"剩余敌方坦克{len(cls.enemyTankList)}"), (5, 5))
            # 检测我方坦克是否存活
            if cls.myTank.life:
                # 显示我方坦克
                cls.myTank.display()
                # 使我方坦克移动
                if not cls.myTank.stop:
                    cls.myTank.move()

            # 显示敌方坦克并发射子弹
            for enemyTank in cls.enemyTankList:
                if not enemyTank.life:
                    cls.enemyTankList.remove(enemyTank)
                    continue
                enemyTank.display()
                if not enemyTank.stop:
                    enemyTank.move()

                if bullet := enemyTank.fire():
                    cls.bulletList.append(bullet)

            # 显示子弹
            for bullet in cls.bulletList:
                if bullet.flag:
                    bullet.display()
                else:
                    cls.bulletList.remove(bullet)

            # 显示爆炸效果
            for explode in cls.explodeList:
                if explode.life:
                    explode.display()
                else:
                    cls.explodeList.remove(explode)

            # 显示墙
            for wall in cls.wallList:
                if wall.life:
                    wall.display()
                else:
                    cls.wallList.remove(wall)
            # 刷新窗口
            t.sleep(0.03)
            display.update()

    @classmethod
    def getEvent(cls):
        """获取事件"""
        eventList = event.get()
        if len(cls.enemyTankList) == 0 or not cls.myTank.life:
            cls.window.blit(
                cls.setText("游戏结束"), (config.WIDTH // 2, config.HEIGHT // 2)
            )
        for e in eventList:
            if e.type == QUIT:
                cls.overGame()
            elif e.type == KEYDOWN:
                if e.key == K_LEFT:
                    cls.myTank.direction = "L"
                    cls.myTank.stop = False
                elif e.key == K_RIGHT:
                    cls.myTank.direction = "R"
                    cls.myTank.stop = False
                elif e.key == K_UP:
                    cls.myTank.direction = "U"
                    cls.myTank.stop = False
                elif e.key == K_DOWN:
                    cls.myTank.direction = "D"
                    cls.myTank.stop = False
                elif e.key == K_ESCAPE:
                    cls.createMyTank()
                elif e.key == K_SPACE:
                    if cls.myTank.life:
                        cls.bulletList.append(cls.myTank.fire())
            elif e.type == KEYUP:
                if e.key == K_LEFT:
                    cls.myTank.direction = "L"
                    cls.myTank.stop = True
                elif e.key == K_RIGHT:
                    cls.myTank.direction = "R"
                    cls.myTank.stop = True
                elif e.key == K_UP:
                    cls.myTank.direction = "U"
                    cls.myTank.stop = True
                elif e.key == K_DOWN:
                    cls.myTank.direction = "D"
                    cls.myTank.stop = True

    @classmethod
    def createMyTank(cls):
        """创建我方坦克"""
        cls.myTank.life = True

    @classmethod
    def setText(cls, text: str):
        """设置文字"""
        # 初始化字体模块
        font.init()
        # 获取字体对象
        infoFont = font.SysFont("kaiti", 20)
        return infoFont.render(text, True, Color(255, 0, 0))

    @classmethod
    def overGame(cls):
        """结束游戏"""
        sys.exit()


class Tank(sprite.Sprite):
    """坦克"""

    def __init__(self, x: int, y: int):# 主类对象
        self.images = {
            "U": image.load(PixMap(":/img/tank/my/U.png")),
            "D": image.load(PixMap(":/img/tank/my/D.png")),
            "L": image.load(PixMap(":/img/tank/my/L.png")),
            "R": image.load(PixMap(":/img/tank/my/R.png")),
        }
        self.direction = "U"  # 坦克方向
        self.image = self.images[self.direction]
        self.stop = True  # 坦克是否停止
        self.life = True  # 坦克是否存活

        # 设置坦克位置
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        # 坦克速度
        self.speed = 5

    def move(self):
        """坦克移动"""
        if self.hitWall() or self.hitOtherTank():
            return
        match self.direction:
            case "U":
                if self.rect.y > 0:
                    self.rect.y -= self.speed
            case "D":
                if self.rect.y < Main.window.get_height() - self.rect.height:
                    self.rect.y += self.speed
            case "L":
                if self.rect.x > 0:
                    self.rect.x -= self.speed
            case "R":
                if self.rect.x < Main.window.get_width() - self.rect.width:
                    self.rect.x += self.speed

    def fire(self):
        """坦克开火"""
        return Bullet(self)

    def hitWall(self):
        """坦克撞墙"""
        for wall in Main.wallList:
            if sprite.collide_rect(self, wall):
                match self.direction:
                    case "U":
                        self.rect.y += self.speed
                    case "D":
                        self.rect.y -= self.speed
                    case "L":
                        self.rect.x += self.speed
                    case "R":
                        self.rect.x -= self.speed

                return True
        return False

    def hitOtherTank(self):
        """碰撞其他坦克"""
        for tank in Main.enemyTankList:
            if tank != self and sprite.collide_rect(self, tank):
                match self.direction:
                    case "U":
                        self.rect.y += self.speed
                    case "D":
                        self.rect.y -= self.speed
                    case "L":
                        self.rect.x += self.speed
                    case "R":
                        self.rect.x -= self.speed
                return True
            if self in Main.enemyTankList and sprite.collide_rect(self, Main.myTank):
                return True
        return False

    def display(self):
        """坦克显示"""
        # 重设图片
        self.image = self.images[self.direction]
        # 显示坦克
        Main.window.blit(self.image, self.rect)
        # 检测坦克是否撞墙
        self.hitWall()


class EnemyTank(Tank):
    """敌方坦克"""

    def __init__(self):
        # 随机坐标

        x = random.randint(0, config.WIDTH - config.TANK_WIDTH)
        y = random.randint(0, config.HEIGHT - config.TANK_HEIGHT)
        super().__init__(x, y)
        self.stop = False  # 坦克始终可以移动
        self.step = 0  # 初始化步数
        self.bulletStep = 0  # 子弹发射前的步数
        
        self.images = {
            "U": image.load(PixMap(":/img/tank/enemy/U.png")),
            "D": image.load(PixMap(":/img/tank/enemy/D.png")),
            "L": image.load(PixMap(":/img/tank/enemy/L.png")),
            "R": image.load(PixMap(":/img/tank/enemy/R.png")),
        }
        # 随机方向
        self.direction = random.choice(["U", "D", "L", "R"])

    def move(self):
        """敌方坦克移动（随机数决定）"""
        if self.step == 0:
            self.direction = random.choice(["U", "D", "L", "R"])
            self.step = random.randint(10, 50)

        super().move()
        self.step -= 1  # 步数减一
        self.bulletStep -= 1  # 子弹步数减一

    def fire(self):
        """敌方坦克开火"""
        if self.bulletStep > 0:
            return None
        self.bulletStep = random.randint(20, 50)

        return EnemyBullet(self)


class Bullet(sprite.Sprite):
    """子弹"""

    def __init__(self, tank: Tank):
        self.image = image.load(PixMap(":/img/bullet/my.png"))
        self.tank = tank  # 坦克对象
        self.direction = tank.direction  # 子弹和坦克方向一致
        # 设置子弹位置
        self.rect = self.image.get_rect()

        self.speed = 20  # 子弹速度
        self.flag = True  # 子弹是否存在

        match self.direction:
            case "U":
                self.rect.x = tank.rect.x + tank.rect.w // 2 - self.rect.w // 2
                self.rect.y = tank.rect.y
            case "D":
                self.rect.centerx = tank.rect.centerx
                self.rect.y = tank.rect.bottom
            case "L":
                self.rect.x = tank.rect.x
                self.rect.centery = tank.rect.centery
            case "R":
                self.rect.x = tank.rect.right
                self.rect.centery = tank.rect.centery

    def move(self):
        """子弹移动"""
        match self.direction:
            case "U":
                if self.rect.y > 0:
                    self.rect.y -= self.speed

            case "D":
                if self.rect.y < Main.window.get_height():
                    self.rect.y += self.speed

            case "L":
                if self.rect.x > 0:
                    self.rect.x -= self.speed

            case "R":
                if self.rect.x < Main.window.get_width():
                    self.rect.x += self.speed

    def display(self):
        """子弹显示"""
        if (
            self.rect.x <= 0
            or self.rect.y <= 0
            or self.rect.x >= Main.window.get_width()
            or self.rect.y >= Main.window.get_height()
        ):
            self.flag = False
        if self.flag:
            Main.window.blit(self.image, self.rect)

            self.move()
            self.hitEnemyTank(Main.enemyTankList)
            self.hitMyTank()
            self.hitWall()

    def hitEnemyTank(self, enemyTankList: list[EnemyTank]):
        """子弹击中敌方坦克"""
        if self.tank not in Main.enemyTankList:
            for enemyTank in enemyTankList:
                if sprite.collide_rect(self, enemyTank):
                    self.flag = False
                    enemyTank.life = False
                    # 显示爆炸效果
                    Main.explodeList.append(Explode(Main.window, enemyTank))

    def hitMyTank(self):
        """子弹击中我方坦克"""
        if sprite.collide_rect(self, Main.myTank):
            self.flag = False
            Main.myTank.life = False
            # 显示爆炸效果
            ex = Explode(Main.window, Main.myTank)
            for _ in range(4):
                ex.display()
                t.sleep(0.1)

    def hitWall(self):
        """子弹击中墙"""
        for wall in Main.wallList:
            if sprite.collide_rect(self, wall):
                self.flag = False
                wall.hp -= 1
                if wall.hp == 0:
                    wall.life = False


class EnemyBullet(Bullet):
    """敌方子弹"""

    def __init__(self, tank: Tank):
        super().__init__(tank)
        self.image = image.load(PixMap(":/img/bullet/enemy.png"))


class Explode:
    """爆炸效果"""

    def __init__(self, window: Surface, tank: Tank):
        self.window = window
        self.rect = tank.rect
        self.life = True  # 爆炸效果是否存在

        self.step = 0

        self.images = [
            image.load(PixMap(":/img/explode/1.png")),
            image.load(PixMap(":/img/explode/2.png")),
            image.load(PixMap(":/img/explode/3.png")),
            image.load(PixMap(":/img/explode/4.png")),
        ]

    def display(self):
        """显示爆炸效果"""
        if self.step < len(self.images):
            self.image = self.images[self.step]
            self.window.blit(self.image, self.rect)
            self.step += 1
        else:
            self.life = False


class Wall(sprite.Sprite):
    def __init__(self):

        self.image = image.load(PixMap(":/img/wall.png"))
        self.rect = self.image.get_rect()

        # 设置生命值，是否展示
        self.life = True
        self.hp = 3

    def create(self):
        xList = list(range(0, config.WIDTH, self.rect.w))
        yList = list(range(0, config.HEIGHT, self.rect.h))
        self.rect.x = random.choice(xList)
        self.rect.y = random.choice(yList)


    def display(self):
        """显示墙"""
        if self.life:
            walls = Main.wallList[:Main.wallList.index(self)]
            for wall in walls:
                if sprite.collide_rect(self, wall):
                    self.create()
                    
            Main.window.blit(self.image, self.rect)


if __name__ == "__main__":
    Main()
