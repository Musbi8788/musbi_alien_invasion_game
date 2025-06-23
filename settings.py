class Settings():
    """A class to store all settings for alien invasion.
    """

    def __init__(self):
        """Initialize the game's settings.
        """
        # Ship settings
        self.ship_speed = 1.5

        # Screen settings
        self.screen_width = 1000
        self.screen_height = 650
        self.bg_color = (130, 200, 229)
        self.game_title = "Alien Invasion"
