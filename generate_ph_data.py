import pandas as pd
import random

locations= ['Makati','Quezon City','Cebu City','Davao City','Calamba']
data=[]

for i in range(1000):
    city=random.choice(locations)
    rooms=random.randint(1,5)
    multiplier=1.5 if city =='Makati' else 1.0
    area=random.randint(30,250)
    price=(area*50000*multiplier)+(rooms*500000)+random.randint(-200000,200000)

    data.append(
        [city,rooms,area,int(price)]
    )
df=pd.DataFrame(
    data,
    columns=['Location','Bedrooms','Area_sqm','Price_PHP']
)
df.to_csv(
    'ph_house_prices.csv',
    index=False
          )
print("Success! 'ph_house_prices.csv' created with 1,000 rows.")