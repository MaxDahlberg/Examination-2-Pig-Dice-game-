class Player:
    def __init__(self, name):
        self.name = name
        self.total_games = 0
        self.total_wins = 0
        self.win_percent = self.total_wins / self.total_games * 100

    def change_name(self, name):
        self.name = name

    def add_total_game(self):
        self.total_games += 1

    def add_win(self):
        self.total_wins += 1

    def get_name(self):
        return self.name

    def get_total_games(self):
        return self.total_games

    def get_total_wins(self):
        return self.total_wins

    def get_win_percent(self):
        if not self.total_games == 0:
            return self.win_percent
