import pandas as pd
import os
import snakemake
from datetime import datetime

def parse_datetime(date_str):
    try:
        return pd.to_datetime(date_str)
    except:
        try:
            return pd.to_datetime(date_str, format='%Y-%m-%d')
        except:
            print(f"Could not parse date: {date_str}")
            return None

def load_and_prepare_data(weather_df, orders_df):
    # print(f"Loading data: {weather_file}, {orders_file}")
    # weather_df = pd.read_csv(weather_file)
    # orders_df = pd.read_csv(orders_file)

    # Standardize columns
    weather_df['date'] = weather_df['time'].apply(parse_datetime)
    weather_df['location'] = weather_df['Location']
    weather_df['temperature'] = weather_df['airTemperature']
    
    orders_df['date'] = orders_df['Transaction_Date'].apply(parse_datetime)
    
    weather_df['date_only'] = weather_df['date'].dt.date
    orders_df['date_only'] = orders_df['date'].dt.date
    
    orders_grouped = orders_df.groupby(['Location', 'date_only']).size().reset_index(name='order_count')
    
    weather_grouped = weather_df.groupby(['location', 'date_only']).agg({
        'temperature': 'mean',
        'precipitation': 'mean',
        'windSpeed': 'mean'
    }).reset_index()
    
    merged_df = pd.merge(
        weather_grouped, 
        orders_grouped, 
        left_on=['location', 'date_only'], 
        right_on=['Location', 'date_only'], 
        how='inner'
    )
    
    merged_df = merged_df.rename(columns={
        'temperature': 'avg_temperature',
        'windSpeed': 'wind_speed'
    })
    
    return merged_df

def main():
    weather_file = pd.read_csv('python scripts/data/allweather_df.csv', sep=',', engine='python')
    orders_file = pd.read_csv('python scripts/data/onlineorder_clean.csv', sep=',', engine='python')

    print(f"Preparing data for: {weather_file}, {orders_file}")
    merged_data = load_and_prepare_data(weather_file, orders_file)
    
    merged_data.to_csv("intermediate/merged_data.csv", index=False)

if __name__ == "__main__":
    main()
