from Gradient_Descent import GradientDescent
from decimal import Decimal
import numpy as np
import pandas as pd

from Linear_regression import comput_cofficient

def main () :
	data = pd.read_csv("data.csv")
	print("Testing Gradient Descent")
	print("km", data["km"].to_numpy())
	x = data["km"].to_numpy().reshape(-1, 1)
	y = data["price"].to_numpy()
	
	gd = GradientDescent(x, y, Decimal('1.005'))
	thetas = gd.train_model()
 
	# print("Theta0: ", thetas[0])
	# print("Theta1: ", thetas[1])
 
	a, b = comput_cofficient(x, y)
	print("a: ", a, "b: ", b)


if __name__ == "__main__" :
	main()