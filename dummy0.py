#!/usr/bin/env python

import runner
from Parsing import PLAYER_TYPE

def lancer():
    runner.lancer(PLAYER_TYPE.DETECTIVE, smart = True, training = False)