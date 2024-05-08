class GameStats:
    """ Recoge as estadísticas """
    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """ vida."""
        self.ships_left = self.settings.ship_limit