import sys
import pygame



# 动作按下集合
def down_key_events(key_event, ship):
    if key_event == pygame.K_RIGHT:
        ship.moving_right = True
    elif key_event == pygame.K_LEFT:
        ship.moving_left = True
    elif key_event == pygame.K_DOWN:
        ship.moving_down = True
    elif key_event == pygame.K_UP:
        ship.moving_up = True


# 动作松开集合
def up_key_events(key_event, ship):
    if key_event == pygame.K_RIGHT:
        ship.moving_right = False
    elif key_event == pygame.K_LEFT:
        ship.moving_left = False
    elif key_event == pygame.K_DOWN:
        ship.moving_down = False
    elif key_event == pygame.K_UP:
        ship.moving_up = False


# 监视键盘和鼠标事件
def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            down_key_events(event.key, ship)
        elif event.type == pygame.KEYUP:
            up_key_events(event.key, ship)


def update_screen(ai_settings, screen, ship):
    # 每次循环时都重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # 让最近绘制的屏幕可见, 更新屏幕
    pygame.display.flip()
