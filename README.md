# ft_linear_regression

# Introdution
Machine learning is a subset of artificial intelligence that focuses on building systems that learn from and make decisions based on data. This project showcases a fundamental machine learning technique known as linear regression, implemented using the Gradient Descent algorithm. The goal is to understand the relationship between dependent and independent variables in a dataset and use this relationship to make predictions.

## What is Linear Regression?
Linear regression is an algorithm that provides a linear relationship between an independent variable and a dependent variable to predict the outcome of future events. It is a statistical method used in data science and machine learning for predictive analysis.



The goal is to find the formula (or equation) of a line to predict the value of the output (dependent/outcome) variable based on the input (independent/predictor) variable with maximum accuracy or minimum error.


![image](https://github.com/Saxsori/ft_linear_regression/assets/92129820/0188ce10-9c24-4e3e-9b2e-306e136ff62c)


```
In the above figure,

X-axis:Independent variable
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

here, n refers to the number of data points in the given data sets.


# Gradient Descent

Gradient descent is one of the most famous techniques in machine learning and used for training all sorts of neural networks. But gradient descent can not only be used to train neural networks, but many more machine learning models. In particular, gradient descent can be used to train a linear regression model!


--------------


An iterative optimization algorithm that tries to find the optimum value (Minimum/Maximum) of an objective function. It is one of the most used optimization techniques in machine learning projects for updating the parameters of a model in order to minimize a cost function. 

```math
\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
```

Where,
```
\hat{y}^{(i)} = \theta_0 + \theta_1x_1^{(i)} 
```


The main aim of gradient descent is to find the best parameters of a model that give the highest accuracy on training. By parameters, we mean the coefficients or weights (𝜃0,𝜃1) in the linear regression model that determine the strength and direction of the relationship between the independent variables (features) and the dependent variable (target).


``` math
\theta_0 = \theta_0 - \alpha \frac{1}{m} \sum_{i=1}^{m} (\hat{y}^{(i)} - y^{(i)})
```

```math
\theta_1 := \theta_1 - \alpha \frac{1}{m} \sum_{i=1}^{m} (\hat{y}^{(i)} - y^{(i)}) x_1^{(i)}
```


Where,

``` 
a: learning rate
m: total data
𝜃0: bias, y-intercept
𝜃1: Weight, slope
```

## Step-by-Step Explanation of Gradient Descent

1. Initialize Parameters
   
Start with initial values for the parameters, can be set to zeros.

```
𝜃0 = 0
𝜃1 = 0
```

2. Compute Gradients



``` math
\frac{\partial}{\partial \theta_0} = \frac{1}{m} \sum_{i=1}^{m} (\hat{y}^{(i)} - y^{(i)})
```

```math
​\frac{\partial}{\partial \theta_1} = \frac{1}{m} \sum_{i=1}^{m} (\hat{y}^{(i)} - y^{(i)}) x_1^{(i)}
```

where, 

```math
\hat{y}^{(i)} = \theta_0 + \theta_1x_1^{(i)} 
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


# Bonus

## Precision
To evaluate the precision of the linear regression model, we use the $`R^2`$ score, which is calculated as follows:

```math
R^2 = 1 - \frac{RSS}{TSS}
```


- TSS (Total Sum of Squares) measures the total variance in the target variable:

where:

```math
  TSS = \sum (y_i - \bar{y})^2
```

Here, $`y_i`$ is the actual value and $`\bar{y}`$ is the mean of the actual values.







