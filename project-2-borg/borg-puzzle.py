### File: missionary.py
### Implements the borg problem for state
### space search

from improvedsearch import *
from search import *
import time
start_time = time.time()

class BorgState(ProblemState):
    def __init__(self, c, b, boat, operator = None):
        self.c = c
        self.b = b
        self.boat = boat
        self.operator = operator

    def __str__(self):
        """
        Required method for use with the Search class.
        Returns a string representation of the state.
        """
        result = ""
        if self.operator is not None:
            result += "Operator: " + self.operator + "\n"
        result += str(self.c) + "," + str(self.b) + "," + str(self.boat)
        return result

    def equals(self, state):
        """
        Required method for use with the Search class.
        Determines whether the state instance and the given
        state are equal.
        """
        return self.c==state.c and self.b==state.b and self.boat==state.boat

    def dictkey(self):
        """
        Required method for use with the Search class.
        Returns a string that can be used as a ditionary key to
        represent unique states.
        """
        return str(self.c) + "," + str(self.b) + "," + str(self.boat)

    def move_b(self):
        if self.boat == 1: #if boat is on the left
            return BorgState(self.c, self.b-1, 0, "move_b") #swap boat state
        else: #if boat = 0, aka boat is on the right
            return BorgState(self.c, self.b+1, 1, "move_b")

    def move_bb(self):
        if self.boat == 1:
            return BorgState(self.c, self.b-2, 0, "move_bb")
        else:
            return BorgState(self.c, self.b+2, 1, "move_bb")

    def move_bc(self):
        if self.boat == 1:
            return BorgState(self.c-1, self.b-1, 0, "move_bc")
        else:
            return BorgState(self.c+1, self.b+1, 1, "move_bc")

    def move_c(self):
        if self.boat == 1:
            return BorgState(self.c-1, self.b, 0, "move_c")
        else:
            return BorgState(self.c+1, self.b, 1, "move_c")

    def move_cc(self):
        if self.boat == 1:
            return BorgState(self.c-2, self.b, 0, "move_cc")
        else:
            return BorgState(self.c+2, self.b, 1, "move_cc")
    def is_legal(self):
        legal = False
        if self.c >= 0 and self.c <= 3 and self.b >= 0 and self.b <= 3 and self.c >= self.b:
            legal = True
        return legal

    def applyOperators(self):
        """
        Required method for use with the Search class.
        Returns a list of valid successors to the current state
        """
        legal_moves = []
        operators = [self.move_b(), self.move_bb(),
                    self.move_bc(), self.move_c(),
                    self.move_cc()]
        for move in operators:
            if move.is_legal():
                legal_moves.append(move)
        return legal_moves

#Search(BorgState(3,3,1), BorgState(0,0,0), True)
ImprovedSearch(BorgState(3,3,1), BorgState(0,0,0), True)
print("--- %s seconds ---" % (time.time() - start_time))
