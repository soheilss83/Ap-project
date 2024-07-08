import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

# Load dataset
file_path = 'mushroom_cleaned.csv'  # Adjust the path as needed
mushroom_data = pd.read_csv(file_path)


#describe the data
print(mushroom_data.head())
print(mushroom_data.describe())


# Removing duplicates
mushroom_data = mushroom_data.drop_duplicates()
# removing zeroes
mushroom_data=mushroom_data[mushroom_data['stem-width']!=0]
# removing outliers
def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    return df

for column in mushroom_data.columns[:-1]:
    mushroom_data = remove_outliers(mushroom_data, column)


# Normalizing data
scaler = MinMaxScaler()
mushroom_data[mushroom_data.columns[:-1]] = scaler.fit_transform(mushroom_data[mushroom_data.columns[:-1]])




# Plotting variable
plt.figure(figsize=(20, 15))

for i, column in enumerate(mushroom_data.columns[:-1], 1):
    plt.subplot(3, 3, i)
    sns.histplot(mushroom_data[column], kde=True, bins=30,color='purple')
    plt.title(f'Distribution of {column}')

plt.tight_layout()
plt.show()



# Plotting the relation between features and class
plt.figure(figsize=(20, 15))

for i, column in enumerate(mushroom_data.columns[:-1], 1):
    plt.subplot(3, 3, i)
    sns.boxplot(x='class', y=column, data=mushroom_data,color='purple')
    plt.title(f'{column} vs Class')

plt.tight_layout()
plt.show()



# correlation matrix
correlation_matrix = mushroom_data.corr()

# Plot the heatmap 
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='Purples', center=0)
plt.title('Correlation Matrix')
plt.show()




# Scatter plots for highly correlated variables
threshold = 0.7  
high_corr_pairs = [(i, j) for i in mushroom_data.columns for j in mushroom_data.columns if i != j and abs(correlation_matrix.loc[i, j]) > threshold]

plt.figure(figsize=(20, 15))

for idx, (var1, var2) in enumerate(high_corr_pairs, 1):
    plt.subplot(len(high_corr_pairs) // 2 + 1, 2,idx)
    sns.scatterplot(x=var1, y=var2, data=mushroom_data,color='purple')
    plt.title(f'Scatter Plot: {var1} vs {var2}')

plt.tight_layout()
plt.show()