1. Table of DFS and BFS Evaluation 

  * Assumption: being optimal means the algorithm finds the best solution/shortest route

![DFS_BFS_Evaluation](https://github.com/clairew2018/AI-Designing-Pac-Man-Agents/blob/master/DFS_BDF_Eval.png)

2. Reflection on how the searches compare 

> Based on the data in the table above, Depth-First Search always finds a solution, but the solution is not guaranteed to be optimal. It explores relatively fewer nodes than Breath-First Search. Breath-First Search explore always finds a solution, and the solution is guaranteed to be optimal. However, it also explores more nodes than Depth-First Search.

> Based on the algorithms, Depth-First Search is good for looking for a solution in a limited time when on the map, there is a long distance between starting point and destination, while Breath-First Search is good for finding the optimal solution when there is a short distance to the destination. Depth-First 