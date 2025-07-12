# Making the fleet move

## Moving to the right
To moving an alien you should set the alien speed in the settings and then update the alien position 

``` Python

self.x += self.settings.alien_speed
self.rect.x = self.x # update the aliens position

```

### Creating settings for fleet direction
### Checking whether an alien has hit the edge
```

    def check_edges(self):
        """Return True if alien is at edge of screen
        """
        # get the screen rect 
        screen_rect = self.screen.get_rect()

        # checking the alien fleet position in the screen
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

```
### Dropping the fleet and changing direction

```
 def _update_aliens(self):
        """Check if an alien is at edge, 
            then update the position of all aliens in the fleet.
        """
        self._check_fleet_edges() # checking the position of the alien and determinding an action to do with each fleet.
        self.aliens.update()

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge.
        """
        for alien in self.aliens.sprites():
            if alien.check_edges(): # call check edges funtion in alien.py 
                self._change_fleet_direction()
                break


    def _change_fleet_direction(self):
        """Drop the entire and fleet and change the fleet's direction.
        """
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

```


### Shotting Aliens

we'll us sprite.groupcollide() methods to check it two group element detected

# Checking if two element have detected

``` pygame.sprite.groupcollide(self.aliens, self.bullets, True, True) ```

This code will get rid of any aliens that have been hit with the bullets