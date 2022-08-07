# Konane Player


## Alpha Beta Pruning Minimax

I was able to successfully implement minimax with alpha beta pruning. In order to do this, I relied on class discussions and pseudocode from the textbook. In my code, I assigned the Black Player to be the maximizer, and the White Player to be the minimizer. I ensured that alpha was initialized to -infinity, and beta was initialized to +infinity. I also generated a "best_value" variable, that gets updated as the program iterates through the successor nodes. The code operates in the sense that it recursively calls the alpha beta minimax function. Additionally, I was able to set instance variable "bestMove" to the move associated with the best score at the root node. However, I needed to modify this area of the code from "if node.depth == 0" to the following:

* "if node.depth == 0 and cur_val > best_value" (for a maximizing player)
* "if node.depth == 0 and cur_val < best_value" (for a minimizing player)

This modification was imperative because if a new best move is found, that move needs to be stored as well. Finally, I was able to use the min() and max() functions to update the values of alpha/beta and the best value, and I utilized a break statement to implement pruning. Alpha Beta Pruning Minimax works in the sense that it shortens the search time by decreasing the number of nodes that are evaluated. More specifically, if alpha is greater than beta at a given time during the search, then we know that we do not need to explore that child node.

## The Static Evaluator
My static evaluator is fairly simple, it calculates the number of moves the player and the opponent has. If the player has 0 moves and is a maximizing player (black), the static evaluator returns -100 to indicate a bad score. If the player has 0 moves and is a minimizing player (white), the static evaluator returns 100, which is a bad score for the minimizing player. In cases that the player does not have 0 moves, the difference between the player's and the opponent's number moves is calculated. If the move difference is positive, the player has more possible moves than the opponent. If the move difference is negative, the opponent has more possible moves than the player. Based on this, and whether or not the player is minimizing or maximizing, the corresponding negative/positive value of the move difference is returned (see code comments for more detail).

Overall, my implementation of Alpha Beta Pruning Minimax and the static evaluator proves to be successful. It passes the test case provided in the README, in which two games are played with a depth1 player and a depth2 player (depth2 player wins both games). I tested my code with other various depth cases, and my implementation was also successful. However, for depth3 vs depth2, depth3 only wins one of the two games. Similarly, for depth4 vs depth3, depth4 only wins one of the two games. I believe there may several causes for this:

1. I'm not certain that my code accounts for multiple board states with the same "best value". For example, in the case of depth3 vs depth2, depth3 SHOULD win all games. However, if the depth3 player has several possible board options of the same value, it has no way of knowing which one is truly the best move. Therefore, the depth3 player can essentially "make a mistake" with its next move selection.

2. Due to the fact that Konane is deterministic game, the program will always search through the possible moves in the same order. 
