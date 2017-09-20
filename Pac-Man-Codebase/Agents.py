# -*- coding: utf-8 -*-

from game import Agent
from game import Directions
import random
class DumbAgent(Agent):
    #"An agent that goes West until it can't."
    def getAction(self, state):
        #"The agent receives a GameState (defined in pacman.py)."
        print "Location: ", state.getPacmanPosition()
        print "Actions available: ", state.getLegalPacmanActions()
        if Directions.WEST in state.getLegalPacmanActions():
            print "Going West."
            return Directions.WEST

class RandomAgent(Agent):
    def getAction(self, state):
        print "Location: ", state.getPacmanPosition()
        actions = state.getLegalPacmanActions()
        # remove stop from directions
        actions.remove(Directions.STOP)
        print "Actions available: ", actions
        randomDir = random.choice(actions)
        print "Going: ", randomDir
        return randomDir

class ReflexAgent(Agent):
    def getAction(self, state):
        currentPacman = state.getPacmanPosition()

        # get x,y position of the pacman
        x = currentPacman[0]
        y = currentPacman[1]
        print "Location: ", currentPacman

        actions = state.getLegalPacmanActions()
        actions.remove(Directions.STOP)
        print "Actions available: ", actions

        # get locations of all food
        currentFood = state.getFood()
        
        # dictionary to update x,y according to directions available
        horz = {'West': x-1, 'East': x+1}
        vert = {'North': y+1, 'South': y-1}

        #indicate whether or not a direction with food is found 
        indicator = 0

        for action in actions: 
            if action in horz:
                #update x value to get the x position of pellete
                x = horz.get(action)
            if action in vert:
                #update y value to get the y position of pellete
                y = vert.get(action) 
            if state.hasFood(x, y):
                # if food is found, turn on indicator and take this direction
                indicator = 1
                print "Going: ", action
                return action
            else: 
                # restore x,y values and check next action
                x = currentPacman[0]
                y = currentPacman[1] 
        # if food is not found, indicator is off and pick a random direction
        if indicator == 0: 
            randomDir = random.choice(actions)
            print "Going: ", randomDir
            return randomDir

