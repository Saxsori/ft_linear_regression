import pandas as pd
import os


def extract_thetas():
    try:
        df = pd.read_csv("./Thetas.csv")
        theta0 = df['theta0'].values[0]
        theta1 = df['theta1'].values[0]

    except FileNotFoundError:
        theta0 = 0.0
        theta1 = 0.0
    
    return theta0, theta1


def save_thetas (theta0, theta1):
	data = {'theta0': [theta0], 'theta1': [theta1]}
	df = pd.DataFrame(data)

	csv_file = "./Thetas.csv"
	
	if os.path.exists(csv_file):
		os.remove(csv_file)
  
	df.to_csv(csv_file, index=False)
