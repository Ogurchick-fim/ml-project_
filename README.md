Used Car Listings Analysis Report
Kalbaev Timur and Tuleev Nursultan SEST 1-22
Introduction
The secondhand automobile market has seen significant growth, offering buyers a variety of options at competitive prices. This report aims to analyze a dataset of used car listings, uncovering insights into pricing trends, vehicle attributes, and market dynamics. By employing SQL queries, we extract and interpret valuable information to assist both buyers and sellers in making informed decisions.
Methods
Data Collection
The dataset was scraped from a m.mashina.kg platform using Python-based web scraping tools such as BeautifulSoup . Data cleaning and preprocessing were performed to handle missing values, standardize formats, and prepare the data for analysis.
Data Analysis
Exploratory Data Analysis (EDA):


Used pandas and matplotlib for descriptive statistics and visualizations.
Investigated distributions and correlations among key variables.
Database Integration:
Imported the dataset into SQLite for structured querying and efficient analysis.
Developed Flask APIs to fetch filtered data based on user criteria (e.g., price range, car model).
Web Application:
Built a Flask-based web interface to visualize data insights and provide users with tools to explore listings interactively.


Analysis:
The analysis was conducted using SQL queries executed on a SQLite database containing the car listings data. Python’s sqlite3 library facilitated interaction with the database, enabling data extraction and aggregation.

Results
Statistical Insights
1. Most Expensive Car
Query:
cursor.execute("""SELECT car_model, year_of_production, price_in_usd
FROM list_cars
ORDER BY price_in_usd DESC
LIMIT 1;
""")
cursor.fetchall()
Result: The most expensive car in the dataset is a Mitsubishi Carisma, produced in 1999, priced at $210000.
2. Unique Car Models Available
Query:
cursor.execute("""SELECT DISTINCT car_model
FROM list_cars;
""")


print(len(cursor.fetchall()))
Result: The dataset contains 251 unique car models.
3. Average Price of Cars by Fuel Type
Query:
cursor.execute("""SELECT fuel, AVG(price_in_usd) AS average_price
FROM list_cars
GROUP BY fuel;


""")
cursor.fetchall()
Result:
Fuel Type
Average Price ($)
Gasoline
4568.224
Diesel
8091.333
Hybrid
Nan

4. Cars with Missing Mileage
Query:
cursor.execute("""SELECT COUNT(*) AS Missing_Mileage_Count
FROM list_cars
WHERE Mileage IS NULL;
  


""")
cursor.fetchall()

Result: The dataset contains 16 cars with missing mileage data.
5. Oldest Car in the Dataset
Query:
cursor.execute("""SELECT car_model, year_of_production
FROM list_cars
ORDER BY year_of_production ASC
LIMIT 1;
""")
cursor.fetchall()

Result: The oldest car is a [Москвич 400], produced in 1951.
6. Most Common Car Color
Query:
cursor.execute("""SELECT color, COUNT(*) AS color_count
FROM list_cars
GROUP BY color
ORDER BY color_count DESC


""")
cursor.fetchone()

Result: The most common car color is “серебристый”, with 445	 cars.

Visual Outputs
<img width="1582" alt="Screenshot 2024-12-20 at 11 51 04 PM" src="https://github.com/user-attachments/assets/e2ef77ac-ab9a-4e89-88d1-b7d786a39e8d" />
<img width="1582" alt="Screenshot 2024-12-20 at 11 44 45 PM 1" src="https://github.com/user-attachments/assets/22689dcf-45f3-403a-af40-fde9f24d4e9b" />


Conclusion
The analysis provides an overview of the dataset, highlighting key trends and patterns:
The most expensive car offers insights into premium vehicle pricing.
Average prices by fuel type and body type help segment the market.
Identifying cars with missing data underscores areas for data quality improvement.
Reflections
Challenges:
Addressing missing data, particularly mileage values, required careful consideration.
Regional and temporal data variations influenced the analysis.
Future Enhancements:
Incorporating visualizations for price distributions and trends.
Expanding the dataset to include additional attributes, such as seller ratings and vehicle conditions.
This study illustrates the utility of SQL and Python for uncovering actionable insights in automotive market data, paving the way for informed decision-making in buying and selling vehicles.

Appendix
Tools Used
Python Libraries: sqlite3, pandas, flask ,sqlite3 ,bs4, requests.
Database Management: SQLite for structured data storage and querying.
Additional Queries
Additional SQL queries and results can be included here if needed for further exploration or validation.


