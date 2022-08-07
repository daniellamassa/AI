# CSC 320: A* Search



For this assignment, we will apply A* search to the eight puzzle problem. The eight puzzle consists of a three by three board with eight numbered tiles and a blank space. A tile adjacent to the blank space can slide into the space. The object is to figure out the steps needed to get from one configuration of the tiles to another.

## Targets

- [ ] PY.1.P	Python Programming (editing, compiling)
- [ ] PY.2.P	Python Debugging (your code, other's code)
- [ ] PY.3.P	Command-Line Python
- [ ] PY.4.P	Advanced Python (List Comprehensions, Objects)
- [ ] SS.4.AP	Heuristic Search (A*, etc)	

## Description

For this problem, a state should specify the location of each the eight tiles as well as the blank space in the three by three grid. The operators are most efficiently represented as moving the blank left, right, up, or down, rather than creating operators for each of the numbered tiles.


For example, suppose we wanted to get from the initial state to the goal state given below.

```
 1 2 3      1 2 3
 8   6  ->  8   4
 7 5 4      7 6 5 
initial      goal
```


We could accomplish this with the following sequence of operators on the blank.


```
 1 2 3       1 2 3      1 2 3      1 2 3     1 2 3
 8   6       8 6        8 6 4      8 6 4     8   4
 7 5 4       7 5 4      7 5        7   5     7 6 5
initial       right     down       left      up (goal) 
```     


## Setup:

Pull the class repo, which should contain a directory with the following:

search.py: My version of blind search that includes a dictionary.

pq.py: An implementation of a priority queue.

informedSearch.py: To be completed by you.

8puzzle.py: To be completed by you.



## Informed Search


Informed search is very similar to the basic search that we used last week. You can use my version or your own version of the basic search as the starting point for informed search. Because they are so similar it makes sense to have the informed classes inherit from the basic classes.


Implement the `InformedProblemState` class. Informed problem states will need one additional method called `heuristic` that takes the goal state as a parameter and returns the estimate of the distance from the current state to the goal state.

Implement the `InformedNode` class. Informed nodes will need one additional instance variable and one additional method. Informed nodes need to store the `goalState`. They will also need a method called `priority()` to calculate the node's $F$ value for A*. Recall that the priorty is  $F(state) = G(state) + H(state)$. The $G(state)$ represents the cost of getting from the starting node to the current node, which in this case is the depth of the node. The $H(state)$ represents the estimate of the distance from the current state to the goal, which is this case will be obtained by calling the current state's heuristic method.

Implement the InformedSearch class. You'll need to override the `__init__` and the `execute()` methods of the basic search. You should replace the queue with a priority queue and you should use informed nodes rather than standard nodes.

## Eight Puzzle


Similar to last week, you'll need to come up with a representation of the state of the problem as well as its operators. In addition, you'll need to implement several heuristics.

Implement a representation of the eight puzzle state. In the physical world, the eight puzzle is a three by three grid. However, in the virtual world of your program, it may be simpler to implement it as a flat list.

Implement the four operators to move the blank up, down, left, and right. Your operators should make a copy of the current state and then move the tiles of the copy to create the next state. To make a copy of a list do the following:
`newLs = ls[:]`.

Implement both of the eight puzzle heuristics that we discussed in class: tiles out of place and Manhattan distance. Remember that you DO NOT count the blank in either of these heuristics.

Test your solution on the following starting states A-H:
```
   1 3   1 3 4   1 3     7 1 2   8 1 2   2 6 3    7 3 4   7 4 5
 8 2 4   8 6 2   4 2 5   8   3   7   4   4   5    6 1 5   6   3
 7 6 5     7 5   8 7 6   6 5 4   6 5 3   1 8 7    8   2   8 1 2
   A       B       C       D       E       F        G       H
```

using the same goal each time:
```
 1 2 3
 8   4
 7 6 5
 goal
 ```


State A should take 2 steps, state B should take 6 steps, and state C should take 8 steps. You'll need to determine the length of the other solutions.

## Experiment


In order to demonstrate that the manhattan distance heuristic is more informed than the tiles out of place heuristic, you will compare the number of nodes that each search expands on the problems given above (A-H). A node is expanded when it is removed from the priority queue.

In your `Writeup.md` create and fill in the following table:


| Problem  |  A*(tiles) |   A*(dist) |
|----------|------------|------------|
|A         |            |            |
|B         |            |            |
|C         |            |            |
|D         |            |            |
|E         |            |            |
|F         |            |            |
|G         |            |            |
|H         |            |            |


## Submit:


* Git add/commit all your files necessary to solve the problem
* including a `Writeup.md` file that contains the table above, analyzes the results, and explains them.
* I recommend a `test.py` file that I can run demonstrates your code works for the above problems

