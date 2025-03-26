# 1. Overview of Project and Updates

## 1.1 Project Plan Update
Originally, the project was designed to analyze DoorDash order patterns and how weather affects food delivery frequency and timing. However, we encountered a significant issue with the dataset. The DoorDash dataset we initially selected did not specify the location of the orders. Instead, it only contained numerical IDs (e.g., 1, 2, 3) to represent the locations, which made it impossible to accurately link weather data to the orders based on location. Because the weather data is location-dependent, this created a major roadblock in our original project plan.

To resolve this issue, we decided to revise our project plan. The new focus is on Analyzing Weather and Time Impact on Online Shopping Behavior. In this updated plan, we will examine how external factors such as weather conditions and time of day affect online shopping activity, focusing on aspects like the time spent shopping online, the total amount spent, and product category preferences.
The revised research questions are:

  * How does weather influence the time spent shopping online and the total amount spent?

  * Are certain product categories (e.g., electronics, home appliances) purchased more frequently during specific weather conditions?

## 1.2 Datasets

We have shifted from using the DoorDash dataset to an Online Shopping dataset, which contains detailed information about online shopping transactions. The dataset includes variables such as customer ID, transaction ID, product description, quantities purchased, average prices, and online and offline spending, among others. This dataset offers sufficient detail to analyze shopping behaviors and correlate them with weather data, which is a key component of our new research focus.

Additionally, we are using the OpenWeather API (One Call API 3.0) to retrieve weather data for the locations where the transactions occurred. We have the capability to pull historical weather data based on latitude, longitude, and date, allowing us to link weather conditions with online shopping activity.

## 1.3 Challenges and Adjustments
The primary challenge so far has been the issues with the DoorDash dataset’s location data, which forced us to pivot to a new project focus. The change in the project scope to analyzing online shopping behavior and weather impact has involved creating new workflows and re-evaluating our initial research approach. This approach was timely and took longer than we anticipated, but our team agreed it was best to entirely shift focus for the integrity of our analysis. However, we are still confident this new direction will yield valuable insights into how weather influences online shopping behaviors.

# 2. Task Updates

## 2.1 Dataset Acquisition
Status: Completed

Artifacts: online_shopping_dataset.csv
* We successfully acquired the Online Shopping dataset. This dataset was sourced from Kaggle and contains information on transactions from an e-commerce platform (Google Merchandise Store), including transaction IDs, product details, customer demographics, and spending data. 

* We have loaded this dataset into our working environment and performed an initial review to understand its structure and key variables.
Obtained the OpenWeather API key and verified that we can pull historical weather data based on geographic coordinates. The weather data we are able to collect will include key variables such as temperature, precipitation, wind speed, and weather conditions (e.g., rain, snow, etc.). 

* Created a .gitignore file in our project repository and added the file containing the API key (weather_apikey.txt) to the list of ignored files for enhanced security (prevents the API key from being uploaded to GitHub, protecting it from unauthorized access).

## 2.2 Dataset Integration
Status: In Progress

Artifacts: data_integration_pt1.ipynb
* Challenges: Currently, we have a basic script to pull weather data for Chicago on specific dates using the OpenWeather API. However, we are still in the process of ensuring that the weather data integrates with the online shopping transaction data. We plan to merge the two datasets by date and location, which will involve handling discrepancies in format and ensuring that the weather data corresponds to the correct transactional period. 

## 2.3 Data Profiling and Quality Assessment
Status: In Progress

Artifacts: data_integration_pt1.ipynb

* We have begun profiling the dataset and identified several areas that need cleaning. We have started cleaning these missing values by imputing them or removing incomplete records. We will continue this process to ensure the dataset is ready for analysis.

* We are currently speculating whether or not to create a preliminary report on missing values, stored in a missing_values_report.md. The report would outline variables that have the highest percentage of missing data and describe the steps we will take to address these gaps.

## 2.4 Reproducibility Package
Status: Pending
Artifacts: None currently

## 2.5 Workflow Automation
Status: Pending
Artifacts: None currently

## 2.6 Data Analysis and Visualization
Status: Pending
Artifacts: None currently

## 2.7 Archiving and Metadata
Status: Pending
Artifacts: None currently


# 3. Updated Timeline

| Task                                     | Status       | Planned Completion Date      |
|------------------------------------------|--------------|------------------------------|
| **Dataset Acquisition**                  | Completed    | Completed                    |
| **Dataset Integration**                  | In Progress  | Week 7                       |
| **Data Profiling and Quality Assessment**| In Progress  | Week 7 - Early Week 8        |
| **Data Analysis/Visualization + Reproducible Package** | Pending     | Early Week 8 + Week 9       |
| **Citation of Data + Software**          | Pending      | Week 11                      |
| **Archiving and Metadata**               | Pending      | Week 13                      |


# 4. Changes to Project Plan
The major change to the project plan was the pivot from analyzing DoorDash order patterns to studying the impact of weather and time on online shopping behavior. This was due to the limitations in the DoorDash dataset we had initially chosen. While this change required an adjustment in our workflows, we are still confident this new direction will allow us to generate meaningful insights.
As a result of this change, we had to adapt our timeline, research questions, and focus on how external factors like weather conditions influence online shopping behaviors, which fits well with the available dataset.
