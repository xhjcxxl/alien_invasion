import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import GameStats
from alien import Alien
import game_functions as gf


def main_run_game():
    # 初始化游戏并创建一个屏幕
    pygame.init()
    # 创建一个setting类的实例 对于整个游戏的设置
    ai_settings = Settings()

    # 对screen进行设置
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.title)

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 飞船的实例，就是那张图片 然后用ship来进行控制
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建 外星人 的编组 用于存储外星人
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            # 更新飞船位置
            ship.update()

            # 更新子弹
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            # 更新外星人
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        # 每次循环时都重新绘制屏幕
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


# 运行游戏主程序
main_run_game()
