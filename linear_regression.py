#!/usr/bin/python

'''
	Linear regression for cell data (dropping low values due to move).
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def readData():
	data = pd.read_csv('httpqps.csv')
	data.head()
	y = data["QPS"]
	x = list(range(0, len(y), 1))
	return x, y


def findFit(x, y):
	m, b = np.polyfit(x, y, 1)
	fit = np.polyval([m, b], x)
	return fit


def plotData(x, y, fit):
	plt.plot(x, fit)
	plt.scatter(x, y)
	plt.grid(True)
	plt.xlabel("time")
	plt.ylabel("qps")
	plt.show()


def main():
	x, y = readData()
	fit = findFit(x, y)
	plotData(x, y, fit)


if __name__ == '__main__':
	main()
