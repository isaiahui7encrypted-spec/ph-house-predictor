import joblib
import pandas as pd
from sklearn.model_selection import train_test_split

df= pd.read_csv('ph_house_prices.csv')
df_encoded=pd.get_dummies(df,columns=['Location'])

X=df_encoded.drop('Price_PHP',axis=1)
y=df_encoded['Price_PHP']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

model=joblib.load('ph_house_prices.pkl')
score=model.score(X_test,y_test)
print(f"Model R-squared Score: {score:.4f}")

# columns=joblib.load('model_columns.pkl')
#
# weights=pd.DataFrame(
#     {'Feature':columns,
#      'Weight':model.coef_
#      }
# )
# print(weights.sort_values(by='Weight',ascending=False))
# score=model.score(X_test,y_test)
# print(f"Model R-squared Score: {score:.4f}")