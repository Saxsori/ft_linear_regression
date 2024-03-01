import matplotlib.pyplot as plt
import numpy as np
from decimal import Decimal
from Linear_regression import plot_line
class GradientDescent :
    def __init__(self, xs: np.ndarray, ys: np.ndarray, lr: Decimal) -> None:
        self.x = xs
        self.y = ys
        self.n = len(xs)
        self.learning_rate = lr
        self._default_mse = Decimal('1e-40')
    
    @staticmethod
    def estimate(theta0, theta1: Decimal, x: Decimal) -> Decimal :
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
        tempTheta0 = Decimal('0.0')
        for i in range(self.n):
            tempTheta0 += (self.estimate(theta0, theta1, self.x[i]) - self.y[i])
        return (self.learning_rate * tempTheta0) / Decimal(self.n)

    
    def get_default_mse(self) -> Decimal:
        return self._default_mse
    
    def set_default_mse(self, default_mse: Decimal) -> Decimal:
        self._default_mse = default_mse
    
    default_mse = property(get_default_mse, set_default_mse, doc="This is the default_mse")
    
    def train_model(self) -> list:
        cur_mse = Decimal('0.0')
        theta0 = Decimal('0.0')
        theta1 = Decimal('0.0')
        
        per_mse = None
        while (1) :
            theta0 -= self.compute_theta0(theta0, theta1)
            theta1 -= self.compute_theta1(theta0, theta1)
            cur_mse = self.compute_mse(theta0, theta1)
            if per_mse is not None and (per_mse - cur_mse) <= self.default_mse:
                break
            per_mse = cur_mse
            print("MSE change: ", per_mse - cur_mse)
            print("cur_mse: ", cur_mse)
            print("per_mse: ", per_mse)
            print("Theta0: ", theta0)
            print("Theta1: ", theta1)
        return [theta0, theta1]
        



def testGradientDescent () :
	print("Testing Gradient Descent")
	xs = np.array([1, 2, 3, 4, 7, 9, 5]).reshape(-1, 1)
	ys = np.array([2, 3, 5, 7, 7, 99, 11])
 
	# print(type(xs))
	
	

	gd = GradientDescent(xs, ys, Decimal('0.001'))
	
	print(gd.train_model())
	



if __name__ == "__main__" :
	testGradientDescent()
