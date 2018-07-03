# PANDAS3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data

# PROBLEM 1
# function that visualizes and describes datasets from pydataset
def p1():
	# load iris data
	iris = data("iris")
	# groupby species
	spec = iris.groupby("Species")
	# plot bar graph of species characteristics
	spec[["Sepal.Length", "Sepal.Width", "Petal.Length", "Petal.Width"]].mean().plot(kind="barh", title="Species Information")
	plt.xlabel("Mean Lengths and Widths")
	plt.ylabel("Species")
	plt.show()
	print("The Setosa species is the easiest to distinguish from the others because its petal widths and lengths are much smaller than those of other species.")
	print("I would identify the Setosa species by its much smaller petal lengths and widths. The Versicolor and Virginia species can be distinguished from each other by the Versicolor's smaller sepal lengths and widths as well as their smaller petal lengths and widths.")
	# load poisons data
	p = data("poisons")
	# groupby poison
	pois = p.groupby("poison")
	# plot bar graph of poison characteristics
	pois[["time"]].mean().plot(kind="barh", title="Poison Information")
	plt.xlabel("Time")
	plt.ylabel("Poison")
	plt.show()
	# groupby treatment
	treat = p.groupby("treat")
	# plot bar graph of treatment characteristics
	treat[["time"]].mean().plot(kind="barh", title="Treatment Information")
	plt.xlabel("Time")
	plt.ylabel("Treatment")
	plt.show()
	# group poison 1 by treatment
	one = pois.get_group(1)
	t_1 = one.groupby("treat")
	t_1[["time"]].mean().plot(kind="barh", title="Treatment for Poison 1")
	plt.xlabel("Time")
	plt.ylabel("Treatment")
	plt.show()
	# group poison 2 by treatment
	two = pois.get_group(2)
	t_2 = two.groupby("treat")
	t_2[["time"]].mean().plot(kind="barh", title="Treatment for Poison 2")
	plt.xlabel("Time")
	plt.ylabel("Treatment")
	plt.show()
	# group poison 2 by treatment
	three = pois.get_group(3)
	t_3 = three.groupby("treat")
	t_3[["time"]].mean().plot(kind="barh", title="Treatment for Poison 3")
	plt.xlabel("Time")
	plt.ylabel("Treatment")
	plt.show()
	print("The most deadly poison is poison 3. The most effective treatment is B. If I were poisoned, I'd choose treatment B because the time is the longest.")
	# load diamonds data
	d = data("diamonds")
	# group diamonds by color
	col = d.groupby("color")
	# graph color against price
	col[["price"]].mean().plot(kind="barh", title="Color and Price")
	plt.xlabel("Price")
	plt.ylabel("Color")
	plt.show()
	# group diamonds by cut
	cut = d.groupby("cut")
	# graph cut against price
	cut[["price"]].mean().plot(kind="barh", title="Cut and Price")
	plt.xlabel("Price")
	plt.ylabel("Cut")
	plt.show()
	# graph carat against price
	cut[["carat"]].mean().plot(kind="barh", title="Carat and Price")
	plt.xlabel("Price")
	plt.ylabel("Carat")
	plt.show()
	print("A premium cut is the most costly, then Fair, Good, Very Good, and lastly Ideal. The color J is the most costly, then I, H, G, F, D, and lastly E. Diamonds with color H and Fair cut sell for more than those with an ideal cut because they have, on average, fewer carats.")