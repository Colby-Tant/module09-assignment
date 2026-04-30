# Module 9 Assignment: Introduction to Data Analysis with Pandas
# GlobalTech Sales Analysis

# Import required libraries
import pandas as pd
import numpy as np
from io import StringIO

# Welcome message
print("=" * 60)
print("GLOBALTECH QUARTERLY SALES ANALYSIS")
print("=" * 60)

# ----- SIMULATED CSV CONTENT (DO NOT MODIFY) -----
csv_content = """Date,Region,Store,Category,Product,Units,Unit_Price,Total_Sales,Promotion
2024-01-15,North America,NA001,Smartphones,PhoneX,12,899.99,10799.88,No
2024-01-18,Europe,EU002,Computers,LaptopPro,8,1299.99,10399.92,Yes
2024-01-20,Asia,AS001,Audio,WirelessEarbuds,25,149.99,3749.75,No
2024-01-22,North America,NA002,Wearables,SmartWatch,15,249.99,3749.85,No
2024-01-25,Latin America,LA001,Smartphones,PhoneX,7,899.99,6299.93,Yes
2024-01-27,Europe,EU001,Accessories,PhoneCase,35,24.99,874.65,No
2024-01-30,Asia,AS002,Smartphones,PhoneSE,18,499.99,8999.82,No
2024-02-02,North America,NA001,Computers,LaptopPro,6,1299.99,7799.94,No
2024-02-05,Europe,EU002,Wearables,SmartWatch,20,249.99,4999.80,Yes
2024-02-08,North America,NA003,Audio,WirelessEarbuds,30,149.99,4499.70,Yes
2024-02-10,Asia,AS001,Accessories,ChargingCable,45,19.99,899.55,No
2024-02-12,Latin America,LA001,Computers,TabletBasic,12,399.99,4799.88,No
2024-02-15,North America,NA002,Smartphones,PhoneSE,14,499.99,6999.86,No
2024-02-18,Europe,EU001,Audio,BlueSpeaker,22,79.99,1759.78,Yes
2024-02-20,Asia,AS002,Wearables,FitnessTracker,28,129.99,3639.72,No
2024-02-22,North America,NA001,Accessories,PhoneCase,50,24.99,1249.50,Yes
2024-02-25,Latin America,LA002,Smartphones,PhoneX,9,,8099.91,No
2024-02-28,Europe,EU002,Computers,LaptopBasic,10,899.99,8999.90,No
2024-03-02,North America,NA003,Wearables,FitnessTracker,,129.99,2599.80,Yes
2024-03-05,Asia,AS001,Smartphones,PhoneSE,15,499.99,7499.85,No
2024-03-08,Europe,EU001,Accessories,ChargingCable,60,19.99,1199.40,Yes
2024-03-10,North America,NA002,Computers,TabletPro,7,599.99,4199.93,No
2024-03-12,Latin America,LA001,Audio,WirelessEarbuds,18,149.99,2699.82,No
2024-03-15,North America,NA001,Wearables,SmartWatch,12,249.99,2999.88,No
2024-03-18,Europe,EU002,Smartphones,PhoneX,11,899.99,9899.89,Yes
2024-03-20,Asia,AS002,Computers,LaptopPro,6,1299.99,7799.94,No
2024-03-22,North America,NA001,Audio,BlueSpeaker,25,79.99,1999.75,No
2024-03-25,Latin America,LA002,Accessories,PhoneCase,40,,999.60,No"""
sales_data_csv = StringIO(csv_content)

# TODO 1: Load and Explore the Dataset
#dataset is stored in a dataframe called sales_df
sales_df = pd.read_csv(sales_data_csv)
#displays first 5 rows
print("\nFirst 5 rows:")
print(sales_df.head())
#displays basic info about the dataframe
print("\nData Info:")
sales_df.info()
#gets dimensions of the data frame and summary statistics for numerical columns
print(f"\nDimensions: {sales_df.shape}")
print("\nSummary Statistics:")
print(sales_df.describe())

# TODO 2: Column Selection and Basic Analysis
#selects and displays the 'product','units', and 'total sales' columns
subset = sales_df[['Product', 'Units', 'Total_Sales']]
#calculates total units sold
total_units = sales_df['Units'].sum()
#calculates total sales amount
total_revenue = sales_df['Total_Sales'].sum()
#calculates average unit price per product
avg_unit_price = sales_df['Unit_Price'].mean()

# TODO 3: Row Selection and Filtering
#selects sales from North America region only
na_sales = sales_df[sales_df['Region'] == 'North America']
#selects sales where units sold is greater than 20
high_volume_sales = sales_df[sales_df['Units'] > 20]
#selects sales of the phonex product that was on promotion
phonex_promo = sales_df[(sales_df['Product'] == 'PhoneX') & (sales_df['Promotion'] == 'Yes')]
#selects sales from February 2024
feb_sales = sales_df[sales_df['Date'].str.contains('-02-')]

# TODO 4: Advanced Filtering and Analysis
#finds the product with the highest total sales
best_product = sales_df.groupby('Product')['Total_Sales'].sum().idxmax()
#calculates total sales by region and sorts in descending order
sales_by_region = sales_df.groupby('Region')['Total_Sales'].sum().sort_values(ascending=False)
#calculates average units sold per category
avg_units_by_category = sales_df.groupby('Category')['Units'].mean()

#compares sales performance on promotion vs not on promotion
promo_avg = sales_df.groupby('Promotion')['Total_Sales'].mean()
promo_sum = sales_df.groupby('Promotion')['Total_Sales'].sum()
promo_comparison = {
    'promo_avg_sales': promo_avg['Yes'],
    'no_promo_avg_sales': promo_avg['No'],
    'promo_total_revenue': promo_sum['Yes'],
    'no_promo_total_revenue': promo_sum['No']
}

# TODO 5: Missing Value Detection and Reporting
#identifies columns with missing values and counts them
missing_counts = sales_df.isnull().sum()
#calculates what percentage of the data is missing in each column
missing_percentages = (sales_df.isnull().sum() / len(sales_df)) * 100

# TODO 6: Insights and Business Analysis
#creates a summary of the best performing category in each region
top_categories_by_region = sales_df.groupby('Region')['Category'].agg(lambda x: x.value_counts().index[0])
#calculates the average unit price for each product category
avg_price_by_category = sales_df.groupby('Category')['Unit_Price'].mean()

#calculates the total revenue and percentage of overall sales for each product
product_rev = sales_df.groupby('Product')['Total_Sales'].sum().to_frame(name='total_revenue')
product_rev['percentage'] = (product_rev['total_revenue'] / total_revenue) * 100
product_revenue_analysis = product_rev

# TODO 7: Generate Analysis Report
print("\n" + "=" * 60)
print("GLOBALTECH Q1 2024 SALES ANALYSIS REPORT")
print("=" * 60)

#displays overall sales performance with requested output format
print("\nOverall Performance:")
print(f"- Total Revenue: ${total_revenue:,.2f}")
print(f"- Total Units Sold: {int(total_units)}")
print(f"- Average Sale Value: ${sales_df['Total_Sales'].mean():.2f}")

#displays regional performance summary with requested format
print("\nRegional Performance:")
for region, val in sales_by_region.items():
    print(f"{region}: ${val:,.2f}")

#displays product category performance with requested format
print("\nCategory Performance:")
for cat in avg_units_by_category.index:
    print(f"{cat}: Avg Units: {avg_units_by_category[cat]:.1f}, Avg Price: ${avg_price_by_category[cat]:.2f}")

#displayes promotion effectiveness with requested format
print("\nPromotion Effectiveness:")
print(f"- Promoted Items Avg Sale: ${promo_comparison['promo_avg_sales']:,.2f}")
print(f"- Non-Promoted Items Avg Sale: ${promo_comparison['no_promo_avg_sales']:,.2f}")
print(f"- Revenue from Promotions: ${promo_comparison['promo_total_revenue']:,.2f}")

#gives report on data quality issues
print("\nData Quality Report:")
cols_with_missing = missing_counts[missing_counts > 0].index.tolist()
print(f"- Missing Values Found: {cols_with_missing}")
print(f"- Total Missing Entries: {missing_counts.sum()}")

#gives 3 key business recommendations
print("\nKEY BUSINESS RECOMMENDATIONS:")
print("1. PhoneX appears to be very popular and is a main driver of revenue.  Make sure that stock levels match demand in North America.")
print("2. Promoted products show a significantly higher sales on average.  Create promos to improve sales in underperforming categories such as Accessories.")
print("3. It appears that the variables for Unit_Price and Units have missing values in Latin America and North America.  Improve data entry to improve financial accuracy and the accuracy of analytics based recommendations.")