<H1>Dice game Pig</H1>
This project is a simple implementation of the dice game Pig. It contains the version that is played with one die.
The game also has a computer player with three difficulties that can be selected and played against.
The game also keeps and saves an active leaderboard over all the players that have played.

<a href="https://en.wikipedia.org/wiki/Pig_(dice_game)">Read more about the game and its strategies here</a>

<H1>Implementation of difficulties</H1>
Most of the game was simple to implement but we have decided to talk about how the three difficulties have been implemented.
The "Hard" difficulty uses one of the game's optimal strategies which is to roll until a score of 25 and then hold.
The "Easy" difficulty is a bit more simple. It will never roll more than two dice. On average this will result in a score of 7 per round and at max 12.
It will on average take the easy difficulty, more than 15 turns to win the game. 
Finally, the "medium" difficulty is implemented the same way as the "Hard" is.
The only difference is that "Medium" always rolls until a score of 15.

<H1>How to download and run the game</H1>
To start we first need to clone or download the project.
This can be done by navigating to the green "code" button and selecting "download zip".
Once the zip is downloaded it needs to be extracted.

To make sure that we have Python installed, start by running the command "python -V" or "python3 -V" if Python is named that.
Now simply change the directory to the directory of the game that resides in "Examination-2-Pig-Dice-game-\game".
Now simply run the code by typing "python main.py" or "python3 main.py".

<H1>How to run tests and regenerate documentation</H1>
To run the tests or for example, regenerate the documentation, simply start by using a bash terminal. 
Then we need to make sure that the makefile is configured for your Python name.
If your Python name is not "python" but for example "python3", simply run the command "export PYTHON=python3".

Now that the makefile will work, we will start by starting a venv. Simply write "make venv" and then follow the instructions that get printed.
Now run the "make install" followed by the "make installed" command. To make sure that everything gets installed.

To now run the linters, use the "make flake8" and "make pylint" commands. "make lint" will run both linters at the same time.
The command "make black" will check and edit the code into the black codestyle.

To test the code you can use "make unittest" to make the test without coverage. "make coverage" will run the test but with coverage.

To regenerate the documentation you can use the commands "make pdoc" and "make pyreverse". "make doc" will run both commands.
"make pdoc" will generate html files with all the documentation of the classes, and "make pyreverse" will generate UML diagrams.
