from informedSearch import *

# ROWS and COLS should always be equal!!
ROWS = 3
COLS = 3
SWAP_HOLDER = 0
GOALSTATE = [1,2,3,8,' ',4,7,6,5]
INVALID_MOVE = [0,0,0,0,0,0,0,0,0]



class EightPuzzle(InformedProblemState):
    #board gets inputted as a list of integers and a space.
    #board representation: [r0c0, r0c1, r0c2... r1c0, r1c1...]
    def __init__(self,board):
        self.board = board

    def __str__(self):
        toPrint = ""
        counter = 0
        for item in self.board:
            toPrint += str(item) + " "
            counter += 1
            if counter % ROWS==0:
                toPrint += "\n"
        return toPrint

    def heuristic(self, goalState):
        #COUNTS NUMBER OF TILES OUT OF PLACE
        counter = 0
        index = 0
        for num in self.board:      #iterate through lists representing current state and goal state.
            if num != GOALSTATE[index]:     #check if values at index match.
                if num == ' ':
                    pass
                else:
                    counter +=1
            index +=1
        return counter

    def heuristic2(self, goalState):
        #DETERMINES MANHATTAN DISTANCE
        manhattan_dist = 0
        for num in self.board:      #iterate through lists representing current state and goal state.
            if num == ' ':
                pass
            else:
                board_index = self.board.index(num)
                solution_index = GOALSTATE.index(num)
                manhattan_dist += abs(board_index - solution_index)
        return manhattan_dist

    def equals(self, state):
        return self.board == state.board

    def move_left(self):
        new_puzzle = self.board.copy()
        empty_index = new_puzzle.index(' ')
        left_index = empty_index - 1
        if left_index < 0 or empty_index % ROWS == 0:
            return EightPuzzle(INVALID_MOVE)
        else:
            new_puzzle[empty_index], new_puzzle[left_index] = new_puzzle[left_index], new_puzzle[empty_index]
            return EightPuzzle(new_puzzle)

    def move_right(self):
        new_puzzle = self.board.copy()
        empty_index = new_puzzle.index(' ')
        right_index = empty_index + 1
        if right_index >= len(self.board) or empty_index % ROWS == ROWS or empty_index % ROWS == ROWS - 1:
            return EightPuzzle(INVALID_MOVE)
        else:
            new_puzzle[empty_index], new_puzzle[right_index] = new_puzzle[right_index], new_puzzle[empty_index]
            return EightPuzzle(new_puzzle)

    def move_up(self):
        new_puzzle = self.board.copy()
        empty_index = new_puzzle.index(' ')
        up_index = empty_index - COLS
        if up_index < 0 or empty_index < COLS:
            return EightPuzzle(INVALID_MOVE)
        else:
            new_puzzle[empty_index], new_puzzle[up_index] = new_puzzle[up_index], new_puzzle[empty_index]
            return EightPuzzle(new_puzzle)

    def move_down(self):
        new_puzzle = self.board.copy()
        empty_index = new_puzzle.index(' ')
        down_index = empty_index + COLS
        if down_index >= len(self.board) or empty_index >= COLS*(COLS-1):
            return EightPuzzle(INVALID_MOVE)
        else:
            new_puzzle[empty_index], new_puzzle[down_index] = new_puzzle[down_index], new_puzzle[empty_index]
            return EightPuzzle(new_puzzle)

    def is_valid(self):
        valid_move = True
        new_puzzle = self.board.copy()

        if new_puzzle == INVALID_MOVE:
            valid_move = False
            '''
        else:
            empty_index = new_puzzle.index(' ')
            if empty_index % ROWS == 0:   #left
                valid_move = False
            elif empty_index < COLS: #UP
                valid_move = False
            elif empty_index % ROWS == ROWS or empty_index % ROWS == ROWS - 1: #right
                valid_move = False
            elif empty_index >= COLS*(COLS-1): #down
                valid_move = False
        '''
        return valid_move

    def applyOperators(self):
        """
        Required method for use with the Search class.
        Returns a list of valid successors to the current state
        """
        legal_moves = []
        #operators = ["left", "right", "up", "down"]
        operators = [self.move_right(), self.move_left(), self.move_up(), self.move_down()]
        for move in operators:
            if move.is_valid():
                legal_moves.append(move)
        return legal_moves

    def dictkey(self):
        """
        Required method for use with the Search class.
        Returns a string that can be used as a ditionary key to
        represent unique states.
        """
        return str(self.board)


'''
TESTING

print(puzzle)
print("MOVE LEFT")
print(puzzle.move_left())
print("MOVE DOWN")
print(puzzle.move_down())
print("MOVE RIGHT")
print(puzzle.move_right())
print("MOVE UP")
print(puzzle.move_up())

puzzle1 = EightPuzzle([' ',3,8,2,1,4,7,6,5])
puzzle2 = EightPuzzle([1,' ',3,8,1,4,7,6,5])
puzzle3 = EightPuzzle([1,3,' ',8,2,1,4,6,5])

print(puzzle1)
print(puzzle1.applyOperators())
print(puzzle2)
print(puzzle2.applyOperators())
print(puzzle3)
print(puzzle3.applyOperators())

puzzle1 = EightPuzzle([' ',1,3,8,2,4,7,6,5])
puzzle2 = EightPuzzle([1,3,4,8,6,2,' ',7,5])
puzzle3 = EightPuzzle([1,3,' ',4,2,5,8,7,6])


print(puzzle1.heuristic(GOALSTATE))
print(puzzle2.heuristic(GOALSTATE))
print(puzzle3.heuristic(GOALSTATE))

puzzle1 = EightPuzzle([' ',3,8,2,1,4,7,6,5])
puzzle2 = EightPuzzle([1,' ',3,8,1,4,7,6,5])
puzzle3 = EightPuzzle([1,3,' ',8,2,1,4,6,5])

print(puzzle1)
print(puzzle1.applyOperators())
print(puzzle2)
print(puzzle2.applyOperators())
print(puzzle3)
print(puzzle3.applyOperators())

puzzle = EightPuzzle([' ',1,3,8,2,4,7,6,5])
print(puzzle)
print("MOVE LEFT")
print(puzzle)
print("MOVE DOWN")
puzzle.move_down()
print(puzzle)
print("MOVE RIGHT")
puzzle.move_right()
print(puzzle)
print("MOVE UP")
puzzle.move_up()
print(puzzle)
'''
