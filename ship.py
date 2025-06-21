import pygame

class Ship():
    """A class to manage the ship.
    """

    def __init__(self, ai_game):
        """Initialize the ship and set it starting position.

        Args:
            ai_game (_type_): _description_
        """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the image and get it rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center on the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at it current location.
        """
        self.screen.blit(self.image, self.rect)