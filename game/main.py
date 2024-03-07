"""Executes the program"""

import cmd
from game import Game


class Main(cmd.Cmd):
    def do_start(self, _):
        """Start the game"""
        Game.login_menu()

    def do_exit(self, _):
        """Leave the game."""
        return True


def main():
    """Execute the main program."""
    print('"start" to start the game\n\n"exit" to exit\n')
    Main().cmdloop()


if __name__ == "__main__":
    main()
