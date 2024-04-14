import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from manage_theta import extract_thetas
from data_scaling import normalize_xy, denormalize_xy

def calculate_r_squared ():

    data = pd.read_csv("data.csv")
    y = data['price']
    x = data['km']
    theta0, theta1 = extract_thetas()
    
    y_mean = np.mean(y)
    
    x_data, y_data = normalize_xy(data['km'], data['price'])

    y_pred = theta0 + (theta1 * x_data)
    
    x_data, y_pred = denormalize_xy(x_data, y_pred, data['km'], data['price'])


    tss = np.sum((y - y_mean) ** 2)
    
    rss = np.sum((y_pred - y) ** 2)
    
    r_squared = 1 - (rss / tss)
    
    return r_squared


def main () :
    print("The precision or goodness of fit of my algorithm: ", calculate_r_squared())
 
if __name__ == "__main__" :
	main()