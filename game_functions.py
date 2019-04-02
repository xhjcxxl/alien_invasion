import sys
import pygame
from bullet import Bullet


# 动作按下集合
def down_key_events(key_event, ai_settings, screen, ship, bullets):
    if key_event == pygame.K_RIGHT:
        ship.moving_right = True
    elif key_event == pygame.K_LEFT:
        ship.moving_left = True
    elif key_event == pygame.K_DOWN:
        ship.moving_down = True
    elif key_event == pygame.K_UP:
        ship.moving_up = True
    elif key_event == pygame.K_SPACE:
        fire_buttel(ai_settings, screen, ship, bullets)


def fire_buttel(ai_settings, screen, ship, bullets):
    """如果子弹没有达到限制，就创建子弹 并添加到编组中"""
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

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
def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            down_key_events(event.key, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            up_key_events(event.key, ship)


def update_screen(ai_settings, screen, ship, bullets):
    # 每次循环时都重新绘制 飞船
    screen.fill(ai_settings.bg_color)
    # 每次循环时都重新绘制 子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    # 让最近绘制的屏幕可见, 更新屏幕
    pygame.display.flip()


def update_bullets(bullets):
    """更新子弹位置，删除已经消失的子弹"""
    bullets.update()

    # 删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
