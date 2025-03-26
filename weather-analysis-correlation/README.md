# is477-fa24-dicy
Cynthia Choi &amp; Dianne Park Final Project Repo

Released under the Apache 2.0 open source license.

# Analyzing Weather and Time Impact on Online Shopping Behavior

## Link to record: https://doi.org/10.5281/zenodo.14456038

## Link to Box: https://uofi.box.com/s/5qn1lje3e9rav8z8dgbrfxuhj3j6lpzo

## Contributers:
* Cynthia Choi
https://orcid.org/0009-0000-0796-0301

* Dianne Park

---

## Project Summary:

The goal of this project is to determine how external factors, such as weather conditions, influence online shopping behavior. By analyzing various elements, including the time spent shopping, total spending, and trends in product categories during specific weather conditions, this project aims to provide actionable insights for e-commerce platforms. The idea is to help these platforms optimize their customer engagement strategies and improve operational decisions based on weather-driven consumer patterns. The motivation for this project comes from a personal interest in how weather affects shopping behavior. As people who tend to shop more during colder seasons, the question arose: do others experience similar behavior, and can these patterns be identified on a larger scale across different geographic locations?

The research addresses two primary questions: 1) How does weather influence the time spent shopping online and the total amount spent? 2) Are certain product categories, such as electronics or home appliances, purchased more frequently during specific weather conditions? Through the analysis of data from cities like Chicago, Washington DC, New Jersey, and California, the project reveals that temperature plays a significant role in driving online shopping behavior, with cities like Chicago and Washington DC showing strong positive correlations between higher temperatures and increased order volumes. Interestingly, New Jersey showed a negative correlation with both temperature and precipitation, suggesting that weather, particularly rainy or snowy conditions, may discourage online shopping in this region.

The findings also highlighted several other key factors, such as varying levels of precipitation and wind speed, which further influence shopping behavior. In California, for example, higher precipitation levels did not significantly deter online shopping, while in New Jersey, the strong negative correlation with precipitation indicated a clear relationship between poor weather and reduced online orders. These insights suggest that e-commerce platforms need to consider location-specific weather conditions when planning promotions, inventory, and marketing strategies. Ultimately, understanding how weather impacts shopping habits can help businesses develop more effective, tailored approaches to engaging customers based on their regional climates, leading to improved sales and customer satisfaction.

**CONSTRAINTS:**

API Limitation. The Online Shopping Dataset contains 52,955 rows of customer behavior data, providing insights into transaction trends over time. While the dataset covers a wide range of dates and locations, we narrowed our focus to a subset of the data for API usage efficiency.

To optimize the limited number of API calls available, we selected:
* Top 5 dates with the highest number of orders.
* Bottom 5 dates with the lowest number of orders.

This approach ensures a balanced representation of high-activity and low-activity periods while staying within the constraints of API usage limits. The selected dates were determined by aggregating order counts by date, sorting them, and then picking the top and bottom performers.

---

## Data Profile: Online Shopping Dataset and Storm Glass Weather Data

This section provides an in-depth analysis of the two datasets—**Online Shopping Dataset** and **Weather Data**—used in this project. Each dataset serves to uncover patterns in online shopping behavior and its correlation with weather conditions. Below is a detailed profile of the datasets, the key variables, and their relevance to the research.

#### **1. Online Shopping Dataset (Kaggle, "file.csv")**

The **Online Shopping Dataset** is sourced from the Kaggle platform and provides valuable insights into customer behavior and purchasing patterns on the Google Merchandise Store. This dataset comprises 52,955 rows and contains multiple variables that describe both the transactional and demographic details of customers. It offers a rich foundation for analyzing how customer characteristics and their shopping behavior interact with other factors such as promotions, pricing, and product categories. Below is a breakdown of the key variables:

**Key Variables:**

- **CustomerID**: A unique identifier assigned to each customer. This variable helps track the purchasing behavior of individual customers, enabling segmentation analyses and repeat purchase trends.
  
- **Gender**: This categorical variable indicates the gender of the customer. Gender can be a crucial factor in understanding purchasing preferences, such as whether certain products (e.g., clothing or electronics) are more popular with a specific gender.
  
- **Location**: The geographical location of the customer, often in the form of a city or region. Location can influence shopping patterns due to regional preferences or climatic conditions, which may correlate with the weather data used in the study.

- **Tenure_Months**: This variable indicates how long a customer has been purchasing from the store, measured in months. Longer tenure may suggest higher loyalty or familiarity with the platform, which could affect purchasing behavior, especially in response to promotions or weather-related factors.

- **Transaction_ID**: A unique identifier for each transaction. This is essential for tracking individual purchases and linking them to specific products, allowing for a more granular analysis of customer behavior.

- **Transaction_Date**: The date when the transaction occurred. This allows for temporal analysis, enabling insights into seasonal trends, purchasing frequencies, or the effect of specific events like promotions or holidays.

- **Product_SKU**: The stock-keeping unit identifier, which is unique to each product. This variable is useful for analyzing which products are most popular, and whether specific categories, like electronics or home appliances, are purchased more often during particular weather conditions.

- **Product_Description**: A textual description of the product. While not directly useful for quantitative analysis, this field provides context and helps in identifying product categories or attributes that might correlate with specific weather patterns.

- **Product_Category**: This variable categorizes the product (e.g., electronics, clothing, home appliances). Analyzing this field allows businesses to identify which product categories are most affected by weather conditions, aiding in targeted marketing or inventory planning.

- **Quantity**: The number of units purchased. This variable is essential in assessing the volume of products being sold and its relationship with factors like weather, promotions, and product category.

- **Avg_Price**: The average price of products in a transaction. This variable helps to assess how spending correlates with specific weather conditions and how product pricing might influence consumer behavior.

- **Delivery_Charges**: The cost of delivering the product to the customer. Delivery charges can impact the overall purchase decision, especially during certain weather conditions when consumers may be more likely to shop for convenience.

- **Coupon_Status**: Indicates whether a coupon was applied to the transaction. This is particularly relevant for analyzing the impact of promotions in driving online shopping behavior during specific weather patterns.

- **GST**: Goods and Services Tax applied to the purchase. While a regulatory requirement, this variable can help in understanding the final cost of the transaction and its influence on consumer behavior.

- **Date**: A separate date variable that could potentially overlap with the **Transaction_Date**, but may be used for different analyses like trend monitoring.

- **Offline_Spend**: Indicates the amount spent by the customer offline, which can help differentiate the purchasing behavior between online and offline shopping channels.

- **Online_Spend**: Represents the total amount spent online. This is the primary variable for analyzing the relationship between weather conditions and online shopping behavior.

- **Month**: The month in which the transaction occurred. This allows for seasonal trend analysis, providing insights into how consumer behavior shifts across the months, potentially due to weather variations.

- **Coupon_Code**: The specific coupon code applied, offering further details on the types of promotions used by customers.

- **Discount_pct**: The percentage discount applied during the transaction. This variable helps understand how discounts influence spending behavior and how these trends might shift during different weather conditions.

**Relevance to the Project:**
The **Online Shopping Dataset** provides a comprehensive view of consumer purchasing behavior, which, when combined with weather data, enables a deeper understanding of how weather conditions affect online shopping. The key variables, such as **Transaction_Date**, **Product_Category**, **Quantity**, **Online_Spend**, and **Coupon_Status**, are crucial for analyzing the impact of weather on product demand, spending patterns, and the effectiveness of promotions.

https://www.kaggle.com/datasets/jacksondivakarr/online-shopping-dataset

Source: Kaggle (login required to access data). Contains 52955 rows with details of customer behavior and purchasing patterns on Google Merchandise Store.

License: Apache 2.0

---

#### **2. Weather Data (Storm Glass API v2, "allweather_df.csv")**

The weather data used in this project is sourced from the **Storm Glass API v2**, which provides hourly historical weather conditions, including temperature, precipitation, wind speed, and general weather conditions like rain or snow. This dataset is essential for understanding how various weather conditions correlate with online shopping behavior. The weather data is available under the **MIT License**, and provides detailed information that is critical for analyzing the weather's influence on purchasing patterns.

https://docs.stormglass.io/#/

**Key Variables:**

- **Temperature**: The temperature is measured in degrees Celsius and provides insights into how warmer or colder weather might affect consumer behavior. For example, colder temperatures may increase indoor activities, such as online shopping, while warmer weather might reduce shopping time or affect the types of products being purchased.

- **Precipitation**: The amount of precipitation (rain or snow) is measured in millimeters. Precipitation is an important factor in this analysis, as it may influence consumers to make purchases online rather than going to physical stores. High levels of precipitation could correlate with increased online shopping, especially for items that provide comfort or convenience during adverse weather conditions.

- **Wind Speed**: Wind speed is recorded in meters per second and can impact shopping behavior, particularly in areas where strong winds may discourage consumers from shopping in physical stores, thus driving more online activity.

**Relevance to the Project:**
The **Weather Data** serves as the primary external factor for analyzing its correlation with online shopping behavior. By pairing this data with transaction details from the **Online Shopping Dataset**, the project can identify patterns in how temperature, precipitation, and wind speed affect consumer purchasing decisions.

Source: Storm Glass API, providing hourly historical weather conditions.

License: MIT License

---

## Findings:

The visualizations reveals several key insights about the relationship between weather conditions and order patterns across different locations. The Orders vs. Average Temperature plot demonstrates varying relationships across cities, with some locations showing positive correlations while others display more scattered patterns. California and Chicago exhibit the highest order volumes, frequently reaching above 100 orders, while Washington DC consistently shows lower order counts.
The precipitation analysis indicates a generally negative impact on order volumes, with most locations showing decreased orders during higher precipitation events. This is particularly evident in the Orders vs. Precipitation plot, where order counts tend to cluster at lower precipitation levels and decrease as precipitation increases.

The correlation heatmap provides quantitative evidence of these relationships, showing a moderate positive correlation (0.23) between average temperature and order count, while precipitation and wind speed show slight negative correlations (-0.18 and -0.17 respectively) with order volumes. The box plot distribution of order counts by location further emphasizes the regional variations, with California and Chicago showing the highest median orders and largest variability, while Washington DC displays the most consistent but lowest order volumes.

The temperature category analysis reveals interesting patterns across regions. Mild temperatures appear to be optimal for order volumes in most locations, as shown in the bar chart comparing average orders by temperature category. California and Chicago particularly thrive in mild conditions, while other locations show more varied responses to temperature changes. The wind speed analysis suggests a moderate influence on order patterns, with most locations showing decreased order volumes during higher wind speed conditions.

## Future Work:

The visualizations provides valuable insights into the relationship between weather conditions and order patterns across different locations. Looking ahead, several critical opportunities emerge from this weather-impact analysis that could enhance both methodology and business insights:
Methodological Improvements
The current analysis could be strengthened through more sophisticated statistical approaches. Implementing time series analysis and machine learning models would better capture the complex relationships between weather variables and order patterns. Additionally, incorporating lag effects and seasonal adjustments could reveal deeper patterns currently masked by the simple correlation analysis.
Data Enhancement Opportunities

The visualization suite reveals gaps in our current data collection approach. Future iterations should focus on:

* Expanding the temporal granularity to capture intra-day weather variations and their immediate impact on ordering patterns
* Including additional weather metrics such as humidity, UV index, and "feels like" temperature that might better explain ordering behavior
* Collecting complementary data points like local events, holidays, and promotional activities to control for non-weather variables

## Reproducing: 

**1. Data Acquisition**

Online Shopping Dataset:

https://www.kaggle.com/datasets/jacksondivakarr/online-shopping-dataset
Extract the online_sales.csv file with 52,955 rows related to customer behavior.

The Online Shopping Dataset can be downloaded programmatically using the Kaggle API. To reproduce this step:

Install the Kaggle Python package:

1. (bash) pip install kaggle
2. Set up your Kaggle API credentials:
    * Go to your Kaggle account settings: https://www.kaggle.com/account
    * Create a new API token. This will download a file named kaggle.json.
    * Save the file in a secure location (~/.kaggle/kaggle.json) or extract the username and key fields from the file.
    
        (^ the first option was not working for me, so I chose to extract the username and key fields. IS 477 TAS GRADING THIS ASSIGNMENT ARE WELCOME TO USE MY CREDENTIALS IN THE SECURE BOX DRIVE.)

    * Export your Kaggle credentials to the environment using the following commands:
    
        (bash) export KAGGLE_USERNAME=your_kaggle_username
    
        (bash) export KAGGLE_KEY=your_kaggle_key

Weather Data:
Register for an API key on the Storm Glass API website to retrieve hourly weather data (temperature, precipitation, and wind speed) for the cities of interest (Again, IS 477 TAs are welcome to use my key located in the secure drive).

https://docs.stormglass.io/#/

**2. Data Preprocessing**

Clean and Format the Data:
Load the online_sales.csv and ensure the Transaction_Date is in a datetime format.
Retrieve weather data for the same time period, ensuring consistency with the sales data.
Merge both datasets based on the transaction date and location.

**3. Data Analysis**

Explore Descriptive Statistics:

Calculate basic statistics for key variables like Online_Spend, Temperature, Precipitation, Wind Speed.
Visualize data distributions with histograms or scatter plots.

Analyze Correlations:

Use correlation matrices to check for relationships between weather variables and shopping behavior.
Run regression models (e.g., linear regression) to quantify the impact of weather on spending and order volume.

**4. Interpretation and Visualization**

Interpret Results:
Assess correlation and regression results to determine how weather factors like temperature, precipitation, and wind speed influence shopping behavior.

Visualize the findings using charts (e.g., line graphs, heatmaps) to show trends across cities.

**5. Reporting**

Summarize Findings:
Document key findings, such as the impact of temperature on spending and how weather conditions affect different cities differently.

Provide Recommendations:
Suggest actionable insights, such as tailoring marketing strategies based on weather conditions or optimizing inventory during specific weather events.

**6. Reproducibility Checklist**

Ensure all datasets are accessible, and the environment is set up with necessary libraries (e.g., Pandas, Matplotlib, Statsmodels, Requests).
Use version control to store scripts for transparency and reproducibility.

## References:

1. "Online Shopping Data (file.csv) accessed from Kaggle: https://www.kaggle.com/datasets/jacksondivakarr/online-shopping-dataset/data, accessed on December 13th, 2024."

2. Kaggle. (n.d.). Kaggle API. GitHub. Retrieved December 13, 2024, from https://github.com/Kaggle/kaggle-api/blob/main/docs/README.md

3. Storm Glass. (n.d.). Weather API - Point Request. Retrieved December 13, 2024, from https://api.stormglass.io/v2/weather/point

4. Microsoft Corporation. (2024). Visual Studio Code. https://code.visualstudio.com/

5. Stack Exchange Inc. (2024). Stack Overflow. https://stackoverflow.com/
