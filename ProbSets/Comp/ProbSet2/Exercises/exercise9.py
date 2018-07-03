# EXERCISE 9

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from fredapi import Fred
fred = Fred(api_key='16fc433e0cb217bb8cb94bf76b981f2f') 

# function that visualizes data from payems.csv
# much help from Natasha
def a():
	n_series = 14
	payems = pd.read_csv('payems.csv', index_col=0)
	# century change
	y2k = payems.index.get_loc('1/1/00')  
	before = payems[:y2k]
	after = payems[y2k:]
	# functions for modifying dates
	repl_1 = lambda s: '19' + s.group(0)
	repl_2 = lambda s: '20' + s.group(0)
	before.index = before.index.str.replace('(\d\d)$', repl_1)
	after.index = after.index.str.replace('(\d\d)$', repl_2)
	payems = pd.concat([before, after])
	payems.index = pd.to_datetime(payems.index)
	# resample for monthly data
	payems = payems.resample('MS').ffill()  
	# find recessions
	indicator = fred.get_series('USREC')
	diff = indicator.diff()
	peak_dates = diff[diff == 1][-n_series:].index
	start_dates = peak_dates - pd.offsets.DateOffset(years=1)
	end_dates = start_dates + pd.offsets.DateOffset(years=10, months=5)
	series = []
	# series of recessions
	for start, end in zip(start_dates, end_dates):
    	series.append(payems[str(start):str(end)])
	new_series = []
	for i in range(n_series):
		p = peak_dates[i]
		norm = series[i].loc[p]
		norm_series = series[i] / norm
		# Create an index range with 0 at a series value equal to 1
		after = norm_series[p:]
		before = norm_series[:p]
		before.index = range(-len(before)+1, 1)
		after.index = range(1, len(after)+1)
		new_series.append(pd.concat([before, after]))
	# plot 
	plt.figure(figsize=(10, 8))
	for s, peak_date in zip(new_series, peak_dates):
		if peak_date.year == 1929:
			plt.plot(s, label=peak_date.strftime('%b %Y'), alpha=0.8, c='k', lw=3)
		elif peak_date.year == 2008:
			plt.plot(s, label=peak_date.strftime('%b %Y'), alpha=0.8, c='r', lw=3)
		else:
			plt.plot(s, label=peak_date.strftime('%b %Y'), alpha=0.8)
	plt.axvline(x=1, c='gray', ls='--', alpha=0.8)
	plt.axhline(y=1, c='gray', ls='--', alpha=0.8)
	plt.legend(bbox_to_anchor=(1.18, 1.01), title='Recession start')
	plt.ylabel('Jobs/peak')
	plt.xlabel('Time from peak')
	plt.xticks(np.arange(-10, 120, 11), 
			['-1yr', 'peak', '+1yr', '+2yr', '+3yr', '+4yr', '+5yr', '+6yr', '+7yr', '+8yr', '+9yr', '+10yr'])
	plt.show()