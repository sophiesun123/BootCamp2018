# PANDAS1

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# PROBLEM 1
# function that takes n entries and sets entries divisible by 3 to 0
def p1():
	# initialize series and index
	ind = []
	ser = []
	# iterate over i
	for i in range(26):
		# get index values
		ind.append(i * 2)
		# if divisible by 3, set to 0
		if (i ** 2 - 1) % 3 == 0:
			ser.append(0)
		else:
			ser.append(i ** 2 - 1)
	return pd.Series(ser, index=ind)

# PROBLEM 2
# function that models volatility of stocks
def p2(p, d=100):
	ser = []
	# date index
	ind = pd.date_range("7/1/2000", "12/31/2000", freq='D')
	# draw from Bernoulli distribution when iterating over dates
	for i in range(len(ind)):
		if np.random.binomial(1, p) == 0:
			ser.append(-1)
		else:
			ser.append(1)
	s = pd.Series(ser,index=ind)
	# set first draw to initial amount
	s[0] = d
	# sum entries cumulatively, setting negative values to 0
	s = s.cumsum()
	for i in range(len(ind)):
		if s[i] < 0:
			s[i] == 0
	s.plot()
	plt.show()

# build toy data for SQL operations
name = ['Mylan', 'Regan', 'Justin', 'Jess', 'Jason', 'Remi', 'Matt', 'Alexander', 'JeanMarie']
sex = ['M', 'F', 'M', 'F', 'M', 'F', 'M', 'M', 'F']
age = [20, 21, 18, 22, 19, 20, 20, 19, 20]
rank = ['Sp', 'Se', 'Fr', 'Se', 'Sp', 'J', 'J', 'J', 'Se']
ID = range(9)
aid = ['y', 'n', 'n', 'y', 'n', 'n', 'n', 'y', 'n']
GPA = [3.8, 3.5, 3.0, 3.9, 2.8, 2.9, 3.8, 3.4, 3.7]
mathID = [0, 1, 5, 6, 3]
mathGd = [4.0, 3.0, 3.5, 3.0, 4.0]
major = ['y', 'n', 'y', 'n', 'n']
studentInfo = pd.DataFrame({'ID': ID, 'Name': name, 'Sex': sex, 'Age': age,'Class': rank})
otherInfo = pd.DataFrame({'ID': ID, 'GPA': GPA, 'Financial_Aid': aid})
mathInfo = pd.DataFrame({'ID': mathID, 'Grade': mathGd, 'Math_Major': major})

# PROBLEM 3
# function that uses SQL
def p3():
	# execute SQL query:
	# SELECT ID, Name from studentInfo WHERE Age > 19 AND Sex = 'M'
	studentInfo[(studentInfo['Age'] > 19) & (studentInfo['Sex']=='M')][['ID', "Name"]])

# PROBLEM 4
# function that creates a df with the ID, age, and GPA of all males
def p4():
	pd.merge(studentInfo,otherInfo, on='ID')[['ID', 'Age', 'GPA']]

# PROBLEM 5
# fucntion that analyzes crime data
def p5():
	# load data
	df = pd.read_csv("crime_data.txt", header=0, index_col=0)
	# create a new column with crime rate information
	df['Crime Rate'] = df["Total"] / df["Population"]
	# sort crime rate by descending order
	desc = df.sort_values('Crime Rate', ascending=False)
	# list 5 years with highest crime rate
	lst = desc.index.values.tolist()
	print("The years with the highest crime rates were: " + str(lst[0:5]))
	# plot crime rate as a function of year
	plt.plot(df.index, df["Crime Rate"])
	plt.show()
	# average number of total and burglary crimes between 1960 and 2012
	tot = df[(df.index > 1960) & (df.index < 2012)][['Total', 'Burglary']]
	av_tot = tot["Total"].sum() / len(tot["Total"])
	av_bur = tot["Burglary"].sum() / len(tot["Total"])
	# years for which crimes was below average but burglaries was above average
	crimes = df[(df["Total"] < av_tot) & (df["Burglary"] > av_bur)]
	yrs = crimes.index.values.tolist()
	print("The years with total crimes below average but burglaries above average were: " + str(yrs))
	# plot murders as a function of population
	plt.plot(df["Murder"], df["Population"])
	plt.show()
	# select pop, violent, robbery for 1980s and save into crime_subset.csv
	new = df[(df.index > 1979) & (df.index < 1990)][["Population", "Violent", "Robbery"]]
	new.to_csv("crime_subset.csv")

# PROBLEM 6
# function that analyzes titanic data
def p6():
	# load data
	data = pd.read_csv("titanic.csv", index_col=0)
	# drop columns
	df = data.drop(columns=["Sibsp", "Parch", "Cabin", "Boat", "Body", "home.dest"])
	# drop entries without data in "Survived" column and change to True or False
	df.dropna(subset=["Survived"])
	df["Survived"] = df["Survived"].replace([1.0], True)
	df["Survived"] = df["Survived"].replace([0.0], False)
	# replace null entries with average age
	av_age = df["Age"].sum() / len(df["Age"])
	df["Age"] = df["Age"].replace([np.nan],av_age)
	df.to_csv("titanic_clean.csv")
	# number and percentage of survivors
	s = df["Survived"].sum()
	p = s / len(df["Survived"])
	# average ticket price and most expensive ticket cost
	a = df["Fare"].sum() / len(df["Fare"])
	exp = df.sort_values('Fare', ascending=False)
	e = exp.iloc[0]["Fare"]
	# sort people by descending age 
	desc_age = df.sort_values("Age", ascending=False)
	# get oldest survivor
	sur = desc_age[desc_age["Survived"] == True]["Age"]
	os = sur.iloc[0]
	# get oldest non-survivor
	nonsur = desc_age[desc_age["Survived"] == False]["Age"]
	on = nonsur.iloc[0]
	# sort people by ascending age
	asc_age = df.sort_values("Age", ascending=True)
	# get youngest survivor
	sur = asc_age[asc_age["Survived"] == True]["Age"]
	ys = sur.iloc[0]
	# get youngest non-survivor
	nonsur = asc_age[asc_age["Survived"] == False]["Age"]
	yn = nonsur.iloc[0]
	print(str(s) + " people survived. " + str(p) + "percent of passengers survived. The average price of a ticket was $" + str(a) + ". The most expensive ticket costed $" + str(e) + ". The oldest survivor and non-survivor was " + str(os) + " and " + str(on) + ". The youngest survivor and non-survivor was " + str(ys) + " and " + str(yn) + ".")
