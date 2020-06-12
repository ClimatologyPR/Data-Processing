# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:50:14 2019

@author: Roberto
"""

import numpy as np

def cleanFile():
	#--- Opens file as readable then copies data to y, then closes file
	data = open(wpath+fileName, 'r')
	y = data.read()
	data.close()

	#--- Reopens file as writable
	data = open(wpath+fileName, 'w')

	#--- test
	print(y)

	y = y.replace(', ', ',').replace(' ,',',')

	#--- test
	print(y)

	#--- Write data from y into file
	data.write(y)
	    
	data.close()

#--- Opens and transposes file
def transpose():
	x = np.loadtxt(fname = wpath+fileName, dtype='str', delimiter = ',')
	x = np.transpose(x)
	np.savetxt(fileName, x, fmt='%s', delimiter=",")
	
wpath = 'C:/Users/Roberto/Desktop/'
fileName = '1982010300Z_indices.txt'

#---
cleanFile()
#---
transpose()

#--- Will create new file with trims [NO LONGER TO BE USED] -----------------

#data = open(wpath+fileName, 'r')
#f = open('test.txt', 'w')

#for line in data:
#    line = line.replace(', ', ',').replace(' ,',',')
#    print(line)
#    f.write(line)
    
    
#data.close()
#f.close()

#----------------------------------------------------------------------------
