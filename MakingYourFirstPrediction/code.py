# --------------
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
# code starts here
df = pd.read_csv(path)
df.head()

# all the dependent columns
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# split the columns into test and training data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=3)

# code ends here



# --------------
import matplotlib.pyplot as plt

# code starts here        
cols = X_train.columns

print(cols)

fig, axes = plt.subplots(nrows=3, ncols=3)

for i in range(3):
    for j in range(3):
        col = cols[ i * 3 + j]
        axes[i, j].scatter(df[col], df['list_price'])
        axes[i, j].set_xlabel(col)
    
fig.set_figheight(15)
fig.set_figwidth(15)
plt.show()


# code ends here



# --------------
# Code starts here
corr = X_train.corr()

X_train = X_train.drop(columns=['play_star_rating', 'val_star_rating'])
X_test = X_test.drop(columns=['play_star_rating', 'val_star_rating'])
# Code ends here


# --------------
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Code starts here

#Instantiate linear regression model
regressor=LinearRegression()

# fit the model
regressor.fit(X_train,y_train)

# predict the result
y_pred =regressor.predict(X_test)

# Calculate mse
mse = mean_squared_error(y_test, y_pred)

# print mse
print(mse)

# Calculate r2_score
r2 = r2_score(y_test, y_pred)

#print r2
print(r2)

# Code ends here


# --------------
# Code starts here

residual = y_test - y_pred

plt.hist(residual)
plt.show()
# Code ends here


