# <center> Project 3 A* Search</center>

# <center> Experiment</center>

| Problem  |  Step Length (# of tiles) |  A*(tiles) |  A*(dist)  |
|----------|---------------------------|------------|------------|
|A         |2                          |2           |2           |
|B         |6                          |7           |6           |
|C         |8                          |13          |8           |
|D         |10                         |38          |14          |
|E         |10                         |38          |14          |
|F         |12                         |90          |137         |
|G         |15                         |333         |40          |
|H         |20                         |3756        |1032        |

# <center> Analysis</center>
For each of the problem states, a manhattan distance heuristic implementation outperformed the "number of tiles out of place" heuristic implementation. This was true for all problem states except Problem F. Despite this, manhattan distance is an optimal heuristic because it calculates the absolute value of the difference for each tile's index and the goal index, and sums these values together. The "number of tiles out of place" heuristic, on the other hand, simply returns a counter of the number of tiles that are not in their correct goal state. The manhattan distance provides a more detailed heuristic value, which allows for a better evaluation of the board state.
