# --------------
import pandas as pd
from sklearn import preprocessing

#path : File path

# Code starts here

# read the dataset
dataset = pd.read_csv(path)

# look at the first five columns
dataset.head()

# Check if there's any column which is not useful and remove it like the column id
dataset.drop(labels=['Id'], inplace=True, axis=1)

# check the statistical description
print(dataset.describe())


# --------------
# We will visualize all the attributes using Violin Plot - a combination of box and density plots
import seaborn as sns
from matplotlib import pyplot as plt

#names of all the attributes 
cols = dataset.columns

#number of attributes (exclude target)
size = len(cols)-1

#x-axis has target attribute to distinguish between classes
x = cols[-1]

#y-axis shows values of an attribute
y = cols[:-1]

#Plot violin for all attributes
for col in y:
    sns.violinplot(x, col, data=dataset)


# --------------
import numpy
threshold = 0.5

# no. of features considered after ignoring categorical variables

num_features = 10

# create a subset of dataframe with only 'num_features'
subset_train = dataset.iloc[:, 0:10]


#Calculate the pearson co-efficient for all possible combinations
data_corr = subset_train.corr()
sns.heatmap(data_corr, cmap="viridis", annot=True)

# Set the threshold and search for pairs which are having correlation level above threshold
corr_var_list={}
for i in range(0, 10):
  for j in range(i+1, 10):
    corr_value = abs(data_corr.iloc[i, j] )
    if corr_value > 0.5 and corr_value!=1:
      corr_var_list[corr_value]  = (data_corr.index[i], data_corr.columns[j])
# Sort the list showing higher ones first 
s_corr_list = sorted(corr_var_list.keys())

#Print correlations and column names
print(s_corr_list)
for k in s_corr_list:
  print(corr_var_list.get(k)) 



# --------------
#Import libraries 
from sklearn import cross_validation
from sklearn.preprocessing import StandardScaler

# Identify the unnecessary columns and remove it 
dataset.drop(columns=['Soil_Type7', 'Soil_Type15'], inplace=True)

X = dataset.iloc[:, :-1]
Y = dataset.iloc[:, -1]

# Scales are not the same for all variables. Hence, rescaling and standardization may be necessary for some algorithm to be applied on it.
X_train, X_test, Y_train, Y_test = cross_validation.train_test_split(X, Y, test_size=0.2, random_state=0)

#Standardized
#Apply transform only for non-categorical data
scale=StandardScaler()
X_train_temp = scale.fit_transform(X_train.iloc[:,:10])
X_test_temp = scale.fit_transform(X_test.iloc[:,:10])

#Concatenate non-categorical data and categorical
X_train1=numpy.concatenate([X_train_temp,X_train.iloc[:,10:]],axis=1)
X_test1=numpy.concatenate([X_test_temp,X_test.iloc[:,10:]],axis=1)
scaled_features_train_df = pd.DataFrame(X_train1, index=X_train.index,
columns=X_train.columns)
scaled_features_test_df = pd.DataFrame(X_test1, index=X_test.index,
columns=X_test.columns)




# --------------
from sklearn.feature_selection import SelectPercentile
from sklearn.feature_selection import f_classif


# Write your solution here:
skb = SelectPercentile(score_func=f_classif, percentile=20)
predictors = skb.fit_transform(X_train1, Y_train)
scores = skb.scores_
top_k_index, top_k_predictors = skb.get_support(indices=True), cols[skb.get_support(indices=True)]
print(top_k_index)
print(top_k_predictors)


# --------------
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, precision_score

clf, clf1 = OneVsRestClassifier(LogisticRegression()), LogisticRegression()
model_fit_all_features = clf.fit(X_train, Y_train)
predictions_all_features = clf.predict(X_test)
score_all_features = accuracy_score(Y_test, predictions_all_features)
print(score_all_features)

model_fit_top_features = clf.fit(scaled_features_train_df[top_k_predictors], Y_train)
predictions_top_features = clf.predict(scaled_features_test_df[top_k_predictors])
score_top_features = accuracy_score(Y_test, predictions_top_features)
print(score_top_features)



