# --------------
import pandas as pd
from sklearn.model_selection import train_test_split
#path - Path of file 

# Code starts here

df = pd.read_csv(path)

df.head()
X = df.drop(labels=['customerID', 'Churn'], axis=1)
y = df.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)



# --------------
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Code starts here
X_train['TotalCharges'] = X_train['TotalCharges'].replace(' ', np.nan).astype(float)
X_test['TotalCharges'] = X_test['TotalCharges'].replace(' ', np.nan).astype(float)
X_train['TotalCharges'] = X_train['TotalCharges'].fillna(X_train['TotalCharges'].mean())
X_test['TotalCharges'] = X_test['TotalCharges'].fillna(X_test['TotalCharges'].mean())
print(X_train.isnull().sum())

le = LabelEncoder()
for col in X_train.select_dtypes(include='object'):
  le.fit(X_train[col])
  X_train[col] = le.transform(X_train[col])

for col in X_test.select_dtypes(include='object'):
  le.fit(X_test[col])
  X_test[col] = le.transform(X_test[col])

y_train = y_train.replace({'No':0, 'Yes':1})
y_test = y_test.replace({'No':0, 'Yes':1})


# --------------
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

# Code starts here
ada_clf = AdaBoostClassifier(random_state=0)
ada_clf.fit(X_train, y_train)
y_pred = ada_clf.predict(X_test)
ada_score = accuracy_score(y_test, y_pred)
ada_cm = confusion_matrix(y_test, y_pred)
ada_cr = classification_report(y_test, y_pred)


# --------------
from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV

#Parameter list
parameters={'learning_rate':[0.1,0.15,0.2,0.25,0.3],
            'max_depth':range(1,3)}

# Code starts here
xgb_clf = XGBClassifier(random_state=0)

xgb_clf.fit(X_train, y_train)
y_pred = xgb_clf.predict(X_test)
xgb_score = accuracy_score(y_test, y_pred)
print("XGB Classifier Accuracy Score:{}".format(xgb_score))

xgb_cm = confusion_matrix(y_test, y_pred)
xgb_cr = classification_report(y_test, y_pred)
print("XGB Classifier Confusion Metrix: {}, Classified Report: {}".format(xgb_cm, xgb_cr))

clf_model = GridSearchCV(estimator=xgb_clf,
                        param_grid=parameters,
                        cv=5)

clf_model.fit(X_train, y_train)
y_pred = clf_model.predict(X_test)
clf_score = accuracy_score(y_test, y_pred)
print("XGB Classifier Grid Search Accuracy Score:{}".format(clf_score))

clf_cm = confusion_matrix(y_test, y_pred)
clf_cr = classification_report(y_test, y_pred)
print("XGB Classifier Grid Search Confusion Metrix: {}, Classified Report: {}".format(clf_cm, clf_cr))




