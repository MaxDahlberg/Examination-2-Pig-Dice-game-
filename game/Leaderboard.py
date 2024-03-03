class Leaderboard:
    def print_leaderboard():
        # for player in players.get_players
        # player.get_name player.get_score
        player_name = ["Filip", "Liam", "Oliver", "Oskar", "Felix", "Marcus"]
        player_score = [3, 7, 3, 421, 34, 1]
        index = 0
        scores = {}

        for name in player_name:
            score = player_score[index]
            index += 1
            scores.update({name: score})

        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

        print(f"{'╭'}{'─' * 31}{'╮'}")
        print(f"{'│'}{'Leaderboard' :^31}{'│'}")
        print(f"{'│'}{'─' * 31}{'│'}")
        print(f"{'│ '}{'Name':<15}{'Wins':<8}{'Win%':<7}{'│'}")
        print(f"{'│'}{'─' * 31}{'│'}")
        for score in sorted_scores:
            print(f"{'│ '}{score[0]:<15}{score[1]:<8}{'100.0':<7}{'│'}")

        print(f"{'╰'}{'─' * 31}{'╯'}")
        print()
