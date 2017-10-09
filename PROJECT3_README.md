Comparison of Searches

Uninformed searches (BFS, DFS, UCS) did not perform as efficiently as informed searches (A*). This is not suprising because
they did not use any knowledge about the search space in their implementation. Because the uninformed searches only knew to test
whether the given node was a goal node, the pacman agent expands and visits more nodes than it needs to based on the uninformed
searches. For the informed searches, the use of heuristics provides an estimate distance to goal which allows it to make more
informed decisions on which path to take, ultimately at a lower cost and at less nodes expanded than its other search counterparts.

For A* search, using the Manhattan and Euclidean heuristic lowered the overall cost and nodes expanded rather than using the trivial
null heuristic. The two heuristics found paths with the same total cost, but the Manhattan heuristic expanded less nodes. When using
the null heuristic, A* reduces to UCS in its behavior. The space and time complexity of A* are heavily dependent on its heuristic, and
by using a better more desirable heuristic in terms of efficiency, A* greatly outperforms UCS in cost and total nodes expanded.
