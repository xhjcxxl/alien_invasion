class Settings():
    """ 存储 外星人入侵 的所有设置的类 """

    def __init__(self):
        """ 初始化游戏设置 静态设置 整个游戏过程中不变"""
        # 整个窗口设置
        self.screen_width = 900
        self.screen_height = 600

        # 设置背景颜色 RGB 0-255
        self.bg_color = (230, 230, 230)
        self.title = "Alien Invasion"

        # 飞船设置
        self.ship_limit = 3

        # 外星人设置
        self.fleet_drop_speed = 4

        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3

        # 怎样的速度加快游戏节奏
        self.speedup_scale = 1.1
        # 外星人点数的提高速度
        self.score_scale = 1.5

        # 游戏初始化设置 动态设置 重新开始游戏恢复默认
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ 初始化随游戏进行而变化的设置"""
        # 飞船 外星人 子弹 速度
        self.ship_speed_factor = 1.0
        self.alien_speed_factor = 0.15
        self.bullet_speed_factor = 0.7
        # 外星人 方向 1向右 -1向左
        self.fleet_direction = 1

        # 记分
        self.alien_points = 50

    def increase_speed(self):
        """ 提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)