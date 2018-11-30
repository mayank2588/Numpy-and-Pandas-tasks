# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 


# code starts here
bank = pd.read_csv(path)
# categorical_var
categorical_var = bank.select_dtypes(include='object')
print(categorical_var)
# numerical_var
numerical_var = bank.select_dtypes(include='number')
print(numerical_var)




# code ends here


# --------------
# code starts here

banks = bank.drop(['Loan_ID'], axis=1)
banks.isnull().sum()

bank_mode = banks.mode()
banks.fillna(bank_mode.iloc[0],inplace=True)
print(banks)
#code ends here


# --------------
# Code starts here
avg_loan_amount = pd.pivot_table(banks, index= ['Gender','Married','Self_Employed'], values= "LoanAmount", aggfunc= np.mean)
print(avg_loan_amount)


# code ends here



# --------------
# code ends here
loan_groupby = banks.groupby('Loan_Status')[['ApplicantIncome','Credit_History']]

mean_values = loan_groupby.mean()
print(mean_values)


# code ends here


# --------------
# code starts here
loan_approved_se = banks[(banks.Self_Employed == 'Yes') & (banks.Loan_Status == 'Y')]
print(loan_approved_se.Loan_Status.count())
loan_approved_nse = banks[(banks.Self_Employed == 'No') & (banks.Loan_Status == 'Y')]
print(loan_approved_nse.Loan_Status.count())

percentage_se = (loan_approved_se.Loan_Status.count() * 100 / 614)
percentage_nse = (loan_approved_nse.Loan_Status.count() * 100 / 614)

print(percentage_se)
print(percentage_nse)
# code ends 



# --------------
# code starts here

loan_term = banks['Loan_Amount_Term'].apply(lambda x: x/12)
print(loan_term)
big_loan_term = banks['Loan_Amount_Term'].apply(lambda x: x/12 >= 25).sum()
print(big_loan_term)


# code ends here


