class Settings():
    """ 存储 外星人入侵 的所有设置的类 """

    def __init__(self):

        self.screen_width = 900
        self.screen_hight = 600
        # 设置背景颜色 RGB 0-255
        self.bg_color = (230, 230, 230)
        self.title = "Alien Invasion"
        self.ship_speed_factor = 1.5