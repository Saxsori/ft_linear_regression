import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from utils.manage_theta import extract_thetas
from utils.data_scaling import normalize_xy, denormalize_xy

def calculate_r_squared (theta0, theta1):

	try:
		data = pd.read_csv("data.csv")
	except FileNotFoundError:
		print("Please Add data.csv file to the same directory as this program -_-.")
		return 0
	
	try :
		y = data['price']
		x = data['km']
	except KeyError :
		print("Please make sure the csv file has the correct column names.")
		return 0
    

	y_mean = np.mean(y)
    
	x_data, y_data = normalize_xy(data['km'], data['price'])

	y_pred = theta0 + (theta1 * x_data)
    
	x_data, y_pred = denormalize_xy(x_data, y_pred, data['km'], data['price'])


	tss = np.sum((y - y_mean) ** 2)
    
	rss = np.sum((y_pred - y) ** 2)
    
	r_squared = 1 - (rss / tss)
    
	return r_squared


def main () :
	theta0, theta1 = extract_thetas()
    
	if theta0 == 0.0 and theta1 == 0.0:
		print("Please train the model first.")
		return
	print("The precision or goodness of fit of my algorithm: ", calculate_r_squared(theta0, theta1))
 
if __name__ == "__main__" :
	main()
 