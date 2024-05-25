#My email yousafsahiwal3@gmail.com
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


df = pd.read_csv('abalone.csv')


print("Few first rows of the dataset:")
print(df.head())


print("\nInformation of Dataset:")
print(df.info())


print("\nSummary Statistics:")
print(df.describe())


print("\nMissing Values of Dataset:")
print(df.isnull().sum())


print("\nDuplicate Rows:")
print(df.duplicated().sum())

numerical_features = df.select_dtypes(include=[float, int]).columns
df[numerical_features].hist(bins=15, figsize=(15, 10), layout=(3, 3))
plt.suptitle('Distribution of Numerical Features')
plt.show()

plt.figure(figsize=(12, 8))
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()


for feature in numerical_features:
    plt.figure(figsize=(10, 5))
    sns.boxplot(y=df[feature])
    plt.title(f'Boxplot of {feature}')
    plt.show()


X = df.drop(columns=['Rings'])  
y = df['Rings']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)


mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\nMean Squared Error: {mse}")

print(f"R^2 Score: {r2}")
