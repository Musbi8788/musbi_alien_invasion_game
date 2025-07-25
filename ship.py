import pygame


class Ship:
    """A class to manage the ship.
    """

    def __init__(self, ai_game):
        """Initialize the ship and set it starting position.

        Args:
            ai_game (_type_): _description_
        """

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the image and get it rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center on the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        # Movement Flag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Update the ship's position based on the movement flag.
        """
        # update the ship's x value not the self.rect
        if self.moving_right and self.rect.right < self.screen_rect.right: 
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x
        self.rect.x = int(self.x) # converted to int

    def blitme(self):
        """Draw the ship at it current location.
        """
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

