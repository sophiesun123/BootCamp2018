# PANDAS2

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data

# PROBLEM 1
# function that visualizes and describes 5 datasets in pydataset
def p1():
	# load road data
	road = data("road")
	# plot deaths, popden, and drivers against index
	road.drop(["rural", "temp", "fuel"], axis=1).plot(linewidth=1)
	plt.title("Deaths, Population Density, and Drivers vs Location - Road")
	plt.xlabel("States")
	plt.ylabel("Number of People")
	plt.show()
	# plot temperature against index
	road.drop(["popden", "deaths", "drivers", "fuel", "rural"], axis=1).plot(linewidth=1)
	plt.title("Temperature vs Location - Road")
	plt.xlabel("States")
	plt.ylabel("Temperature")
	plt.show()
	# load Arbuthnot data
	arb = data("Arbuthnot")
	arb.index = arb["Year"]
	# plot males and females against year
	arb.plot(y=["Males", "Females"])
	plt.title("Males and Females vs Year - Arbuthnot")
	plt.xlabel("Year")
	plt.ylabel("Number of People")
	plt.show()
	arb.drop(["Males", "Females", "Year", "Ratio", "Total"], axis=1).plot(linewidth=1)
	# plot plague and mortality against year
	plt.title("Plague and Mortality vs Year - Arbuthnot")
	plt.xlabel("Year")
	plt.ylabel("Number of People")
	plt.show()
	# load birthdeathrates data
	birth = data("birthdeathrates")
	birth.drop([], axis=1).plot(linewidth=1)
	# plot birth and death rates against country
	plt.title("Birth and Death Rates vs Country - Birthdeathrates")
	plt.xlabel("Country")
	plt.ylabel("Rates")
	plt.show()
	# plot birth and death rates against country
	birth.plot(kind="hist", y=["birth", "death"],bins=20, alpha=.7, rot=30)
	plt.title("Birth and Death Rates vs Country - Birthdeathrates")
	plt.xlabel("Country")
	plt.ylabel("Rates")
	plt.show()
	# load bwt data
	bwt = data("birthwt")
	# plot age against birthweight
	plt.scatter(bwt["age"], bwt["bwt"], alpha=.5, edgecolor='none')
	plt.title("Age vs Birthweight - bwt")
	plt.xlabel("Age")
	plt.ylabel("Birthweight")
	plt.show()
	# plot lwt against birthweight
	plt.scatter(bwt["lwt"], bwt["bwt"], alpha=.5, edgecolor='none')
	plt.title("Lwt vs Birthweight - bwt")
	plt.xlabel("Lwt")
	plt.ylabel("Birthweight")
	plt.show()
	# load bfeed data
	bfeed = data("bfeed")
	# plot duration against agemth
	plt.scatter(bfeed["duration"], bfeed["agemth"], alpha=.5, edgecolor='none')
	plt.title("Duration vs Age - bfeed")
	plt.xlabel("Duration")
	plt.ylabel("Age")
	plt.show()
	# plot duration against yschool
	plt.scatter(bfeed["duration"], bfeed["yschool"], alpha=.5, edgecolor='none')
	plt.title("Duration vs Yschool - bfeed")
	plt.xlabel("Duration")
	plt.ylabel("Yschool")
	plt.show()