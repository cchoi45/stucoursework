import pandas as pd
import requests
import zipfile
import arrow
from kaggle.api.kaggle_api_extended import KaggleApi

def download_and_extract_dataset():
    api = KaggleApi()
    api.authenticate()

    api.dataset_download_files('jacksondivakarr/online-shopping-dataset')

    with zipfile.ZipFile('online-shopping-dataset.zip', 'r') as zip_ref:
        zip_ref.extractall('python scripts/data')

def clean_orders_data(csv_file_path):
    df = pd.read_csv(csv_file_path)

    df.dropna(inplace=True)
    if 'Unnamed: 0' in df.columns:
        df.drop(['Unnamed: 0'], axis=1, inplace=True)

    df['Transaction_Date'] = pd.to_datetime(df['Transaction_Date'])
    date_count = df.groupby('Transaction_Date').size().reset_index(name='Order_Count')
    date_count.sort_values(by='Order_Count', ascending=False, inplace=True)

    high_order_dates = date_count.head(5)['Transaction_Date']
    low_order_dates = date_count.tail(5)['Transaction_Date']
    selected_dates = pd.concat([high_order_dates, low_order_dates]).sort_values().reset_index(drop=True)

    df_clean = df[df['Transaction_Date'].isin(selected_dates)]
    return df_clean

def orders_per_location(df, dates):
    filtered_df = df[df['Transaction_Date'].isin(dates)]
    location_counts = (
        filtered_df
        .groupby(['Transaction_Date', 'Location'])
        .size()
        .reset_index(name='Order_Count')
    )
    return location_counts

def fetch_weather_data(dates, lat, lng, params, api_key):
    all_data = []

    for date_str in dates:
        # convert to arrow obj
        day_start = arrow.get(date_str).shift(hours=1).to('UTC')
        day_end = arrow.get(date_str).shift(hours=23).to('UTC')

        # make call
        response = requests.get(
            'https://api.stormglass.io/v2/weather/point',
            params={
                'lat': lat,
                'lng': lng,
                'start': day_start.timestamp(),
                'end': day_end.timestamp(),
                'params': ','.join(params)
            },
            headers={
                'Authorization': api_key
            }
        )

        if response.status_code == 200:
            json_data = response.json()
            all_data.extend(json_data['hours'])
        else:
            print(f"Failed to fetch data for {date_str}: {response.status_code}")

    return pd.DataFrame(all_data)

def clean_weather_data(df, location):
    cleaned_data = {
        'Location': location,
        'airTemperature': df['airTemperature'].apply(lambda x: x['noaa']),
        'precipitation': df['precipitation'].apply(lambda x: x['noaa']),
        'time': df['time'],
        'windSpeed': df['windSpeed'].apply(lambda x: x['noaa'])
    }
    return pd.DataFrame(cleaned_data)

def main():
    # 1. download and extract dataset
    download_and_extract_dataset()

    # 2. clean order data
    csv_file_path = 'python scripts/data/file.csv'
    df_clean = clean_orders_data(csv_file_path)

    # save cleaned data
    df_clean.to_csv('/Users/cynthiachoi/is477_final/is477-fa24-dicy/data/onlineorder_clean.csv', index=False)

    # 3. fetch weather data
    with open('data/weather_apikey.txt', 'r') as file:
        api_key = file.read().strip()

    parameters = ['airTemperature', 'precipitation', 'windSpeed']

    locations = [
        (['2019-11-27', '2019-07-13', '2019-08-16', '2019-08-02', '2019-07-31', '2019-01-28', '2019-02-05', '2019-12-24'], 41.8500, -87.6501, "Chicago"),
        (['2019-07-01', '2019-07-13', '2019-07-31', '2019-08-02', '2019-11-27'], 38.8951, -77.0364, "Washington DC"),
        (['2019-07-13', '2019-07-31', '2019-08-02', '2019-08-16', '2019-11-27', '2019-01-28', '2019-02-05', '2019-07-01', '2019-08-20', '2019-12-24'], 37.269175, -119.30661, "California"),
        (['2019-07-13', '2019-07-31', '2019-08-02', '2019-08-16', '2019-11-27', '2019-08-20', '2019-12-24'], 40.730610, -73.935242, "New York"),
        (['2019-11-27', '2019-08-02', '2019-07-31', '2019-12-24'], 39.833851, -74.871826, "New Jersey")
    ]

    weather_dfs = []

    for dates, lat, lng, location in locations:
        raw_weather_df = fetch_weather_data(dates, lat, lng, parameters, api_key)
        cleaned_weather_df = clean_weather_data(raw_weather_df, location)
        weather_dfs.append(cleaned_weather_df)

    allweather_df = pd.concat(weather_dfs, ignore_index=True)

    # save weather data
    allweather_df.to_csv('/Users/cynthiachoi/is477_final/is477-fa24-dicy/data/allweather_df.csv', index=False)

if __name__ == "__main__":
    main()