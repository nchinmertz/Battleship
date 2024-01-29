A simulation of the game Battleship with multiple ways to set up the game as well as types of players.

The `configs` file shows all the different types of game set ups. This can be changed in the main.py file by changing the pathname parameter. It is currently set to `classc_game.txt`.

The type of players can be chosen once the program has started. There are four different options for players, a human player or three different computer players. The three computer players are cheating which knows its opponents board, search and destroy which will continue to make hits around a known hit, and random which will make random guesses. Inheritance is used to create this different type of players. The first layer differentiating between a human player and a computer, the second layer being for all the different types of computer players.

