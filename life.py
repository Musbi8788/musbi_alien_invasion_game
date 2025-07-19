import pygame
from pygame.sprite import Sprite


class Life(Sprite):
    """A class to manage the heart.
    """

    def __init__(self, ai_game):
        """Initialize the heart and set it starting position.

        Args:
            ai_game (_type_): _description_
        """
        super().__init__()
        
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the image and get it rect
        self.image = pygame.image.load('images/heart.bmp')
        self.rect = self.image.get_rect()

        # Start each new heart at the bottom center on the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the heart's horizontal position.
        self.x = float(self.rect.x)


    
    def blitme(self):
        """Draw the heart at it current location.
        """
        self.screen.blit(self.image, self.rect)

