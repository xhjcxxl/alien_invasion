import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化游戏并创建一个屏幕
    pygame.init()
    # 创建一个setting类的实例 对于整个游戏的设置
    ai_settings = Settings()

    # 对screen进行设置
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_hight))
    pygame.display.set_caption(ai_settings.title)

    # 飞船的实例，就是那张图片 然后用ship来进行控制
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)

        # 更新飞船位置
        ship.update()

        # 更新子弹
        gf.update_bullets(bullets)

        # 每次循环时都重新绘制屏幕
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
