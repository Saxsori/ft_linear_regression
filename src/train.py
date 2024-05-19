from decimal import Decimal
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from utils.manage_theta import save_thetas
from utils.data_scaling import normalize_xy

def main () :
    
	try:
		data = pd.read_csv("data.csv")
	except FileNotFoundError:
		print("Please Add data.csv file to the same directory as this program -_-.")
		return

	try :
		x, y = normalize_xy(data['km'], data['price'])
	except KeyError :
		print("Please make sure the csv file has the correct column names.")
		return
 
	x = np.array([Decimal(i) for i in x])
	y = np.array([Decimal(i) for i in y])

	
	stopping_threshold = Decimal('1e-15')
	theta1 = Decimal('0.0')
	theta0 = Decimal('0.0')
	learning_rate = Decimal('1.01')
	tempTheta0 = Decimal('0.0')
	tempTheta1 = Decimal('0.0')
	cur_mse = Decimal('0.0')
	per_mse = None
	
	for i in range(1000) :
		estm = theta0 + (theta1 * x)
		
		# learning rate is the step size, the bigger it is, determines the step size at each iteration while moving towards a minimum of the loss function
		tempTheta0 = learning_rate * (sum(estm - y) / Decimal(len(x)))
		tempTheta1 = learning_rate * (sum((estm - y) * x) / Decimal(len(x)))

		# update thetas, cuz we want to minimize the cost function
		theta0 -= tempTheta0
		theta1 -= tempTheta1
  
		cur_mse = sum((estm - y) ** 2) / Decimal(len(x))
  
		# mse is the mean squared error, which is the average of the squared errors
		# this is the cost function, and we want to minimize it, 
  		# cuz the smaller it is, the better the model, the better the predictions
		if per_mse is not None and abs(per_mse - cur_mse) <= stopping_threshold:
			print("theta0: ", theta0)
			print("theta1: ", theta1)
			break

		per_mse = cur_mse
  
	save_thetas(theta0, theta1)
	



if __name__ == "__main__" :
	main()