class Settings():
    """A class to store all settings for alien invasion.
    """

    def __init__(self):
        """Initialize the game's settings.
        """

        # Bullet settings
        self.bullet_width = 3 
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Ship settings
        self.ship_limit = 3 

        # Screen settings
        self.screen_width = 1000
        self.screen_height = 650
        self.bg_color = (230, 230, 230)
        self.game_title = "Alien Invasion"

        # Alien settings
        self.fleet_drop_speed = 10 # determind the speed of the aliens
        

        # How quickly the game speed up
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game.
        """
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet_direction of 1 represents right, -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
