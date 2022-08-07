# Konane Player

For this assignment you will implement the minimax adversarial search algorithm with alpha-beta pruning on the game of Konane, also known as Hawaiian Checkers. The game is played on an N by N board of black and white pieces. N may be as small as 4 or as large as 8. The board shown below is 8 by 8, and uses 'B' for black pieces and 'W' for white pieces.


```
     0 1 2 3 4 5 6 7 
  0  B W B W B W B W
  1  W B W B W B W B
  2  B W B W B W B W
  3  W B W B W B W B
  4  B W B W B W B W 
  5  W B W B W B W B
  6  B W B W B W B W        
  7  W B W B W B W B
```


In order to play Konane, the black player goes first and removes one black piece from the corner or the center of the board. For an `8 by 8` board, this equates to positions `(0,0), (3,3), (4,4), or (7,7)`. Next the white player removes a white piece adjacent to the space created by the first move. Then the players alternate moves, each jumping one of their own pieces over one horizontally or vertically adjacent opponent's piece, landing in an empty space on the other side, and removing the jumped piece. If desired, this may be continued in a multiple jump, as long as the same piece is moved in a straight line. The game ends when one player can no longer move and that player is considered the loser.

## Setup

Pull the class repo and copy the relevant directory to your repo.  Add/commit/push the files.

I've provided a python implementation of the Konane game. You will need to implement minimax and then focus on finding a good evaluation function for estimating the value of a given Konane board. It has been noted that "the performance of a game-playing program is dependent on the quality of its evaluation function" (Russell and Norvig, page 171).


## Implementing Minimax 


Open the file `updatedKonane.py` and read through the definitions provided. The board size must be specified in the constructor for the Konane class. There is also a base class called Player and there are three specializations of this class: `HumanPlayer`, `SimplePlayer`, and `RandomPlayer`. Each of these player definitions inherits from both the `Player` class and the `Konane` class. Therefore, the board size must also be specified in the constructors for these classes.

* Modify the calls at the bottom of `updatedKonane.py` to play a game between the `RandomPlayer`  and the `SimplePlayer` on an `8 by 8` board.

* In the file `minimax.py`, implement a `MinimaxNode` class to hold the necessary information for a search node in a minimax game tree. It should include the following data:
        * `state`: the current board configuration
        * `operator`: the move that resulted in the current board configuration
        * `depth`: the depth of the node in the search tree
        * `player`: maximizer or minimizer


* In the file `minimax.py`, implement a `MinimaxPlayer` class that inherits from both thePlayer class and the `Konane`. Your class must override the abstract methods `initialize` and `getMove` from the `Player` class. It should also implement several other methods, which are described in the file. 

Notice that the first line of the `MinimaxPlayer` constructor calls the constructor of the `Konane` base class. Also notice that the depth limit for the search is passed in as an argument to the class. Therefore you will not need to pass it as an argument to the minimax method. You should be able to use your `MinimaxPlayer` in the following way:

```
game = Konane(8)
game.playNGames(2, MinimaxPlayer(8, 2), MinimaxPlayer(8, 1), False)
```


Executing the above commands should demonstrate that the minimax player which searches to depth 2 will outperform a minimax player which only searches to depth 1.

```
Game 0
MinimaxDepth2 wins
Game 1
MinimaxDepth2 wins
MinimaxDepth2 2 MinimaxDepth1 0

```

## A Static Evaluator
* Implement an appropriate static evaluator for Konane. The key difference between Konane players will be in how they evaluate boards. Based on our reading, the static evaluator should:

    * Order the end states correctly
    * Be time efficient to compute
    * Be strongly correlated with the actual chances of winning


Explain your static evaluator in your `Writeup.md`.  Discuss the various features you considered including as part of the evaluation function. How did you determine which features were the most effective? This should be between one and two pages of single-spaced text.

## Challenge: Alpha Beta

Update your minimax to use alpha-beta pruning
## Tournament Play

We will hold two tournaments. One tournament will have both a depth limit of 4 and a time limit of 3 seconds. The other tournament will have only a time limit of 3 seconds.

Each Konane player should conduct a minimax search and return a move within 5 seconds. If a move is not returned within the time limit, then a random move will be selected. In addition, each Konane player may not use more than half a gigabyte of memory. This can be monitored using the "top" command.

Each Konane player will play every other Konane player in the tournament twice, one time going first and the other time going second. Each player will receive a +1 for a win. The winner of the tournament will be determined by the cumulative score over all of these games. It will be possible to have multiple winners.

During class we will hold the tournament to determine whose program is the ultimate Konane player. If for some reason your program is not operational, you must compete against the computer champion.

## Submit

* add/commit/push all files, 
* a `Writeup.md` describing your player, especially the heuristic static evaluator.