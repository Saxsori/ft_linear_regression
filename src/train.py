from decimal import Decimal
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from manage_theta import save_thetas
from data_scaling import normalize_xy

def main () :
	data = pd.read_csv("data.csv")
 
	x, y = normalize_xy(data['km'], data['price'])
 
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
		
		tempTheta0 = learning_rate * (sum(estm - y) / Decimal(len(x)))
		tempTheta1 = learning_rate * (sum((estm - y) * x) / Decimal(len(x)))

		theta0 -= tempTheta0
		theta1 -= tempTheta1
  
		cur_mse = sum((estm - y) ** 2) / Decimal(len(x))
  
		if per_mse is not None and abs(per_mse - cur_mse) <= stopping_threshold:
			# print(f"{i} Converged", i)
			# print("MSE change: ", per_mse - cur_mse)
			print("theta0: ", theta0)
			print("theta1: ", theta1)
			break

		per_mse = cur_mse

		# print(f"Iteration {i}")
		# print("MSE change: ", per_mse - cur_mse)
		# print("Theta0: ", theta0)
		# print("Theta1: ", theta1)
		# print("---------------------------------")
  
	save_thetas(theta0, theta1)
	



if __name__ == "__main__" :
	main()