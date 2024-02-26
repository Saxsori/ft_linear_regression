import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

def comput_cofficient(x , y):
    model = LinearRegression()
    model.fit(x, y)
    a = model.coef_[0]
    b = model.intercept_
    return a, b

def plot_line (a, b, x, y):
    x_values = np.linspace(np.min(x), np.max(x), 100)
    y_values = a * x_values + b
    plt.scatter(x, y, color='blue', label='Data points')
    plt.plot(x_values, y_values, color='red', label='Regression line')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Linear Regression')
    plt.legend()
    plt.grid(True)
    plt.show()

def testLinearRegression():
    try:
		# data need to be reshaped to 2D array, because sklearn LinearRegression model expects 2D array for x
        x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
        y = np.array([2, 3, 5, 7, 11])

        a, b = comput_cofficient(x, y)
        print("a: ", a, "b: ", b)
        plot_line(a, b, x, y)

    except Exception as e:
        print("Error: ", e)


if __name__ == "__main__" :
	testLinearRegression()
