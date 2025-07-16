import pygame.font # .font allow pygame to render text on the screen

class Button:
    """ A Class to Create the Start Button
    """

    def __init__(self, ai_game, msg):
        """Initialize the button attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimenson and properties the of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message need to be prepped only once
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Trun msg into a rendered image and center text on the button."""

        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw blank button and then draw message"""
        self.screen.fill(self.button_color, self.rect) # draw the rectange 
        self.screen.blit(self.msg_image, self.msg_image_rect) # draw the text image