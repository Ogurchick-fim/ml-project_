# Used Car Listings Analysis Report

**Authors**: Kalbaev Timur and Tuleev Nursultan  
**Course**: SEST 1-22

## Introduction

The secondhand automobile market has experienced significant growth, offering buyers a variety of options at competitive prices. This report analyzes a dataset of used car listings, uncovering insights into pricing trends, vehicle attributes, and market dynamics. By leveraging SQL queries and Python-based analysis, this study aims to provide actionable insights to assist both buyers and sellers in making informed decisions.

## Methods

### Data Collection

The dataset was scraped from the m.mashina.kg platform using Python-based web scraping tools such as **BeautifulSoup**. After scraping, the data underwent cleaning and preprocessing to handle missing values, standardize formats, and prepare it for further analysis.

### Data Analysis

- **Exploratory Data Analysis (EDA)**:  
  Used **pandas** and **matplotlib** for descriptive statistics and visualizations to investigate distributions and correlations among key variables.
  
- **Database Integration**:  
  Imported the dataset into **SQLite** for structured querying and efficient analysis. Python's `sqlite3` library facilitated interaction with the database, enabling data extraction and aggregation.
  
- **Web Application**:  
  Built a **Flask-based web interface** to visualize data insights and provide users with interactive tools to explore listings based on custom criteria (e.g., price range, car model).

## Analysis Results

### 1. Most Expensive Car

The most expensive car in the dataset is a **Mitsubishi Carisma** (1999), priced at **$210,000**.

### 2. Unique Car Models Available

The dataset contains **251 unique car models**.

### 3. Average Price of Cars by Fuel Type

| Fuel Type  | Average Price ($) |
|------------|-------------------|
| Gasoline   | 4,568.22          |
| Diesel     | 8,091.33          |
| Hybrid     | Data not available (NaN) |

### 4. Cars with Missing Mileage

The dataset contains **16 cars with missing mileage data**.

### 5. Oldest Car in the Dataset

The oldest car in the dataset is a **Москвич 400**, produced in **1951**.

### 6. Most Common Car Color

The most common car color is **серебристый** (Silver), with **445** cars listed.

## Visual Outputs

<img width="1582" alt="Screenshot 2024-12-20 at 11 51 04 PM" src="https://github.com/user-attachments/assets/1f4a5fbe-470f-4998-b888-2d789e7cdf99" />


## Conclusion

This analysis offers a detailed overview of the used car market by highlighting key trends and patterns in the dataset:

- The **most expensive car** illustrates the pricing of high-end vehicles.
- **Average prices** by fuel type help segment the market and guide buyer preferences.
- Identifying cars with **missing mileage data** points to areas where data quality can be improved.

## Reflections

### Challenges:
- Addressing missing data, especially **mileage**, was a significant challenge.
- **Regional and temporal** variations in the dataset influenced the analysis and results.

### Future Enhancements:
- Incorporating visualizations for **price distributions** and **market trends** over time.
- Expanding the dataset to include additional attributes, such as **seller ratings** and **vehicle conditions**.

This study demonstrates the power of SQL and Python for uncovering actionable insights in automotive market data, facilitating informed decision-making for both buyers and sellers.

## Appendix

### Tools Used

- **Python Libraries**: `sqlite3`, `pandas`, `flask`, `beautifulsoup4` (bs4), `requests`
- **Database Management**: **SQLite** for structured data storage and querying

### Additional Notes

Additional SQL queries and results can be included here if further exploration or validation of the dataset is needed.
