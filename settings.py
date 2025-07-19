class Settings():
    """A class to store all settings for alien invasion.
    """

    def __init__(self):
        """Initialize the game's settings.
        """
        self.screen_settings()
        self.bullet_settings()
        self.initialize_dynamic_settings()

        # Ship settings
        self.ship_limit = 3 

        # Alien settings
        self.fleet_drop_speed = 10 # determind the speed of the aliens
        
        # How quickly the game speed up
        self.speedup_scale = 1.1

        # How quickly the alien point values increase
        self.score_scale = 1.5

    def screen_settings(self):
        """Set the screen settings"""
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 650
        self.bg_color = (230, 230, 230)
        self.game_title = "Alien Invasion"

        
    def bullet_settings(self):
        """Set the bullet settings"""
        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3


    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game.
        """
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 0.8

        # Scoring 
        self.alien_points = 50

        # fleet_direction of 1 represents right, -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale) # increase the score point when the game increase
    
        
    def medium_speed(self):
        """Medium speed settings"""
        self.ship_speed = 1.7
        self.bullet_speed = 3.2
        self.alien_speed = 1.2

        # Scoring
        self.alien_points = 75

        # fleet_direction of 1 represents right, -1 represents left.
        self.fleet_direction = 1

    def hard_speed(self):
        """Hard speed settings"""
        self.ship_speed = 1.9
        self.bullet_speed = 3.0
        self.alien_speed = 1.4

        # Scoring
        self.alien_points = 100

        # fleet_direction of 1 represents right, -1 represents left.
        self.fleet_direction = 1
