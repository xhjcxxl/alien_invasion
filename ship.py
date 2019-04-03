import pygame


class Ship:

    def __init__(self, ai_settings, screen):
        self.screen = screen

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 飞船位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.ai_settings = ai_settings
        self.center_FL = float(self.rect.centerx)
        self.center_UD = float(self.rect.bottom)

        # 飞船动作开关
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        """ 在指定位置绘制飞船图片 """
        self.screen.blit(self.image, self.rect)

    def update(self):
        # 先对参数坐标进行调整 rect就是 飞船(ship那张图片) 可以看做是边界
        # screen 就是整个窗口，窗口也有自己的screen_rect 可以看做是边界
        # right 是 rect的右边界
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center_FL += self.ai_settings.ship_speed_factor
        # left 是 rect的左边界
        if self.moving_left and self.rect.left > 0:
            self.center_FL -= self.ai_settings.ship_speed_factor
        # bottom 是 rect的底边界
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center_UD += self.ai_settings.ship_speed_factor
        # top 是 rect的顶边界
        if self.moving_up and self.rect.top > 0:
            self.center_UD -= self.ai_settings.ship_speed_factor
        # 给飞船赋坐标
        self.rect.centerx = self.center_FL
        self.rect.bottom = self.center_UD