# import statements
import sys
from time import sleep

import pygame
import pygame.mixer

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard

from button import Button
from ship import Ship


from bullet import Bullet
from alien import Alien


class AlienInvasion():
    """Overall class to manage the game assets and behavior.
    """

    def __init__(self,):
        """Initialize the game and create game resources.
        """
        # The game resources
        pygame.init()

        self.settings = Settings()

        # # Fullscreen mode
        self.full_screen()

        # Normalscreen mode
        # self.screen = pygame.display.set_mode(
        #     (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption(self.settings.game_title)

        # Create an instance to the stats
        # and create a scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        # Make the bullets and aliens in a pygame group form
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        # Add sound effect
        self.shooting_sfx = pygame.mixer.Sound("./sounds/shooting1.mp3")
        self.ship_sfx = pygame.mixer.Sound("./sounds/ship_hit.mp3")

        # Create the initial fleet of aliens
        self._create_fleet()

        # Make the play buttons level
        self.play_level_buttons()

    def play_level_buttons(self):
        """Respond to the play button levels"""
        # Make the play button
        center_x = 500
        self.easy_button = Button(self, "Easy", center=(
            center_x, 310), color=(78, 181, 135))
        
        self.medium_button = Button(
            self, "Medium", center=(center_x, 390), color=(0, 0, 255))
        
        self.hard_button = Button(self, "Hard", center=(center_x, 470), color=(255, 0, 0))

        self.game_over = Button(self, "Game Over", center=(
            800, 390), color=(200, 100, 255))
        

    def full_screen(self):
        """Create a fullscreen"""
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height


    def run_game(self):
        """Start the main loop for the game
        """
        while True:
            self._check_events()
            #
            if self.stats.game_active:
                self.ship.update()
                self.bullets.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _check_events(self):
        """Respond to keypress and mouse events
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._save_high_score()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:  # check for mouse click
                mouse_pos = pygame.mouse.get_pos()  # get the position of the mouse click
                self._check_play_button(mouse_pos)

    def _start_game(self):
        """Respond to start the game"""
        if not self.stats.game_active:  # Allow player's to start the game if the game is inactive

            # Reset the game statistics
            self.stats.rest_stats()
            self.stats.game_active = True

            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Hide the mouse
            pygame.mouse.set_visible(False)

    def _set_difficulty(self, level):
        """Reponse to the game difficulty
        level: will determine which level you are start on the game.
        """
        if level == "easy":
            self.settings.initialize_dynamic_settings()
        elif level == "medium":
            self.settings.medium_speed()
        elif level == "hard":
            self.settings.hard_speed()

    def collide_button(self, mouse_pos):
        """Respond to collide point for the three button"""
        self.easy_button_clicked = self.easy_button.rect.collidepoint(mouse_pos)

        self.medium_button_clicked = self.medium_button.rect.collidepoint(mouse_pos)

        self.hard_button_clicked = self.hard_button.rect.collidepoint(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks a level"""

        self.collide_button(mouse_pos)

        self.game_levels()

    
    def game_levels(self):
        """Respond to the game levels button."""

        # Only make the button clickable when the game is inactive
        if self.easy_button_clicked and not self.stats.game_active:
            # Reset the game settings
            self._set_difficulty("easy")  # Start from the easy level

            # Rest the game statistics
            self.reset_game_settings()

        # Only make the button clickable when the game is inactive
        elif self.medium_button_clicked and not self.stats.game_active:
            # Reset the game settings
            self._set_difficulty("medium")  # Start from medium level

            # Rest the game statistics
            self.reset_game_settings()


        # Only make the button clickable when the game is inactive
        elif self.hard_button_clicked and not self.stats.game_active:
            # Reset the game settings
            self._set_difficulty("hard")  # Start from the hard level

            # Rest the game statistics
            self.reset_game_settings()


    def reset_game_settings(self):
        """Reponse to resetting the game settings"""
        # Rest the game statistics
        self.stats.rest_stats()
        self.stats.game_active = True
        # Reset the text images
        self.sb.prep_images()
        self._start_game()

        # Show the cursor
        pygame.mouse.set_visible(False)

    def _save_high_score(self):
        """Store the high score in a text file"""
        with open('high_score.txt', 'w') as save_score:
            save_score.write(str(self.stats.high_score))

    def _check_keydown_events(self, event):
        """Respond to key presses

        Args:
            event (_type_): _description_
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            if self.stats.game_active:
                self._fire_bullet()
                self.shooting_sfx.play()

        elif event.key == pygame.K_p:
            self._start_game()  # Start as Easy Level when P key is pressed

        elif event.key == pygame.K_q:
            self._save_high_score()
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases

        Args:
            event (_type_): _description_
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group.
        """
        # limit bullet showing in the screen.
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets.
        """
        # Get rid of bullets that has disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullets_aliens_collisions()

    def _check_bullets_aliens_collisions(self):
        """Respond to bullets-aliens collisions
        """
        # Remove any bullets and aliens that have collided

        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)  # change False to True after

        if collisions:
            for aliens in collisions.values():
                # increase the player score when ever the bullet collided with an alien.
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()  # prepare the score
            self.sb.check_high_score()  # update the high score

        self._start_new_level()  # New level of game

    def _start_new_level(self):
        """Respond to staring a new level"""

        # if aliens don't exist create a new fleet of aliens
        if not self.aliens:
            # Destory existing bullets and create new fleet
            self.bullets.empty()  # destory the bullets
            self._create_fleet()  # create new fleet of aliens
            self.settings.increase_speed()  # level up the game

            # Increase level
            self.stats.level += 1
            self.sb.prep_level()  # update level image

    def _create_fleet(self):
        """Create the fleet of alien
        """
        # Create an alien and find the number of an aliens in a row
        # Spacing between each alien is equal to one alien width.
        alien = Alien(self)  # alien use for calculation and spacing
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determine the number of aliens that fit on the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)  # defualt is 2

        # Create the full fleet of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Create an alien
        """
        # Create an alien and place it in the row
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x

        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        """Check if an alien is at edge, 
            then update the position of all aliens in the fleet.
        """
        self._check_fleet_edges(
            # checking the position of the alien and determinding an action to do with each fleet.
        )
        self.aliens.update()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):  # type:ignore
            self._ship_hit()  # Destory the ship

        # Look for aliens hitting the bottom of the screen
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge.
        """
        for alien in self.aliens.sprites():
            if alien.check_edges():  # call check edges funtion in alien.py
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction.
        """
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""

        # Allow the user to start over if ship is still available with them
        if self.stats.ships_left > 0:

            # Decrement ships_left and update scoreboard
            self.stats.ships_left -= 1
            self.sb.prep_lifes()
            self.ship_sfx.play()
            self.destory_ship_bullets_aliens()
            self.game_over


            # Pause
            sleep(0.8)

        else:
            self.stats.game_active = False  # End the game
            pygame.mouse.set_visible(True)  # Show the mouse on the screen


    def destory_ship_bullets_aliens(self):
        """Respond to destory the ship-aliens-bellets"""
        # Get rid of any remaining aliens and bullets on the screen
        self.aliens.empty()
        self.bullets.empty()

        # Create a new fleet and center the ship
        self._create_fleet()
        self.ship.center_ship()



    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        # Loop through the aliens sprite
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this the same as the ship got hit.
                self._ship_hit()
                # add sound
                self.ship_sfx.play()
                break

    def _draw_level_button(self):
        """Draw the level button
        easy, medium, hard"""
        self.easy_button.draw_button()
        self.medium_button.draw_button()
        self.hard_button.draw_button()
        if self.stats.ships_left == 0:
            self.game_over.draw_button()

    def _update_screen(self):
        """Update image on the screen and flip to the new screen
        """
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Draw the score information
        self.sb.show_score()

        # Draw the play buttons if the game is inactive.
        if not self.stats.game_active:
            self._draw_level_button()

        pygame.display.flip()


if __name__ == "__main__":
    """Make the game instance and run the game.
    """
    ai = AlienInvasion()
    ai.run_game()  # Running the game
