# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 11:59:26 2015

@author: YY
"""

import numpy as np
import random
import matplotlib.pyplot as plt
import sys


success_rate = 0.51

# Biased Flip with success rate 0.51
def flip():
    return 1 if random.random() < success_rate else -1

def revenue(position):
    position_value = 1000/position
    daily_trade = [flip() for i in xrange(position)]
    daily_rev = np.mean(daily_trade)
    return daily_rev
        

def output(position, num_trials):       
    rev = [revenue(position) for i in xrange(num_trials)]
    mu = np.mean(rev)
    sigma = np.std(rev) 
    
    # results.txt output
    file = open('results.txt', 'a')
    file.write('\n'+str(position)+'\t\t'+str(mu)+'\t\t'+str(sigma))   
    
    # Pdf Histogram Output
    plt.hist(rev,100,range=[-1,1])
    plt.title('Positions: %d, ' % position+'$\mu=$ %.3g,' % mu + ' $\sigma=$ %.3g'% sigma)
    plt.xlabel('Daily Return')
    plt.ylabel('Frequency')
    plt.savefig('Position_'+str(position)+'_Histogram.pdf')
    plt.clf()
    
