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

        # Load the image and set it rect attributes
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # Start each new alien near the top of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)
    
    def update(self):
        """Move the alien to right 
        """
        self.x += self.settings.alien_speed # Make alien move
        self.rect.x = self.x # update position of the alien rect



