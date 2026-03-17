import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('ph_house_prices.csv')
print(df.describe())

plt.figure(figsize=(10,6))
sns.heatmap(
    df.drop(
        'Location',
        axis=1
            )
    .corr(),
    annot=True,
    cmap='coolwarm'
)
plt.title("What drives the Price in PH Real Estate?")
plt.show()

plt.figure(figsize=(12,6))
sns.boxplot(
    x='Location',
    y='Price_PHP',
    data=df
)
plt.suptitle("Price Distribution by City")
plt.show()