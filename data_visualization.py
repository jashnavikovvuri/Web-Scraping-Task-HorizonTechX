import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("books_dataset.csv")

availability_counts = df["Availability"].value_counts()

plt.figure(figsize=(6,4))
plt.bar(availability_counts.index, availability_counts.values)

plt.title("Book Availability Analysis")
plt.xlabel("Availability Status")
plt.ylabel("Number of Books")

plt.tight_layout()
plt.show()