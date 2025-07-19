class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.rest_stats()
        # Start game in an inactive state
        self.game_active = False
        self.read_high_score()

    def read_high_score(self):
        """Read the high score and set the """

        # High score should never be reset.
        try:
            with open("high_score.txt", "r") as content:
                all_time_high_score = content.read()
                
            self.high_score = int(all_time_high_score)
        
        except FileNotFoundError:
            self.high_score = 0
            with open("high_score.txt", "w") as content:
                content.write(str(self.high_score))

            
    def rest_stats(self,):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1 # The game level is one
