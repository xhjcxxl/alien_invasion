class Settings():
    """ 存储 外星人入侵 的所有设置的类 """

    def __init__(self):
        # 整个窗口设置
        self.screen_width = 900
        self.screen_hight = 600

        # 设置背景颜色 RGB 0-255
        self.bg_color = (230, 230, 230)
        self.title = "Alien Invasion"

        # 飞船移动速度
        self.ship_speed_factor = 1.5

        # 子弹设置
        self.bullet_speed_factor = 0.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3