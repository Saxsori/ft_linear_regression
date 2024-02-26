class GradientDescent :
    def __init__(self, x, y) -> None:
        self.theta0 = 0
        self.theta1 = 0
        self.x = x
        self.y = y
        self.n = len(x)
        self.learning_rate = 0.01
        self.cur_mse = 0
        self.default_mse = 0.000000001
    
    def estimate(self, x) :
        return self.theta0  + (self.theta1 * x)
    
    
    def compute_mse(self) : 
        diff = 0
        for i in range(self.n) :
            diff += (self.estimate(self.theta1, self.theta2, self.x[i]) - self.y[i]) ** 2
        return diff / self.n


def testGradientDescent () :
	print("Testing Gradient Descent")
	gd = GradientDescent()
	print("gd: ", gd)
    


if __name__ == "__main__" :
	testGradientDescent()