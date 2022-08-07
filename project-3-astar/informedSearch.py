from pq import *
from search import *

class InformedProblemState(ProblemState):
    """
    Informed problem states will need one additional method called heuristic
    that takes the goal state as a parameter and returns the estimate of the
    distance from the current state to the goal state.
    """
    def heuristic2(self, goalState):
        abstract()

class InformedNode(Node):
    """
    Informed nodes need to store the goalState. They will also need a method
    called priority() to calculate the node's $F$ value for A*. Recall that the
    priorty is  $F(state) = G(state) + H(state)$. The $G(state)$ represents the
    cost of getting from the starting node to the current node, which in this
    case is the depth of the node. The $H(state)$ represents the estimate of the
    distance from the current state to the goal, which is this case will be
    obtained by calling the current state's heuristic method.
    """
    def __init__(self, state, parent, goalState, depth):
        self.goalState = goalState
        super(InformedNode, self).__init__(state, parent, depth) #override basic search per instructions.

    def priority(self):
        f_value = self.depth + self.state.heuristic2(self.goalState)
        return f_value

class InformedSearch(Search):
    def __init__(self, initialState, goalState, verbose=False):
        self.uniqueStates = {}
        self.uniqueStates[initialState.dictkey()] = True
        self.q = PriorityQueue()
        self.q.enqueue(InformedNode(initialState, None, goalState, 0))
        self.goalState = goalState
        self.verbose = verbose
        solution = self.execute()
        if solution == None:
            print( "Search failed")
        else:
            self.showPath(solution)
    def execute(self):
        nodes_expanded = 0
        while not self.q.empty():
            current = self.q.dequeue()
            nodes_expanded += 1
            if self.goalState.equals(current.state):
                return current
            else:
                successors = current.state.applyOperators()
                for nextState in successors:
                    #if not self.uniqueStates.has_key(nextState.dictkey()):
                    # simple <key> in <dictionary> works too, but I find it
                    # more semantically vague than
                    # <key> in <dictionary>.keys()
                    if nextState.dictkey() not in self.uniqueStates.keys():
                        n = InformedNode(nextState, current, self.goalState, current.depth+1)
                        self.q.enqueue(n)
                        self.uniqueStates[nextState.dictkey()] = True
                if self.verbose:
                    print( "Expanded:", current)
                    print( "Number of successors:", len(successors))
                    print("Queue length:", self.q.size())
                    print("Number of nodes expanded: ", nodes_expanded)
                    print( "-------------------------------")
