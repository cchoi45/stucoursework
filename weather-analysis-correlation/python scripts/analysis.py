import pandas as pd
from sklearn.linear_model import LinearRegression
import json
import snakemake

def detailed_location_analysis(merged_df):
    analysis_results = {}
    
    for location in merged_df['location'].unique():
        location_data = merged_df[merged_df['location'] == location]
        
        location_analysis = {}
        
        # correlation analysis
        correlation_metrics = ['avg_temperature', 'precipitation', 'wind_speed']
        correlations = location_data[correlation_metrics + ['order_count']].corr()['order_count'][correlation_metrics]
        location_analysis['correlations'] = correlations.to_dict()
        
        # regression analysis for temp impact
        from sklearn.linear_model import LinearRegression
        
        # temp impact
        X = location_data[['avg_temperature']]
        y = location_data['order_count']
        
        reg = LinearRegression().fit(X, y)
        
        location_analysis['temperature_impact'] = {
            'slope': reg.coef_[0],
            'intercept': reg.intercept_,
            'r_squared': reg.score(X, y)
        }
        
        location_analysis['total_orders'] = int(location_data['order_count'].sum())
        location_analysis['average_daily_orders'] = location_data['order_count'].mean()
        location_analysis['weather_summary'] = {
            'avg_temperature': location_data['avg_temperature'].mean(),
            'avg_precipitation': location_data['precipitation'].mean(),
            'avg_wind_speed': location_data['wind_speed'].mean()
        }
        
        analysis_results[location] = location_analysis
    
    return analysis_results

def main():
    merged_data = pd.read_csv('intermediate/merged_data.csv')

    location_impact = detailed_location_analysis(merged_data)
    analysis_results_output = 'results/analysis_results.json'

    # save analysis results to json
    with open(analysis_results_output, 'w') as f:
        json.dump(location_impact, f, indent=4)

if __name__ == '__main__':
    main()