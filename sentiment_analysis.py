from textblob import TextBlob
import pandas as pd

reviews = [
    "This product is amazing and very useful",
    "I love this service",
    "The product is okay",
    "Not bad, but could be better",
    "I am very disappointed with the quality",
    "Worst experience ever"
]

results = []

for review in reviews:
    analysis = TextBlob(review)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    results.append([review, sentiment])

df = pd.DataFrame(results, columns=["Review", "Sentiment"])

print(df)

df.to_csv("sentiment_results.csv", index=False)
import matplotlib.pyplot as plt

sentiment_counts = df["Sentiment"].value_counts()

plt.bar(sentiment_counts.index, sentiment_counts.values)
plt.title("Sentiment Analysis Results")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.show()