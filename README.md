# Dobble-Game
This repository contains a Python implementation of the Dobble game. Dobble is a popular card game where players have to spot matching symbols between two cards. The code generates random cards with symbols and prompts the player to find the matching symbol. 

The code imports the 'string' library to access letters and 'random' for generating random numbers. The code initializes an empty 'symbols' list with all letters. Two empty lists, 'card1' and 'card2', are created. Random positions, 'pos1' and 'pos2', are chosen for the matching symbols. The code prints the random positions for 'card1' and 'card2'. A symbol is randomly selected from 'symbols' and removed to avoid repetition. If 'pos1' equals 'pos2', the symbol is assigned to both positions in 'card1' and 'card2'. Otherwise, the symbol is assigned to 'card1[pos1]' and 'card2[pos2]'. Other positions in the cards are filled with different symbols, ensuring no repetition. The generated cards are printed, and the player is asked to find the matching symbol. If the player's input matches the symbol, a success message is displayed. Otherwise, an error message is shown.

Feel free to explore and enhance the code to add more features or improve the user experience. Enjoy playing Dobble!





User

2 / 2
