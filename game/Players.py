import pickle


class Players:
    players = []

    def load_players():
        try:
            with open("players.bin", "rb") as players_file:
                Players.players = pickle.load(players_file)
            print("Loading players")
        except FileExistsError:
            with open("players.bin", "wb") as players_file:
                pass
            Players.load_players()

    def save_players():
        try:
            with open("players.bin", "wb") as players_file:
                pickle.dump(Players.players, players_file)
            print("Saving players")
        except FileExistsError:
            print("File doesnt exist")

    def add_player(player):
        Players.players.append(player)

    def get_players():
        return Players.players
