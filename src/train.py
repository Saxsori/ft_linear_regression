from Gradient_Descent import GradientDescent
from decimal import Decimal
import numpy as np
import pandas as pd
import time
from Linear_regression import plot_line
from sklearn.preprocessing import StandardScaler


# Standardize the given data to have a mean of 0 and a standard deviation of 1.
# Standardizing the data makes the gradient descent algorithm converge faster, because the data is centered around 0 and has a standard deviation of 1.
# This makes the cost function more symmetric and easier to minimize.
# The standardization formula is: (x - mean) / standard deviation
# where x is the data, mean is the mean of the data, and standard deviation is the standard deviation of the data.
# The mean and standard deviation are calculated using the formula:
# mean = sum(x) / n, where n is the number of data points
# standard deviation = sqrt(sum((x - mean)^2) / n)
# The standardization formula is applied to each data point in the data.
# The data is standardized using the StandardScaler class from the scikit-learn library.
# The StandardScaler class has a fit_transform method that standardizes the data.
# The fit_transform method takes the data as input and returns the standardized data.
# The standardized data is then used to train the model.






def main () :
	data = pd.read_csv("data.csv")
	print("Testing Gradient Descent")
	
	ss = StandardScaler()
	
	stand_data = ss.fit_transform(data)
	
	print("standardized Data: ", data)
	
	x = stand_data[:, 0]
	y = stand_data[:, 1]
	
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
			print("Converged")
			print("MSE change: ", per_mse - cur_mse)
			print("theta0: ", theta0)
			print("theta1: ", theta1)
			break

		per_mse = cur_mse


		print("MSE change: ", per_mse - cur_mse)
		print("Theta0: ", theta0)
		print("Theta1: ", theta1)
		print("---------------------------------")
		time.sleep(1)
  

	# # convert Decimal to float
	theta0 = float(theta0)
	theta1 = float(theta1)
 
	print("theta0: ", theta0)
	
	x_test = x[11]
 
	originalTheta0 = 6332.16666667
	originalTheta1 = theta1 * data["price"].std() / data["km"].std()
 
	y_pred = theta0 + (theta1 * float(x[13]))
	print("y_pred: ", y_pred)
	
	#append the predicted values to the y column
	
	# ys = StandardScaler()
	
	# yrange = np.append(y, y_pred)
	
	#reshape the yrange to 2D array
	# yrange = yrange.reshape(-1, 1)
	
	
	
	# plot_line(originalTheta1, originalTheta0, data["km"], data["price"])
	
 
	# data = ss.inverse_transform(data)
	
	# print("De-standardized Data: ", data)
	
	
	# destandardize the data
	
	
	# print("De-standardized x: ", xs)
	# print("De-standardized y: ", ys)
	


def test () :
	data = pd.read_csv("data.csv")
	
	xs = StandardScaler()
	ys = StandardScaler()
	ss = StandardScaler()

	data = ss.fit_transform(data)
	
	print("Standardized Data: ", data)

	data = pd.read_csv("data.csv")

	x = data["km"].values.reshape(-1, 1)
	y = data["price"].values.reshape(-1, 1)
	
	standrise_x = xs.fit_transform(x)
	standrise_y = ys.fit_transform(y)
	
	print("Standardized x: ", standrise_x)
	print("Standardized y: ", standrise_y)
	
	
	# destandardize the data
	# destandrise_x = xs.inverse_transform(standrise_x)
	# destandrise_y = ys.inverse_transform(standrise_y)
	
	# print("De-standardized x: ", destandrise_x)
	# print("De-standardized y: ", destandrise_y)
 
 
	new_y = np.append(standrise_y.reshape(-1), -2.3027420237579683e-16)
 
	new_y = new_y.reshape(-1, 1)
 
	destandrise_y = ys.inverse_transform(new_y)
 
	print("De-standardized y: ", destandrise_y)
 
	
 
	
	
 
	


if __name__ == "__main__" :
	main()