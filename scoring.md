# Scoring the Final Part

## Adding the player button
We make the game to inactive state and this is a great logic to now add a button 

``` self.game_active = False ```

```self.font.render # render string in an image```
Because pygame only render images not string so we convert it to an image

``` 
def _update_screen(self):
        """Update image on the screen and flip to the new screen
        """
        
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Draw the play button if the game is inactive.
        if not self.stats.game_active:
            self.play_button.draw_button() # Note when we draw the button make the button show ontop of all the others element and this is the best place to but it

        pygame.display.flip() 
```

## Self addition 
make the game to show the game over button when the user fail

### Resetting the Game