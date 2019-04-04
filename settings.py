class Settings():
    """ 存储 外星人入侵 的所有设置的类 """

    def __init__(self):
        # 整个窗口设置
        self.screen_width = 900
        self.screen_height = 600

        # 设置背景颜色 RGB 0-255
        self.bg_color = (230, 230, 230)
        self.title = "Alien Invasion"

        # 飞船设置
        self.ship_speed_factor = 1.0
        self.ship_limit = 3

        # 外星人设置
        self.alien_speed_factor = 0.1
        self.fleet_drop_speed = 2
        self.fleet_direction = 1
        # direction = 1 向右
        # direction = -1 向左

        # 子弹设置
        self.bullet_speed_factor = 0.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3