import pandas as pd

# Read the CSV file
df = pd.read_csv('RatingNGenreOfS.csv')

# Display the first few rows of the DataFrame
#print(df.head())

# Check for missing values
miss_val = df.isnull().sum()
print(miss_val)

# Check data types of columns
data_type = df.dtypes
print(data_type)

y=[]
for i in range(len(df)):
    x=tuple(df.iloc[i])
    y.append(x)
print(y)    
file=open('GenreNRatingOfS.txt','w')
for tuple in y:
    file.write(str(tuple) + ',' +'\n')
file.close()





































