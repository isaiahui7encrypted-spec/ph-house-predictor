import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

df= pd.read_csv('ph_house_prices.csv')
df_encoded=pd.get_dummies(
    df,
    columns=['Location']
)
X=df_encoded.drop(
    'Price_PHP',
    axis=1
)
y=df_encoded['Price_PHP']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
model=LinearRegression()
model.fit(X_train,y_train)
joblib.dump(model,'ph_house_prices.pkl')
joblib.dump(X.columns.tolist(),'model_columns.pkl')

print("Model trained and saved successfully!")