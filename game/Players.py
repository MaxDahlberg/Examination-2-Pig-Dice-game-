from Player import Player


player1 = Player("Filip")
player2 = Player("Liam")
player3 = Player("Oliver")
player4 = Player("Oskar")
player5 = Player("Felix")
player6 = Player("Marcus")


class Players:
    players = [
        player1,
        player2,
        player3,
        player4,
        player5,
        player6,
    ]  # load all players into list

    def load_players(self):
        print("Loading players")

    # load_players (When program starts)
    # read from file and add to list of players

    def save_players():
        print("Saving players")

    # save players (When program exits)
    # read from list of players and override the file

    def get_players():
        return Players.players
