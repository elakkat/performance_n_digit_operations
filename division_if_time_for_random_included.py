# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 23:02:48 2018

@author: Gireesh
"""
# THis program generates two n digit rangom numbers and then divide  first number by second

from random import randint
import random
import time
import matplotlib.pyplot as plt

#creating random integers of N digits
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

#c= a/b; 
#print (z)
#print (c)

N=[4, 8, 16, 32, 64, 128, 256, 512]; 
time_for_n_digit=[];
for i in range (0, len(N)):
    t0 = time.time()
    time_base=0;
    for j in range(1,1000):
        a=random_with_N_digits(N[i]);
        b=random_with_N_digits(N[i]); 
#        t0 = time.time()
        c=a/b; 
#        t1 = time.time()
#        total_n = t1-t0; 
#        time_base=time_base+total_n;
    t1 = time.time()
    time_base=t1-t0;
    time_for_n_digit.append(time_base);
    
plt.plot(N, time_for_n_digit)
plt.xlabel('number of digits')
plt.ylabel('time taken for execution')
plt.title('Performance of division',fontsize=14, color='red')
