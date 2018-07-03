# PANDAS4

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
from datetime import datetime

# PROBLEM 1
# function that cleans and plots data from djia.csv
def p1():
	# load data
	data = pd.read_csv("DJIA.csv")
	# set index as datetime
	date_index = pd.to_datetime(data["DATE"], format="%Y-%m-%d")
	data.index = date_index
	df = data.drop(columns=["DATE"])
	# drop empty rows and change to floats
	df = df.dropna(subset=['VALUE'])
	df = df[(df["VALUE"] != ".")]
	df["VALUE"] = df["VALUE"].astype('float')
	plt.plot(df["VALUE"], lw=0.5)
	plt.show()

# PROBLEM 2
# function that generates the datetimeindex and plots data from paychecks.csv
def p2():
	# load data 
	data = pd.read_csv("paychecks.csv")
	# first and third fridays
	dates = pd.date_range(start='3/21/2008', periods=92, freq="2W")
	data.index = dates 
	plt.plot(data["1122.26"])
	plt.xlabel("Date")
	plt.ylabel("Paycheck Amount")
	plt.title("Paycheck Amount")
	plt.show()

# PROBLEM 3
# function that plots quarterly finances data 
def p3():
	# load data
	data = pd.read_csv("finances.csv")
	# quarterly basis
	dates = pd.period_range("1978-09", periods=84, freq="Q")
	data.index = dates
	# plot data
	data.drop([], axis=1).plot(linewidth=1)
	plt.xlabel("Date")
	plt.ylabel("Earnings and Expenses")
	plt.title("Earnings and Expenses per Quarter")
	plt.show()

# PROBLEM 4 
# function that calculates duration of visit times and plots the result
def p4():
	# load data
	data = pd.read_csv("website_traffic.csv")
	# make the enter and leave times a datetime object
	data["ENTER"] = pd.to_datetime(data["ENTER"], format="%Y-%m-%d %H:%M:%S")
	data["LEAVE"] = pd.to_datetime(data["LEAVE"], format="%Y-%m-%d %H:%M:%S")
	# calculate the time, convert to seconds, and set it as the index
	diff = data["LEAVE"] - data["ENTER"]
	dur = diff.dt.total_seconds()
	data.index = dur
	# calculate duration average min and hr 
	av = dur.sum() / len(data)
	av_min = av / 60.0
	av_hr = av / 360.0
	dur.drop([], axis=1).plot(linewidth=1)
	plt.show()

# PROBLEM 5
# function that calculates largest gain and loss
def p5():
	# load data
	data = pd.read_csv("DJIA.csv")
	# set index as datetime
	date_index = pd.to_datetime(data["DATE"], format="%Y-%m-%d")
	data.index = date_index
	df = data.drop(columns=["DATE"])
	# drop empty rows and change to floats
	df = df.dropna(subset=['VALUE'])
	df = df[(df["VALUE"] != ".")]
	df["VALUE"] = df["VALUE"].astype('float')
	# find difference for each day and order by value
	diff = df - df.shift(1)
	s_g = diff.sort_values("VALUE", ascending = False).index[0]
	s_l = diff.sort_values("VALUE", ascending = True).index[0]
	# find difference for each month and order by value
	m_data  = df.resample('M').first()
	m_diff = (m_data - m_data.shift(1)).dropna()
	m_g = m_diff.sort_values("VALUE", ascending = False).index[0]
	m_l = m_diff.sort_values("VALUE", ascending = True).index[0]
	print("The single day with the largest gain was " + str(s_g) + ". The single day with the largest loss was " + str(s_l) + ". The month with the largest gain was " + str(m_g) + ". The month the the largest loss was " + str(m_l) + ".")

# PROBLEM 6
# function that plots data from DJIA.csv
def p6(): 
	# load data
	data = pd.read_csv("DJIA.csv")
	# set index as datetime
	date_index = pd.to_datetime(data["DATE"], format="%Y-%m-%d")
	data.index = date_index
	df = data.drop(columns=["DATE"])
	# drop empty rows and change to floats
	df = df.dropna(subset=['VALUE'])
	df = df[(df["VALUE"] != ".")]
	df["VALUE"] = df["VALUE"].astype('float')
	# plot data
	windows = [30, 120, 365]
	plt.figure(figsize=(10, 8))
	plt.plot(df, alpha=0.5, label='actual')
	for w in windows:
		plt.plot(df.rolling(window=w).max(), alpha=0.5, label=f'window = {w}')
	plt.title('Rolling maximums')
	plt.legend()
	plt.show()