import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from manage_theta import extract_thetas
from data_scaling import normalize_xy, normalize_value, denormalize_value, denormalize_xy



def plot_line (theta0: float, theta1: float):

    data = pd.read_csv("data.csv")
    
    # convert to list
    x = data['km']
    y = data['price']
    
    x_data, y_data = normalize_xy(x, y)


    x_values = np.linspace(np.min(x_data), np.max(y_data), 100)
    y_values = theta0 + (theta1 * x_values)
    
        
    x_values, y_values = denormalize_xy(x_values, y_values, x, y)
    
    x_data, y_data = denormalize_xy(x_data, y_data, x, y)

    plt.scatter(x_data, y_data, color='blue', label='Data points')
    plt.plot(x_values, y_values, color='red', label='Regression line')
    plt.show()






def predict ():

    data = pd.read_csv("data.csv")
    
    theta0, theta1 = extract_thetas()
    
    if theta0 == 0.0 and theta1 == 0.0:
        print("Please train the model first.")
        return
    
    # prompt user for input
    x_value = float(input("Enter the number of mileage kilometers: "))
    
    x_value = normalize_value(x_value, data['km'].tolist())
    
    
    y_value = theta0 + (theta1 * x_value)
    
    y_value = denormalize_value(y_value, data['price'].tolist())
    
    
    print("Predicted price: ", y_value)
    
    plot_line(theta0, theta1)
    
    


if __name__ == "__main__" :
	predict()