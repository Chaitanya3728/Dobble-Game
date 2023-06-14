# Dobble-Game
This repository contains a Python implementation of the Dobble game. Dobble is a popular card game where players have to spot matching symbols between two cards. The code generates random cards with symbols and prompts the player to find the matching symbol. 

The code starts by importing the necessary libraries: string for accessing alphabetical characters and random for generating random numbers. It initializes an empty list called symbols and populates it with all the uppercase and lowercase letters.

Two cards, card1 and card2, are created as empty lists with five positions each. Two random positions, pos1 and pos2, are generated to determine the locations of the matching symbols in the cards.

The code prints the random positions chosen for card1 and card2. It also selects a random symbol from the symbols list and removes it to prevent repetition in the two cards. If pos1 is equal to pos2, the matching symbol is assigned to both positions in card1 and card2. Otherwise, the matching symbol is assigned to card1[pos1] and card2[pos2]. For the other positions in the cards, different symbols are randomly chosen from the symbols list and assigned to each card, ensuring no repetition.

Finally, the generated cards are printed, and the player is prompted to spot the similar symbol. If the player's input matches the chosen symbol, a success message is displayed. Otherwise, an error message is shown.

Feel free to explore and enhance the code to add more features or improve the user experience. Enjoy playing Dobble!





User

2 / 2
