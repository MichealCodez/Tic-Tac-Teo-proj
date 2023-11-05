# Tic-Tac-Toe Game

This is a simple console-based Tic-Tac-Toe game implemented in Python. The game provides a two-player experience, where players take turns to input their moves and the program validates the input and determines the winner.

## How to Play

1. **Board Representation**:

    The Tic-Tac-Toe board is represented as follows:

    ```
    1 1 | 1 2 | 1 3
    ---------------
    2 1 | 2 2 | 2 3
    ---------------
    3 1 | 3 2 | 3 3
    ```

    Players need to input the coordinates of their moves based on this representation (e.g., "2 2" represents the center of the board).

2. **Player Turns**:

    - Player 1 is represented by 'X'.
    - Player 2 is represented by 'O'.

    Players take turns entering the row and column numbers (separated by space) where they want to place their symbol.

3. **Winning**:

    The game ends when one player successfully places three of their symbols in a horizontal, vertical, or diagonal row. If the board is filled and no player achieves this, the game is declared a draw.

## Running the Game

To play the game, simply run the Python script in your terminal or command prompt:

```bash
python tic_tac_toe.py
```

Follow the on-screen instructions to input your moves and enjoy the game!

**Note**: This game assumes proper input from the players (valid coordinates and correct format). It doesn't handle invalid inputs for simplicity.
