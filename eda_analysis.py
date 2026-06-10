import pandas as pd

# Load dataset
df = pd.read_csv("books_dataset.csv")

print("Dataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nSummary:")
print(df.describe(include='all'))
import matplotlib.pyplot as plt

availability_counts = df["Availability"].value_counts()

plt.bar(availability_counts.index, availability_counts.values)
plt.title("Book Availability")
plt.xlabel("Availability")
plt.ylabel("Count")
plt.show()