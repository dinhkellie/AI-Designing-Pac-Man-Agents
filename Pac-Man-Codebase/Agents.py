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
        print "Actions available: ", state.getLegalPacmanActions()
        randomDir = random.choice(state.getLegalPacmanActions())
        print "Going ", randomDir
        return randomDir
