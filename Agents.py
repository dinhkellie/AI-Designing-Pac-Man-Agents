# -*- coding: utf-8 -*-

from game import Agent
from game import Directions
class DumbAgent(Agent):
    "An agent that goes West until it can't."
    def getAction(self, state):
        "The agent receives a GameState (defined in pacman.py)."
        print "Location: ", state.getPacmanPosition()
        print "Actions available: ", state.getLegalPacmanActions()
        if Directions.WEST in state.getLegalPacmanActions():
            print "Going West."
            return Directions.WEST
        elif Directions.EAST in state.getLegalPacmanActions():
            print "Going East."
            return Directions.EAST
        elif Directions.SOUTH in state.getLegalPacmanActions():
            print "Going South."
            return Directions.South
        elif Directions.NORTH in state.getLegalPacmanActions():
            print "Going NORTH."
            return Directions.NORTH
        else:
            print "Going West I guess."
            return Directions.WEST