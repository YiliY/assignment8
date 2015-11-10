# -*- coding: utf-8 -*-
"""
Tue Nov 10 2015: Rain

"""
import sys

def inputPositions():
    
    try: 
        input = raw_input("List of positions? e.g. 1, 10, 100, 1000 \n")
    except(KeyboardInterrupt, EOFError):
        sys.exit()
        
    if input.lower() == "quit":
        sys.exit()
        
    try:
        position_input = positiveInt(input)
        return position_input
    except NonPositiveIntException:
        print("NOT A POSITIVE INTEGER or WRONG FORMAT (please use comma for separation")
        return inputPositions()
        
def inputTrials():
    
    try:
        trialsInput = raw_input("Number of Trials? e.g. 1000 \n")
        
    except(KeyboardInterrupt, EOFError):
        sys.exit()
        
    if trialsInput.lower() == "quit":
        sys.exit() 
        
    try:
        trials = positiveInt(trialsInput)
        return trials[0]
    except NonPositiveIntException:
        print ("Invalid input")
        return inputTrials()

#Validate input value: positive and integer        
def positiveInt(a):
    alist = a.split(',')
    
    intlist = [int(s) for s in alist if s.isdigit()  and int(s) != 0]
    
    if len(intlist) == 0:
        raise NonPositiveIntException()
        
    else:
        return intlist


class NonPositiveIntException(Exception):
    def __str__(self):
        return "NOT A POSITIVE INTEGER or WRONG FORMAT (please use comma for separation)"
        

 
       
