"""Module for keeping statistics of a player."""


class Player:
    """Class for keeping statistics of a player."""

    def __init__(self, name):
        """Init the player object."""
        self.name = name
        self.game_total = 0
        self.round_total = 0
        self.total_games = 0
        self.total_wins = 0

    def change_name(self, name):
        """Change the name."""
        self.name = name

    def update_round_total(self, round_total):
        """Update the total round score."""
        self.round_total = round_total

    def add_round_to_game_total(self):
        """Add the total round score to the total game score."""
        self.game_total += self.round_total

    def reset_round_total(self):
        """Reset the total round score."""
        self.round_total = 0

    def reset_game_total(self):
        """Reset the total game score."""
        self.game_total = 0

    def add_total_game(self):
        """Add 1 game to the total game score."""
        self.total_games += 1

    def add_win(self):
        """Add 1 win."""
        self.total_wins += 1

    def get_name(self):
        """Get name."""
        return self.name

    def get_game_total(self):
        """Get total game score."""
        return self.game_total

    def get_round_total(self):
        """Get total round score."""
        return self.round_total

    def get_total_games(self):
        """Get total number of games."""
        return self.total_games

    def get_total_wins(self):
        """Get total number of wins."""
        return self.total_wins

    def get_win_percent(self):
        """Get win % if total games are not 0."""
        if not self.total_games == 0:
            return self.total_wins / self.total_games * 100
        else:
            return 0
