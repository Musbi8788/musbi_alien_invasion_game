class GameStats:
    """Track statistics for Alien Invasion"""
    
    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.rest_stats()
        # Start Alien Invasion in an active state
        self.game_active = True 

    def rest_stats(self,):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        
