# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Code starts here

df = pd.read_csv(path)
print(df.head())

#plt histrogram on rating
df['Rating'].hist()
plt.show()

mask = df['Rating'] <= 5
data = df[mask]

#Code ends here


# --------------
# code starts here
total_null = data.isnull().sum()
percent_null = total_null/data.isnull().count()

missing_data = pd.concat([total_null, percent_null], keys=['Total','Percent'], axis=1)
print(missing_data)

#drop missing value
data.dropna(inplace=True)

total_null_1 = data.isnull().sum()
percent_null_1 = total_null_1/data.isnull().count()

missing_data_1 = pd.concat([total_null_1, percent_null_1], keys=['Total','Percent'], axis=1)
print(missing_data_1)
# code ends here


# --------------

#Code starts here
cp = sns.catplot(x='Category', y='Rating', data=data, kind='box', height=10)
cp.set_xticklabels(rotation=90)
plt.title("Rating vs Category [boxPlot]")
plt.show()
#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here
# print the data installs value counts
data['Installs'].value_counts()

# remove plus and comma sign from installs and convert it to int
data['Installs'] = data['Installs'].str.replace('+', '')
data['Installs'] = data['Installs'].str.replace(",", '')
data['Installs'] = data['Installs'].astype(int)

# Initialize encoder object
le = LabelEncoder()

# Fit-transform on data
data['Installs'] = le.fit_transform(data['Installs'])

#reg plot
sns.regplot(x='Installs', y='Rating', data=data)
plt.title('Rating vs Installs [RegPlot]')
plt.show()


#Code ends here



# --------------
#Code starts here
#replace $ sign
data.Price = data.Price.str.replace("$", '')

# convert to float
data.Price = data.Price.astype(float)

#plot regplot
sns.regplot(x='Price', y='Rating', data=data)
plt.title("Rating vs Price [RegPlot]")
plt.show()


#Code ends here


# --------------

#Code starts here
#split the Genres column
new = data["Genres"].str.split(";", n = 1, expand = True)

# store the first Genres
data.Genres = new[0]

# group by Genres and Rating
gr_mean = data.groupby(by=['Genres'], as_index=False)['Rating'].mean()

# describe function
gr_mean.describe()

# sort rating values
gr_mean = gr_mean.sort_values(by=['Rating'])

# reset index and print first and last value
gr_mean.reset_index(drop=True, inplace=True)

#first value
print(gr_mean.loc[0])

# last value
print(gr_mean.iloc[-1])
#Code ends here


# --------------

#Code starts here

# convert the last updated column to date time format
data['Last Updated']= pd.to_datetime(data['Last Updated'])

# save the max date 
max_date = data['Last Updated'].max()

# creating new column last updated days
data['Last Updated Days'] = (max_date - data['Last Updated']).dt.days

# plot the regplot between last updated days and rating
sns.regplot(x='Last Updated Days', y='Rating', data=data)
plt.title('Rating vs Last Updated [RegPlot]')
plt.show()



#Code ends here


