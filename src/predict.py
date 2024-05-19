import pandas as pd
import numpy as np
import matplotlib as mpl
mpl.use("GTK3Agg") # or mpl.use("GTK3Cairo")
mpl.get_backend()
import matplotlib.pyplot as plt # --> this will throw the error 'Namespace Gtk not available'
from utils.manage_theta import extract_thetas
from utils.data_scaling import normalize_xy, normalize_value, denormalize_value, denormalize_xy



def plot_line (theta0: float, theta1: float):

    data = pd.read_csv("data.csv")
    
    # convert to list
    x = data['km']
    y = data['price']
    
    x_data, y_data = normalize_xy(x, y)

    x_values = np.linspace(np.min(x_data), np.max(y_data), 100)
    y_values = theta0 + (theta1 * x_values)
    
        
    x_values, y_values = denormalize_xy(x_values, y_values, x, y)
    print("here")
    
    x_data, y_data = denormalize_xy(x_data, y_data, x, y)

    plt.scatter(x_data, y_data, color='blue', label='Data points')
    plt.plot(x_values, y_values, color='red', label='Regression line')
    plt.show()






def predict ():
    
    try:
        data = pd.read_csv("data.csv")
    except FileNotFoundError:
        print("Please Add data.csv file to the same directory as this program -_-.")
        return
    
    theta0, theta1 = extract_thetas()
    
    untrained_flag = False
    
    if theta0 == 0.0 and theta1 == 0.0:
        print("Please train the model first.")
        untrained_flag = True
    
    try:
        x_value = float(input("Enter the number of mileage kilometers: "))
        if (x_value < 0):
            print("Milage kilometers can't be negative. Please enter a positive number.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if untrained_flag:
        print("Value doesn't need to be normalized, as the model hasn't been trained yet.")
    else:
        x_value = normalize_value(x_value, data['km'].tolist())
    
    y_value = theta0 + (theta1 * x_value)
    
    if untrained_flag == False:
        y_value = denormalize_value(y_value, data['price'].tolist())
    
    
    print("Predicted price: ", y_value)
    
    if untrained_flag == False:
    	plot_line(theta0, theta1)
    
    


if __name__ == "__main__" :
	predict()