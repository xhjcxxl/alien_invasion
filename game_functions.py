import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


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
        fire_bullet(ai_settings, screen, ship, bullets)
    elif key_event == pygame.K_q:
        sys.exit()


def fire_bullet(ai_settings, screen, ship, bullets):
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


def check_events(ai_settings, screen, stats, play_button, ship, bullets):
    """ 监视键盘和鼠标事件 """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            down_key_events(event.key, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            up_key_events(event.key, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y)


def check_play_button(stats, play_button, mouse_x, mouse_y):
    """ 玩家单击Play 按钮时开始新游戏 """
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        stats.game_active = True


def update_screen(ai_settings, screen, stats, ship, aliens, bullets,
                  play_button):
    # 先绘制 屏幕 背景颜色
    screen.fill(ai_settings.bg_color)
    # 绘制 子弹编组中的每一个子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 绘制 飞船
    ship.blitme()
    # 绘制 外星人
    aliens.draw(screen)
    # 如果游戏处于非活动状态，就绘制 Play按钮
    if not stats.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕可见, 显示到屏幕上去
    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """更新子弹位置，删除已经消失的子弹"""
    bullets.update()

    # 删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    # 检查是否有子弹击中了外星人
    # 如果 是 就删除对应的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    # 如果外星人群为空，就生成新的外星人群
    if len(aliens) == 0:
        # 删除现有的子弹并新建一群外星人
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)
        if ai_settings.alien_speed_factor < 0.5:
            ai_settings.alien_speed_factor += 0.1
        else:
            ai_settings.fleet_drop_speed += 5


def get_number_aliens_x(ai_settings, alien_width):
    """ 计算每行可以容纳多少个外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_aliens_y(ai_settings, ship_height, alien_height):
    """ 计算屏幕可以容纳多少行外星人"""
    available_space_y = (ai_settings.screen_height -
                         (3 * alien_height) - ship_height)
    number_aliens_y = int(available_space_y / (2 * alien_height))
    return number_aliens_y


def creat_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建一个外星人 并放入当前行"""
    # 创建外星人实例
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    # 添加外星人到编组当中
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """ 创建外星人实例 要用到 飞船高度，外星人高度，屏幕，设置等参数"""
    alien = Alien(ai_settings, screen)
    # 计算个数
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_aliens_y = get_number_aliens_y(ai_settings, ship.rect.height,
                                          alien.rect.height)

    # 有多少行
    for row_number in range(number_aliens_y):
        # 创建第一行外星人 一行多个
        for alien_number in range(number_aliens_x):
            # 创建外星人并加入到外星人编组当中
            creat_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    """ 有外星人到达边缘时进行相应的处理 """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """ 将整个外星人群下移，并改变它们的方向 """
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """ 更新外星人数据 """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # 检测外星人和飞船之间的碰撞
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """ 响应被外星人撞到的飞船 """
    if stats.ships_left > 0:
        # 将ships_left -= 1
        stats.ships_left -= 1

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新外星人，并将飞船放到屏幕底端中央（重置到初始位置）
        ship.center_ship()
        create_fleet(ai_settings, screen, ship, aliens)

        # 暂停
        sleep(0.5)
    else:
        stats.game_active = False


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """ 检查是否有外星人到达了屏幕底端 """
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 像飞船被撞到了一样进行处理
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break
