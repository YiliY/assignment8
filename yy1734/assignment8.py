# -*- coding: utf-8 -*-
from hw8functions import *
from hw8input import *
import sys

success_rate = 0.51

def start():
    positions = inputPositions()
    trials = inputTrials()
    
    # Create Output Txt file
    file = open('results.txt', 'w')
    file.write('\n'+'Position'+'\t'+'Mean'+'\t\t'+'SD')
    file.close()
    
    for i in range (0,len(positions)):
        output(positions[i],trials)


start()