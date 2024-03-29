"""Module for creating and priting the games leaderboard."""

from player import Player
from players import Players


class Leaderboard:
    """Class for creating and priting the games leaderboard."""

    def print_leaderboard():
        """Creates and prints the leaderboard."""
        scores = {}

        for player in Players.get_players():
            scores.update({player.get_name(): player.get_total_wins()})

        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

        print(f"{'╭'}{'─' * 31}{'╮'}")
        print(f"{'│'}{'Leaderboard' :^31}{'│'}")
        print(f"{'│'}{'─' * 31}{'│'}")
        print(f"{'│ '}{'Name':<15}{'Wins':<8}{'Win%':<7}{'│'}")
        print(f"{'│'}{'─' * 31}{'│'}")

        for score in sorted_scores:
            for player in Players.get_players():
                if score[0] == player.get_name():
                    print(
                        f"{'│ '}{score[0]:<15}{score[1]:<8}{player.get_win_percent():<7.1f}{'│'}"
                    )

        print(f"{'╰'}{'─' * 31}{'╯'}")
        print()
