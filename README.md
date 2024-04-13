This program simulates the classic Battleship game with a variety of configurations and player types.

#### Features 
* Multiple Configurations: The `configs` file contains several setups for different game configurations. A coustom configuration format can be created using the following format:
    ```
    num_rows num_cols
    ship_name ship_length
    ship_name ship_length
    ...
    ```
  Modify the `config_file_path` parameter in `main.py` (line 5) fto chose a different configuration. The default is `classc_game.txt`
* Various Player Types: Choose which player types are going to play
  * Human: For an actual human to play
  * Cheating Computer: Uses opponent's board information to always make an accurate hit
  * Search and Destroy: Strategically hunts around a known hit
  * Random: Makes randoms guesses
#### Development
This project was developed with object-oriented programming principles, inheritance is used to create the different player types. This approach allows for customization and flexability in gameplay.

#### To Run
Execute `main.py` using Python3. Ensure all dependencies are installed before running.
