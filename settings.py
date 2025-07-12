class Settings():
    """A class to store all settings for alien invasion.
    """

    def __init__(self):
        """Initialize the game's settings.
        """

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 300 # testing mode
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Ship settings
        self.ship_speed = 1.5

        # Screen settings
        self.screen_width = 1000
        self.screen_height = 650
        self.bg_color = (130, 200, 229)
        self.game_title = "Alien Invasion"

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right, -1 represents left.
        self.fleet_direction = 1
