# ft_linear_regression

# Introdution
Machine learning is a subset of artificial intelligence that focuses on building systems that learn from and make decisions based on data. This project showcases a fundamental machine learning technique known as linear regression, implemented using the Gradient Descent algorithm. The goal is to understand the relationship between dependent and independent variables in a dataset and use this relationship to make predictions.

## What is Linear Regression?
Linear regression is an algorithm that provides a linear relationship between an independent variable and a dependent variable to predict the outcome of future events. It is a statistical method used in data science and machine learning for predictive analysis.



The goal is to find the formula (or equation) of a line to predict the value of the output (dependent/outcome) variable based on the input (independent/predictor) variable with maximum accuracy or minimum error.


![image](https://github.com/Saxsori/ft_linear_regression/assets/92129820/99d1f2b7-459c-4c17-9775-0390c292aa30)

```
In the above figure,

X-axis:Independent variable
Y-axis: Output / dependent variable
Line of regression: Best fit line for a model

```

Line is plotted for the given data points that suitably fit all the issues. Hence, it is called the ‘best fit line.’ The goal of the linear regression algorithm is to find this best fit line seen in the above figure.


Suppose the equation of the best-fitted line is given by Y = aX + b 

```
y = ax + b

Where,

Y: dependent variable
m: slope or regression coefficient
c: y-intercept
```
then, the regression coefficients formula is given as follows:

![image](https://github.com/Saxsori/ft_linear_regression/assets/92129820/941bf7be-1536-4e0c-96f5-f5360016e86c) 

here, n refers to the number of data points in the given data sets.


# Gradient Descent

Gradient descent is one of the most famous techniques in machine learning and used for training all sorts of neural networks. But gradient descent can not only be used to train neural networks, but many more machine learning models. In particular, gradient descent can be used to train a linear regression model!


--------------


An iterative optimization algorithm that tries to find the optimum value (Minimum/Maximum) of an objective function. It is one of the most used optimization techniques in machine learning projects for updating the parameters of a model in order to minimize a cost function. 

![image](https://github.com/Saxsori/ft_linear_regression/assets/92129820/d7115b7b-d3ec-430e-bcf3-d3f22770d076)

The main aim of gradient descent is to find the best parameters of a model that give the highest accuracy on training. By parameters, we mean the coefficients or weights (𝜃0,𝜃1) in the linear regression model that determine the strength and direction of the relationship between the independent variables (features) and the dependent variable (target).

![image](https://github.com/Saxsori/ft_linear_regression/assets/92129820/14f210fb-39a0-404b-b3d0-e0b696eea7ba)

```
Where,

a: learning rate
m: total data

the parameters
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



4. Update Parameters

5. Calculate Cost Function

6. Repeat







