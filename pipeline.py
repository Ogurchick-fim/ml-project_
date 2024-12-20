import requests 
import pandas as pd
from bs4 import BeautifulSoup
import sqlite3

html_page = requests.get('https://www.mashina.kg/search/bmw/all/?currency=2&sort_by=upped_at%20desc').content
soup = BeautifulSoup(html_page, 'lxml')
all_products =  soup.find_all('div', class_='list-item list-label')

car_model = []
year_of_production = []
engine_volume = []
mileage = []
fuel = []
steering_wheel_location = []
color = []
body_type = []
location = []
price_in_usd = []

list_lengths = {
    "car_model": len(car_model),
    "year_of_production": len(year_of_production),
    "engine_volume": len(engine_volume),
    "mileage": len(mileage),
    "fuel": len(fuel),
    "steering_wheel_location": len(steering_wheel_location),
    "color": len(color),
    "body_type": len(body_type),
    "location": len(location),
    "price_in_usd": len(price_in_usd),
    
}


for i in range(1,100):
    a = f"https://m.mashina.kg/search/all/all/?currency=2&gear_box_multiple=1&region=all&sort_by=upped_at+desc&page={i}"
    html_page = requests.get(a).content
    soup = BeautifulSoup(html_page, 'lxml')
    all_products =  soup.find_all('div', class_='list-item list-label')
    
    for product in all_products:
        mod = product.find('h2', class_='name').text.strip()
        car_model.append(mod)
        
        firs = (product.find('p', class_='year-miles').text.strip()).split(',')
        
        if len(firs) == 2:
            year_of_production.append(int(firs[0].replace('г.','')))
            engine_volume.append(None)
        else:
            year_of_production.append(int(firs[0].replace('г.','')))
            engine_volume.append(float(firs[1].replace('л.','')))
        
        second = (product.find('p', class_='body-type').text.strip()).split(',')
        body_type.append(second[0])
        fuel.append(second[1])
        
        third = (product.find('p', class_='volume').text.strip()).split(',')
        if len(third) > 1:
            steering_wheel_location.append(third[0])
            mileage.append(int(third[1].replace('км','').replace(' ','')))
        else:
            steering_wheel_location.append(third[0])
            mileage.append(None) 
        four = (product.find('strong').text.strip()).split(',') 
        price_in_usd.append(int(four[0].replace('$','').replace(' ','')))
        
        coloar = product.find('div',class_='item-info-wrapper').find('p',class_='year-miles').i
        color.append(coloar['title'])
        
        location.append((product.find('p',class_='city').text.strip()).split()[0])


data = {
    'Car Model': car_model,
    'Year of Production': year_of_production,
    'Engine Volume': engine_volume,
    'Mileage': mileage,
    'Fuel': fuel,
    'Steering Wheel Location': steering_wheel_location,
    'Color': color,
    'Body Type': body_type,
    'Location': location,
    'Price in USD': price_in_usd
}


df = pd.DataFrame(data)

df.to_csv('list.csv')


data_file = 'list.csv'
df = pd.read_csv(data_file)

sqlite_db = 'list.db'

conn = sqlite3.connect(sqlite_db)
cursor = conn.cursor()

table_query = """
CREATE TABLE IF NOT EXISTS list_cars (
    id INTEGER PRIMARY KEY,
    car_model TEXT,
    year_of_production INTEGER,
    engine_volume REAL,
    mileage REAL,
    fuel TEXT,
    steering_wheel_location TEXT,
    color TEXT,
    body_type TEXT,
    location TEXT,
    price_in_usd REAL
);
"""

cursor.execute(table_query)

df.rename(columns={
    "Car Model": "car_model",
    "Year of Production": "year_of_production",
    "Engine Volume": "engine_volume",
    "Mileage": "mileage",
    "Fuel": "fuel",
    "Steering Wheel Location": "steering_wheel_location",
    "Color": "color",
    "Body Type": "body_type",
    "Location": "location",
    "Price in USD": "price_in_usd"
}, inplace=True)


df.to_sql('list_cars', conn, if_exists='replace', index=False)

conn.commit()
conn.close()


