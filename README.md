# ft_linear_regression

# Introdution
Machine learning is a subset of artificial intelligence that focuses on building systems that learn from and make decisions based on data. This project showcases a fundamental machine learning technique known as linear regression, implemented using the Gradient Descent algorithm. The goal is to understand the relationship between dependent and independent variables in a dataset and use this relationship to make predictions.

## What is Linear Regression?
Linear regression is an algorithm that provides a linear relationship between an independent variable and a dependent variable to predict the outcome of future events. It is a statistical method used in data science and machine learning for predictive analysis.



The goal is to find the formula (or equation) of a line to predict the value of the output (dependent/outcome) variable based on the input (independent/predictor) variable with maximum accuracy or minimum error.


![image](https://github.com/Saxsori/ft_linear_regression/assets/92129820/0188ce10-9c24-4e3e-9b2e-306e136ff62c)


```
In the above figure,

X-axis: Independent variable
Y-axis: Output / dependent variable
Line of regression: Best fit line for a model
```

Line is plotted for the given data points that suitably fit all the issues. Hence, it is called the ‘best fit line.’ The goal of the linear regression algorithm is to find this best fit line seen in the above figure.


Suppose the equation of the best-fitted line is given by 

```
y = ax + b

Where,

y: dependent variable
x: independent variable
a: slope or regression coefficient
b: y-intercept
```
then, the regression coefficients formula is given as follows:

![image](https://github.com/Saxsori/ft_linear_regression/assets/92129820/941bf7be-1536-4e0c-96f5-f5360016e86c) 

```
here,

n refers to the number of data points in the given data sets.
```

# Gradient Descent

Gradient descent is one of the most famous techniques in machine learning and used for training all sorts of neural networks. But gradient descent can not only be used to train neural networks, but many more machine learning models. In particular, gradient descent can be used to train a linear regression model!


--------------


An iterative optimization algorithm that tries to find the optimum value (Minimum/Maximum) of an objective function. It is one of the most used optimization techniques in machine learning projects for updating the parameters of a model in order to minimize a cost function. 

```math
\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
```

Where,
```math
\hat{y}_i = \theta_0 + \theta_1x_i 
```


The main aim of gradient descent is to find the best parameters of a model that give the highest accuracy on training. By parameters, I mean the coefficients or weights $`(\theta_0, \theta_0)`$ in the linear regression model that determines the strength and direction of the relationship between the independent variables (features) and the dependent variable (target).


``` math
\theta_0 = \theta_0 - \alpha \frac{1}{m} \sum_{i=1}^{m} (\hat{y_i} - y_i)
```

```math
\theta_1 := \theta_1 - \alpha \frac{1}{m} \sum_{i=1}^{m} (\hat{y_i} - y_i x_i)
```




```
Where,

a: learning rate
m: total data
𝜃0: bias, y-intercept
𝜃1: Weight, slope
```

## Step-by-Step Explanation of Gradient Descent

1. Initialize Parameters
   
Start with initial values for the parameters, which can be set to zeros.

```
𝜃0 = 0
𝜃1 = 0
```

2. Compute Gradients



``` math
\frac{\partial}{\partial \theta_0} = \frac{1}{m} \sum_{i=1}^{m} (\hat{y_i} - y_i)
```

```math
​\frac{\partial}{\partial \theta_1} = \frac{1}{m} \sum_{i=1}^{m} (\hat{y_i} - y_i x_i)
```

where, 

```math
\hat{y}^{(i)} = \theta_0 + \theta_1x_i
```



```python
pred = theta0 + (theta1 * x)
tempTheta0 = (sum(pred) - y) / Decimal(len(x)))
tempTheta1 = (sum(pred) - y) * x) / Decimal(len(x)))
```


4. Update Parameters
``` math
\theta_0:= \theta_0 - \alpha \frac{\partial}{\partial \theta_0} 
```

```math
​\theta_1:= \theta_1 - \alpha \frac{\partial}{\partial \theta_1}
```

```python
theta0 -= learning_rate * tempTheta0
theta1 -= learning_rate * tempTheta1
```


6. Calculate Cost Function

```math
\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
```


```python
mse = sum(((theta0 + (theta1 * x)) - y) ** 2) / Decimal(len(x))
```


8. Repeat
- Repeat steps 2-5 for a number of iterations of your choice, or infinitely until the parameters converge or reach a predefined stopping threshold.
- Convergence means that the parameters are no longer changing significantly with further iterations, indicating that the algorithm has found the minimum of the cost function.


## OverFitting
Overfitting occurs when a model learns the training data too well, resulting in poor performance on new, unseen data. Overfitting is not acceptable because it compromises the model’s ability to generalize from the training data to other data.


In this implementation, the stopping threshold and learning rate are used to avoid overfitting:

- Stopping Threshold: By defining a threshold for minimal changes in the cost function or parameter values, we can prevent the model from continuing to learn the noise in the training data, which helps avoid overfitting.
- Learning Rate (α): A carefully chosen learning rate ensures that the model learns efficiently without making too large updates to the parameters, which can cause overfitting or divergence.


## Customizing Parameters
The learning rate 𝛼, number of iterations, and stopping threshold can be defined by the developer. These hyperparameters may vary from model to model based on the specific requirements and nature of the data.

- Learning Rate (𝛼): Controls the size of the steps taken to reach the minimum of the cost function.
- Number of Iterations: Defines how many times the gradient descent steps are repeated.
- Stopping Threshold: Determines when to stop the iterations based on minimal change in the cost function or parameter values.

These settings can be adjusted to optimize the model’s performance and ensure it converges appropriately without overfitting.

## Normalization
Before starting the gradient descent algorithm, data needs to be normalized. Normalization scales the features of your data to a specific range, often [0, 1] or [-1, 1], to ensure they have a consistent scale.

#### Normalization Equation

For min-max normalization:

```math
x_{\text{norm}} = \frac{x - \min(x)}{\max(x) - \min(x)} 
```

#### Benefits for Gradient Descent

1. **Faster Convergence**: Normalized features lead to more efficient gradient descent steps, reducing the number of iterations needed.
2. **Numerical Stability**: Prevents overflow/underflow issues by keeping feature values within a manageable range.
3. **Equal Influence**: Ensures all features contribute equally to the gradient updates.

```python
def normalize(x):
	x = (x - x.min()) / (x.max() - x.min())
   return x
```

#### Denormalization for Accuracy
To avoid errors and increase accuracy, it is better to denormalize the data at the end of the algorithm. After getting the predictions using normalized parameters, denormalize the predicted values to get more accurate values in their original scale. This helps to maintain the integrity of the data and provides more meaningful predictions.

```python
def denormalize(x, original_x):
    x = x * (max(original_x) - min(original_x)) + min(original_x)
    return x
```


## Precision
To evaluate the precision of the linear regression model, I used the $`R^2`$ score, which is calculated as follows:

```math
R^2 = 1 - \frac{RSS}{TSS}
```


- $`TSS`$ (Total Sum of Squares) measures the total variance in the target variable:
  
```math
  TSS = \sum (y_i - \bar{y})^2
```

   Here, $`y_i`$ is the actual value and $`\bar{y}`$ is the mean of the actual values.



- $`RSS`$ (Residual Sum of Squares) measures the variance that the model fails to explain:

```math
  RSS = \sum (y_i - \hat{y}_i)^2
```

   Here, $`\hat{y}_i`$ is the predicted value.


Using the Python code, the $`R^2`$ calculation looks like this:

```python
y_mean = np.mean(y)

y_pred = theta0 + (theta1 * x_data)

tss = np.sum((y - y_mean) ** 2)

rss = np.sum((y_pred - y) ** 2)

r_squared = 1 - (rss / tss)
```

The $`R^2`$ score provides a measure of how well the model's predictions match the actual data, with a value closer to 1 indicating a better fit.

# Launching the Project

To isolate the packages installed from your local system and to maintain package consistency in each launch, I implemented two approaches: Docker with X11 forwarding and a Python virtual environment (venv). Both methods ensure that you can display graphical outputs from Python applications without any issues, including those displayed via MobaXterm.

- Docker and X11 Forwarding approach can be found in the main branch.
- Python Virtual Environment approach can be found in the submit_version branch.

## Approach 1: Docker with X11 Forwarding (Main Branch)
**What is X11 Forwarding?**

X11 forwarding allows you to run applications with a graphical user interface (GUI) on a remote machine while displaying the GUI on your local machine. This is useful for running applications in a Docker container and viewing the GUI on your host system.

### How to Launch

1. X11 Server: Ensure you have an X11 server running on your host system. You can use:
	- macOS: XQuartz
 	- Windows: MobaXterm
 	- Linux: An X11 server is usually pre-installed.

   
2. Run the Script
```bash
sh launch.sh setup
```


3. When prompted
	- Confirm that your X11 server is ready.
	- Specify whether your X11 server is launched locally or remotely.
		- For local: The script will automatically set the IP address of your host.
		- For remote: Enter the IP address of the host running the X11 server when prompted.

This setup ensures that the GUI from the Docker container will be forwarded to your host system's X11 server.

## Approach 2: Using Python Virtual Environment (venv) (Submit_Version Branch)
**What is venv?**

venv is a tool in Python that creates an isolated environment for your Python projects. This means that all dependencies and packages are installed in an isolated directory, avoiding conflicts with other projects and system-wide packages

### How to Launch
1. Run the Script
```bash
sh launch.sh setup
```
This command will:
- Create a virtual environment in the venv directory (if it doesn't already exist).
- Activate the virtual environment.
- Install the necessary Python packages (matplotlib, numpy, pillow, and pandas).

## Run Project Commands
- To Train the Model
```bash
sh launch.sh train
```
- To Predict Prices
```bash
sh launch.sh predict
```
- To Calculate Precision
```bash
sh launch.sh precise
```
- To Clean the Environment (if needed)
```bash
sh launch.sh clean
```


