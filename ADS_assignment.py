# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 11:41:43 2022

@author: et22aap
"""

import pandas as pd
import matplotlib.pyplot as plt

# reading csv file into spyder using pandas
df = pd.read_csv('cause_of_deaths.csv')
df_ams = pd.read_csv('listings_amsterdam.csv')

'''
# printing first 5 rows from my data frame
print(df.head())
print('\n')

# printing data types in df
print(df.dtypes)
print('\n')

# printing the sum of all nulls in df
print(df.isnull().sum())
print(df)

# plotting bar chart of neighbourhood against price
plt.figure()
plt.barh(df['Meningitis'], df['Country/Territory'])
plt.xticks(rotation = 90)
plt.ylabel('cause of deaths')
plt.xlabel('Country')
plt.title('Cause of deaths by countries')
plt.tight_layout()

print('\n')

# plotting pie chart of all room types in df
room_1 = df.groupby('Country/Territory').count().reset_index()
room_df = pd.DataFrame(room_1)
size = []
for y in room_df['Year']:
    size.append(i)

name = []
for y in room_df['Country/Territory']:
    name.append(i)
explode = (0, 0.1)
plt.figure()
plt.pie(size, labels = name)
plt.show()

# line plot showing number of reviews in selected neighbourhoods per the years
plt.plot(df[df['Country/Territory'] == 'Ghana']['Year'],
         df[df['Country/Territory'] == 'Ghana']['Meningitis'])
plt.plot(df[df['Country/Territory'] == 'United Kingdom']['Year'],
         df[df['Country/Territory'] == 'United Kingdom']['Meningitis'])

'''




'''
data = df[df[['last_review', 'number_of_reviews', 'minimum_nights']]]
df.columns
data = df[ ['last_review', 'price'] ]
data = data.set_index('last_review')
print(data)

#data.plot()
#plt.xticks(rotation = 45)
#df['last_review'] = pd.to_datetime(df['last_review'])
#df = df.set_index('last_review')
#df.plot('number_of_reviews')
#df.plot('minimum_night')
'''