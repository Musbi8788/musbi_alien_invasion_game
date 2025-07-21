import pygame 
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet.
    """

    def __init__(self, ai_game):
        """Initialize the alien and set it starting position.
        """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Alien image
        self.alien_image()
    
    def alien_image(self):
        """Respond for the alien images"""

        # Load the image and set it rect attributes
        self.image = pygame.image.load("images/alien1.bmp")
        
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen
        """
        # get the screen rect 
        screen_rect = self.screen.get_rect()

        # checking the alien fleet position in the screen
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        
    def update(self):
        """Move the alien left or right
        """
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x # update position of the alien rect



