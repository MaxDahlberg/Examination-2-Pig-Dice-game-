class Player:
    def __init__(self, name):
        self.name = name
        self.game_total = 0
        self.round_total = 0
        self.total_games = 0
        self.total_wins = 0

    def change_name(self, name):
        self.name = name

    def update_round_total(self, round_total):
        self.round_total = round_total

    def add_round_to_game_total(self):
        self.game_total += self.round_total

    def reset_round_total(self):
        self.round_total = 0

    def reset_game_total(self):
        self.game_total = 0

    def add_total_game(self):
        self.total_games += 1

    def add_win(self):
        self.total_wins += 1

    def get_name(self):
        return self.name

    def get_game_total(self):
        return self.game_total

    def get_round_total(self):
        return self.round_total

    def get_total_games(self):
        return self.total_games

    def get_total_wins(self):
        return self.total_wins

    def get_win_percent(self):
        if not self.total_games == 0:
            return self.total_wins / self.total_games * 100
        else:
            return 0
