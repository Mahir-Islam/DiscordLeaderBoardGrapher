import matplotlib.pyplot as plt
import numpy as np
from pylab import *
import random

def PROCESS(x):
	multiplier = 1
	if x[-1] == "k":
		multiplier = 1000
		x = x[:-1]
	y = float(x) * multiplier
	return int(y)


def S_D(values):
	n = len(values)
	m = sum(values)/n
	s = 0
	
	for x in values:
		s += (x - m)**2

	s = (s/n)**0.5

	#[standard deviation, variance, error interval, mean]
	return [ s, s*s, s/(n**0.5), m]

def Z_L(expDex):
	vals = [round(expDex[0]/x, 0) for x in range(1, len(expDex)+1)]
	return vals
	
def PLOT(index, msgDex, expDex, title, statsF):

	funcs = [S_D, Z_L]
	items = []
	zipf = []

	label = "Experience Points" 

	if statsF[0]:
		items = funcs[0](expDex)

	if statsF[1]:
		zipf = funcs[1](expDex)


		label =	f"""
Mean: {round(items[3],2)},
Variance: {round(items[1],2)},
Standard Deviation: {round(items[0],2)},
Error Interval: {round(items[2],4)}"""

	plt.rcdefaults()

	fig, ax = plt.subplots()
	names = [ key for key in index.keys() ]
	y_pos = np.arange(len(names))
	#error = np.random.rand(len(names))

	if zipf != []:
		plt.plot(zipf, [x for x in range(0,len(zipf))], color='firebrick',linewidth=2)

	major_ticks = np.arange(0, max(expDex), max(expDex)/10 )
	minor_ticks = np.arange(0, max(expDex), max(expDex)/10 )

	ax.set_xticks(major_ticks)
	ax.set_xticks(minor_ticks, minor=True)
	ax.set_yticks(major_ticks)
	ax.set_yticks(minor_ticks, minor=True)

	ax.grid(which='both')

	ax.barh(y_pos, expDex, align='center', label=label)
	ax.set_yticks(y_pos)
	ax.set_yticklabels(names)
	ax.invert_yaxis()  # labels read top-to-bottom
	ax.set_xlabel('Experience Points')
	ax.set_title(f"Top {len(names)} users in {title}.")
	
	plt.legend(loc="lower right")

	plt.show()
