import pygame

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

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ship)

        # 更新飞船位置
        ship.update()

        # 每次循环时都重新绘制屏幕
        gf.update_screen(ai_settings, screen, ship)


run_game()
