import matplotlib.pyplot as plt
import numpy as np
from decimal import Decimal
from Linear_regression import plot_line
class GradientDescent :
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.n = len(x)
        self.learning_rate = Decimal('0.001')
        self._default_mse = Decimal('1e-40')
    
    @staticmethod
    def estimate(theta0, theta1: Decimal, x) -> Decimal :
        return theta0  + (theta1 * x)

    def compute_mse(self, theta0: Decimal, theta1: Decimal) -> Decimal:
        diff = 0
        for i in range(self.n) :
            diff += ((self.estimate(theta0, theta1, self.x[i]) - self.y[i]) ** 2)
        return diff / (self.n * 2)
    
    def compute_theta1 (self, theta0: Decimal, theta1: Decimal) -> Decimal:
        tempTheta1 = Decimal('0.0')
        for i in range(self.n) :
            tempTheta1 += (self.estimate(theta0, theta1, self.x[i]) - self.y[i]) * self.x[i]
        return (self.learning_rate * tempTheta1) / Decimal(self.n)
    
    def compute_theta0(self, theta0: Decimal, theta1: Decimal) -> Decimal:
        tempTheta0 = Decimal('0.0')  # Initialize tempTheta0 as a Decimal
        for i in range(self.n):
            tempTheta0 += (self.estimate(theta0, theta1, self.x[i]) - self.y[i])
        return (self.learning_rate * tempTheta0) / Decimal(self.n)

    
    def get_default_mse(self) -> Decimal:
        return self._default_mse
    
    def set_default_mse(self, default_mse: Decimal) -> Decimal:
        self._default_mse = default_mse
    
    default_mse = property(get_default_mse, set_default_mse, doc="This is the default_mse")

	# def train (self, )

def testGradientDescent () :
	print("Testing Gradient Descent")
	x = np.array([1, 2, 3, 4, 7, 9, 5]).reshape(-1, 1)
	y = np.array([2, 3, 5, 7, 7, 99, 11])

	gd = GradientDescent(x, y)
	print("gd: ", gd)
	cur_mse = Decimal('0.0')
	theta0 = Decimal('0.0')
	theta1 = Decimal('0.0')
	
	per_mse = None
	while (1) :
		theta0 -= gd.compute_theta0(theta0, theta1)
		theta1 -= gd.compute_theta1(theta0, theta1)
		cur_mse = gd.compute_mse(theta0, theta1)
		if per_mse is not None and (per_mse - cur_mse) <= gd.default_mse:
			print("MSE change: ", per_mse - cur_mse)
			print("cur_mse: ", cur_mse)
			print("per_mse: ", per_mse)
			print("Theta0: ", theta0)
			print("Theta1: ", theta1)
			break
		per_mse = cur_mse



if __name__ == "__main__" :
	testGradientDescent()
