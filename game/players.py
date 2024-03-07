"""Module for keeping player statistics between runtimes."""

import os
import pickle


class Players:
    """Class for keeping player statistics between runtimes."""

    players = []

    def load_players():
        """Load players from a file."""
        if os.path.exists("players.bin"):
            try:
                with open("players.bin", "rb") as players_file:
                    Players.players = pickle.load(players_file)
            except EOFError:
                Players.players = []
        else:
            Players.players = []

    def save_players():
        """Save players in a file."""
        try:
            with open("players.bin", "wb") as players_file:
                pickle.dump(Players.players, players_file)
        except FileExistsError:
            print("File doesnt exist")

    def add_player(player):
        """Add player to list of players."""
        Players.players.append(player)

    def get_players():
        """Get list of players."""
        return Players.players
