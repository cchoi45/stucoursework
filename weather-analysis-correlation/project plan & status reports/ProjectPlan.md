# Project Plan: Analyzing Weather and Time Impact on Online Shopping Behavior

## Overview:
The goal of this project is to determine how external factors, such as weather conditions, influence online shopping behavior. By analyzing the time spent shopping online, total spending, and trends in product categories during specific weather conditions, this project seeks to provide actionable insights for e-commerce platforms to optimize customer engagement and operational strategies.

## Research Question(s):
1. How does weather influence the time spent shopping online and the total amount spent?
2. Are certain product categories (e.g., electronics, home appliances) purchased more frequently during specific weather conditions?

## Team:
**Data Acquisition & Integration:** Set up API connections to Storm Glass and retrieve data, as well as load and manage the Online Sales dataset. Also merge the two datasets, ensure quality control, and clean the data.
  * Cynthia Choi

**Data Analysis/Visualization:** Conduct analysis, visualize trends, and prepare the final reporting.
  * Dianne Park

## Datasets:

**Online Shopping Dataset (online_sales.csv):**

https://www.kaggle.com/datasets/jacksondivakarr/online-shopping-dataset

Source: Kaggle (login required to access data). Contains 52955 rows with details of customer behavior and purchasing patterns on Google Merchandise Store.

Variables: CustomerID, Gender, Location, Tenure_Months, Transaction_ID, Transaction_Date, Product_SKU, Product_Description, Product_Category, Quantity, Avg_Price, Delivery_Charges, Coupon_Status, GST, Date, Offline_Spend, Online_Spend, Month, Coupon_Code, Discount_pct.

License: Apache 2.0

**Weather Data (Storm Glass API v2):**

https://stormglass.io/

Source: Storm Glass API, providing hourly historical weather conditions.

Variables: Temperature, precipitation, wind speed, and weather conditions like rain or snow.

License: MIT License

## Timeline:
**Week 3-4: Dataset Acquisition**
Acquire online shopping data and integrate the Storm Glass API.
Implement data integrity checks (e.g., row count validation, checksums).
Document data retrieval processes and steps for handling missing records.

**Week 5-6: Dataset Integration**
Merge the online shopping dataset with weather data based on date, time, and location.
Validate data alignment and ensure compatibility of variables across datasets (e.g., categorical vs. continuous data).

**Week 7: Data Profiling and Quality Assessment**
Profile the data to identify missing values, inconsistencies, and outliers.
Apply data cleaning techniques and document the process for reproducibility.

**Week 8: Reproducibility Package**
Package data integration and cleaning code into a Notebook for easy reproducibility.
Include detailed documentation in Markdown to ensure all steps are transparent and replicable (include system details).

**Week 9-10: Workflow Automation**
Set up an automated end-to-end workflow to run data acquisition, integration, cleaning, and analysis with minimal manual intervention.
Test the workflow to confirm that all stages are executed correctly and consistently.

**Week 11-12: Data Analysis and Visualization**
Perform statistical analysis to assess how weather conditions impact time spent shopping online and total spending.
Investigate trends in product categories purchased under different weather conditions.
Create visualizations (e.g., heatmaps, line charts) to illustrate findings.

**Week 13: Archiving and Metadata**
Archive the project in a repository with metadata, obtaining a persistent identifier.
Include accurate citations for both datasets and any software packages used.