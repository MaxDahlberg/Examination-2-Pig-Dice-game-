from Players import Players
from Player import Player


class Leaderboard:
    def print_leaderboard():
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
