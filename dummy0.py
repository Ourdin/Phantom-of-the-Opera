#!/usr/bin/env python

from qlearning import runner
from qlearning import AgentTypes

def lancer():
    runner.lancer(AgentTypes.PLAYER_TYPE.DETECTIVE, smart = True, training = False)

if __name__ == "__main__":
    lancer()