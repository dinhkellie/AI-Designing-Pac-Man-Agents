# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

class Node:
    def __init__(self, state, action, cost, parent):
        self.state = state
        self.action = action 
        self.cost = cost
        self.parent = parent

    def getState(self):
        return self.state

    def getAction(self):
        return self.action 

    def getCost(self):
        return self.cost

    def getParent(self):
        return self.parent

def findPath(node):
    path = []
    listOfParents = []
    listOfParents.append(node)
    while(node.getParent()!=None):
        listOfParents.insert(0,node.getParent())
        node = node.getParent()
    for p in listOfParents:
        if p.getAction()!=None:
            path.append(p.getAction())
    return path

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    head = Node(problem.getStartState(), None, 0, None)
    Frontier = util.Stack()
    Frontier.push(head)
    Explored = {}
    path = []
    while(True):
        if Frontier.isEmpty():
            return []
        node = Frontier.pop()
        if problem.isGoalState(node.getState()):
            path = findPath(node)
            return path
        Explored[node.getState()] = True
        for state, action, cost in problem.getSuccessors(node.getState()):
            if state not in Explored:
                nextNode = Node(state, action, cost, node)
                Frontier.push(nextNode)


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    head = Node(problem.getStartState(), None, 0, None)
    Frontier = util.Queue()
    Frontier.push(head)
    Explored = {}
    path = []
    while(True):
        if Frontier.isEmpty():
            return []
        node = Frontier.pop()
        if problem.isGoalState(node.getState()):
            path = findPath(node)
            return path
        Explored[node.getState()] = True
        for state, action, cost in problem.getSuccessors(node.getState()):
            if state not in Explored:
                nextNode = Node(state, action, cost, node)
                Frontier.push(nextNode)


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    head = Node(problem.getStartState(), None, 0, None)
    Frontier = util.PriorityQueue()
    Frontier.push(head, head.getCost())
    Explored = set()
    path = []
    while(True):
        if Frontier.isEmpty():
            return []
        node = Frontier.pop()
        if problem.isGoalState(node.getState()):
            path= findPath(node)
            return path
        successors = problem.getSuccessors(node.getState())
        for state, action, cost in successors:
            if state not in Explored:
                Explored.add(state)
                cost = cost + node.getCost()
                nextNode = Node(state, action, cost, node)
                Frontier.push(nextNode, cost)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
        """Search the node that has the lowest combined cost and heuristic first."""
    # "*** YOUR CODE HERE ***"
    # head = Node(problem.getStartState(), None, 0, None)
    # Frontier = util.PriorityQueue()
    # Frontier.push(head, head.getCost())
    # Explored = set()
    # path = []
    # while(True):
    #     if Frontier.isEmpty():
    #         return []
    #     node = Frontier.pop()
    #     if problem.isGoalState(node.getState()):
    #         path= findPath(node)
    #         return path
    #     successors = problem.getSuccessors(node.getState())
    #     for state, action, cost in successors:
    #         if state not in Explored:
    #             Explored.add(state)
    #             # cost = cost + node.getCost() + heuristic(state, problem)
    #             nextNode = Node(state, action, cost, node)
    #             Frontier.push(nextNode,cost)

    head = Node(problem.getStartState(), None, 0, None)
    Frontier = util.PriorityQueue()
    Frontier.push(head, head.getCost())
    Explored = set()
    while (True):
        if Frontier.isEmpty():
            return []
        node = Frontier.pop()
        if problem.isGoalState(node.getState()):
            path = findPath(node)
            return path
        if node.getState() not in Explored:
            Explored.add(node.getState())
            for state, action, cost in problem.getSuccessors(node.getState()):
                if state not in Explored:
                    backwardCost = cost + node.getCost()
                    forwardCost = heuristic(state, problem)
                    totalCost = backwardCost+forwardCost
                    nextNode = Node(state, action, backwardCost, node)
                    Frontier.push(nextNode, totalCost)

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
