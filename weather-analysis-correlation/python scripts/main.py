# SCRATCH PAPER .PY
# import pandas as pd
# import json
# from data_cleaning import load_and_prepare_data
# from visualization import create_comprehensive_analysis
# from analysis import detailed_location_analysis

# def main():
#     weather_file = 'allweather_df.csv'
#     orders_file = 'onlineorder_clean.csv'
    
#     visualization_output = 'results/visualization.png'
#     visualization_results_output = 'results/visualization_results.json'
#     analysis_results_output = 'results/analysis_results.json'
    
#     # prep data
#     merged_data = load_and_prepare_data(weather_file, orders_file)
    
#     # create viz and save
#     visualization_results = create_comprehensive_analysis(merged_data, visualization_output)
    
#     # save viz results to json
#     with open(visualization_results_output, 'w') as f:
#         json.dump(visualization_results, f)
    
#     # statistical analysis
#     location_impact = detailed_location_analysis(merged_data)
    
#     # save analysis results to json
#     with open(analysis_results_output, 'w') as f:
#         json.dump(location_impact, f)
    
#     # print results
#     print("\nLocation-Specific Weather Impact Analysis:")
#     for location, details in location_impact.items():
#         print(f"\n{location}:")
#         print("Correlations with Order Count:")
#         for metric, correlation in details['correlations'].items():
#             print(f"  {metric}: {correlation:.4f}")
        
#         print("\nTemperature Impact:")
#         print(f"  Slope: {details['temperature_impact']['slope']:.4f}")
#         print(f"  R-Squared: {details['temperature_impact']['r_squared']:.4f}")
        
#         print("\nOrder Metrics:")
#         print(f"  Total Orders: {details['total_orders']}")
#         print(f"  Average Daily Orders: {details['average_daily_orders']:.2f}")
        
#         print("\nWeather Summary:")
#         for metric, value in details['weather_summary'].items():
#             print(f"  {metric}: {value:.2f}")

# if __name__ == "__main__":
#     main()
