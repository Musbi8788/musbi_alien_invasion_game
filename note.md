# Making the fleet move

## Moving to the right
To moving an alien you should set the alien speed in the settings and then update the alien position 

``` Python

self.x += self.settings.alien_speed
self.rect.x = self.x # update the aliens position

```
