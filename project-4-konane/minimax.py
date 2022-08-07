from updatedKonane import *
import math

class MinimaxNode:
    """
    Black always goes first and is considered the maximizer.
    White always goes second and is considered the minimizer.
    """
    def __init__(self, state, operator, depth, player):
        self.state = state
        self.operator = operator
        self.depth = depth
        self.player = player

class MinimaxPlayer(Konane, Player):

    def __init__(self, size, depthLimit):
        Konane.__init__(self, size)
        Player.__init__(self)
        self.limit = depthLimit
        self.bestMove = []


    def initialize(self, side):
        """
    	Initializes the player's color and name.
    	"""
        self.side = side
        self.name = "MinimaxDepth" + str(self.limit) + "Massa"

    def getMove(self, board):
        """
        Returns the chosen move based on doing an alphaBetaMinimax
    	search.

        CURRENTLY: RUN MINIMAX
        """
        moves = self.generateMoves(board, self.side)
        n = len(moves)
        self.bestMove = []
        if n == 0:
            return []
        else: #RUN MINIMAX
            alpha = -math.inf
            beta = +math.inf
            root_node = MinimaxNode(board, None, 0, self.side) #state, operator, depth, player
            self.alphaBetaMinimax(root_node, alpha, beta)
            return self.bestMove


    def staticEval(self, node):
        """
    	Returns an estimate of the value of the state associated
    	with the given node.
        """
        player_num_moves = len(self.generateMoves(node.state, self.side))
        opponent_num_moves = len(self.generateMoves(node.state, self.opponent(self.side)))

        if player_num_moves == 0 and self.side == "B":
            return -100
        if player_num_moves == 0 and self.side == "W":
            return 100 # BAD SCORE FOR WHITE
        else:
            move_difference = player_num_moves - opponent_num_moves
            if move_difference >= 0: #positive difference = good: opponent has less moves.
                if self.side == "B":
                    return move_difference #positive return = good
                else:
                    return -move_difference #negative return = good
            else: #negative difference = bad: opponent has more moves.
                if self.side == "B":
                    return move_difference #negative return = bad
                else:
                    return abs(move_difference) #positive return = bad
            '''
            if self.side == "B":
                return player_num_moves - opponent_num_moves # POSITIVE CONTRIBUTION GOOD
            else:
                return opponent_num_moves - player_num_moves # NEGATIVE CONTRIBUTION IS GOOD
            '''

    def successors(self, node):
        """
        Returns a list of the successor nodes for the given node.
        """
        successors = []
        moves = self.generateMoves(node.state, node.player)
        if len(moves) != 0:
            for move in moves:
                next_board = self.nextBoard(node.state, node.player, move)
                #use minimax constructor to turn board states to nodes.
                successor_node = MinimaxNode(next_board, move, node.depth + 1, self.opponent(node.player))
                successors.append(successor_node)
            return successors #return list of nodes
        else: #no moves
            return []


    def alphaBetaMinimax(self, node, alpha, beta):
        """
    	Returns the best score for the player associated with the
    	given node.  Also sets the instance variable bestMove to the
        move associated with the best score at the root node.
    	Initialize alpha to -infinity and beta to +infinity.
        """
        successors = self.successors(node)
        if len(successors)  == 0 or node.depth == self.limit:
            return self.staticEval(node)
        else:
            if node.player == "B": #black player: maximize
                best_value = -math.inf
                for cur_node in successors:
                    cur_val = self.alphaBetaMinimax(cur_node, alpha, beta) #recursive minimax
                    if node.depth == 0 and cur_val > best_value: #found a new best move, value we need to store
                        self.bestMove = cur_node.operator
                    alpha = max(alpha, best_value)
                    best_value = max(best_value, cur_val)
                    if beta <= alpha:
                        break
            else: #white player: minimize
                best_value = +math.inf
                for cur_node in successors:
                    cur_val = self.alphaBetaMinimax(cur_node, alpha, beta) #recursive minimax
                    if node.depth == 0 and cur_val < best_value:
                        self.bestMove = cur_node.operator
                    best_value = min(best_value, cur_val)
                    beta = min(beta, best_value)
                    if beta <= alpha:
                         break
            return best_value


if __name__ == '__main__':
    game = Konane(8)
    game.playNGames(2, MinimaxPlayer(8, 2), MinimaxPlayer(8, 1), False)
