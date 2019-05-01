### Project Overview

 Customer churn, also known as customer attrition, customer turnover, or customer defection, is the loss of clients or customers.Telephone service companies, Internet service providers, pay TV companies, insurance firms, and alarm monitoring services, often use customer attrition analysis and customer attrition rates as one of their key business metrics because the cost of retaining an existing customer is far less than acquiring a new one.

Predictive analytics use churn prediction models that predict customer churn by assessing their propensity of risk to churn. Since these models generate a small prioritized list of potential defectors, they are effective at focusing customer retention marketing programs on the subset of the customer base who are most vulnerable to churn.

For this project we will be exploring the dataset of a telecom company and try to predict the customer churn


### Learnings from the project

 AdaBoost and XGBoost Classifier can significantly increase the performance of the metrics.


### Approach taken to solve the problem

 1. Loaded the dataset
2. Converted TotalCharges columns to numerical
3. removed nan values
4. Applied label encoding for all the categorical columns
5. Replaced yes with 1 and No with 0 in target 
6. Applied AdaBoost classifier and checked its accuracy, confusion and classifier report
7. applied XGBoos classifer and checked and compared its metrics with adaboost
8.XGBoost is giving better result


### Challenges faced

 1. Identifying Missing values, replaceing space ' ' with NaN and then converting it to float
2. removing NaN with mean
3. Converting Categorical column to numeric using label encoding


### Additional pointers

 Classification report gives you all the metrics at once without computing. Better to make use of this API in classification problem.


