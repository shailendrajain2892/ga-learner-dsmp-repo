# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here

bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include= 'object')
print(categorical_var)

numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)


# code ends here


# --------------
# code starts here
banks = bank.drop(columns=['Loan_ID'])
print(banks.isnull().sum())
bank_mode = banks.mode()
#print(bank_mode.iloc[0])
banks = banks.fillna(0)
print(banks.isnull().values)
#print(bank.isnull().sum())
#code ends here


# --------------
# Code starts here
#print(banks)
avg_loan_amount = pd.pivot_table(banks, index=['Gender', 'Married','Self_Employed'], values='LoanAmount')
print(avg_loan_amount)



# code ends here



# --------------
# code starts here
loan_approved_se = banks [ (banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')]
loan_approved_nse = banks [ (banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')]
Loan_Status = 614
percentage_se = (len(loan_approved_se)/len(banks))*100
percentage_nse = (len(loan_approved_nse)/len(banks))*100
print(percentage_se, percentage_nse)
# code ends here


# --------------
# code starts here
convertMonthsToYear = lambda m : m/12
loan_term = banks['Loan_Amount_Term'].apply(lambda m:convertMonthsToYear(m))
print(len(loan_term))
big_loan_term = len(banks[loan_term >= 25])
print(big_loan_term)




# code ends here


# --------------
# code starts here

columns_to_show = ['ApplicantIncome', 'Credit_History']
 
loan_groupby=banks.groupby('Loan_Status')

loan_groupby=loan_groupby[columns_to_show]

# Check the mean value 
mean_values=loan_groupby.mean()


# code ends here


