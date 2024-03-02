from decimal import Decimal
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main () :
	data = pd.read_csv("data.csv")
 
	x = data['km']
	y = data['price']
	
	# normalize the data
	x = (x - x.min()) / (x.max() - x.min())
	y = (y - y.min()) / (y.max() - y.min())
 
	# convert to numpy array elements to Decimal
	x = [Decimal(i) for i in x]
	y = [Decimal(i) for i in y]
 
	# convert Decimalto numpy array
	x = np.array(x)
	y = np.array(y)
 
	print("x: ", x)
	print("y: ", y)

 
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
			print(f"{i} Converged", i)
			print("MSE change: ", per_mse - cur_mse)
			print("theta0: ", theta0)
			print("theta1: ", theta1)
			break

		per_mse = cur_mse

		print(f"Iteration {i}")
		print("MSE change: ", per_mse - cur_mse)
		print("Theta0: ", theta0)
		print("Theta1: ", theta1)
		print("---------------------------------")
  
	
  
	# convert to float 
	theta0 = float(theta0)
	theta1 = float(theta1)
	
	# convert x to float
	x = [float(i) for i in x]
	y = [float(i) for i in y]

 
	# line points
	x_values = np.linspace(np.min(x), np.max(x), 100)
	y_values = theta0 + (theta1 * x_values)
	
	# unnormalize the x_values and y_values
	x_values = x_values * (max(data['km']) - min(data['km'])) + min(data['km'])
	y_values = y_values * (max(data['price']) - min(data['price'])) + min(data['price'])
	
	
	# convert all data to float
	xs = np.array(x) * (max(data['km']) - min(data['km'])) + min(data['km'])
	ys = np.array(y) * (max(data['price']) - min(data['price'])) + min(data['price'])
 
	# plot the line
	plt.scatter(xs, ys, color='blue', label='Data points')
	plt.plot(x_values, y_values, color='red', label='Regression line')
	plt.show()
	
  



if __name__ == "__main__" :
	main()