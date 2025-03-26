import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import snakemake
import numpy as np
import json

def create_comprehensive_analysis(merged_df, output_file):
    print('here)')
    # prep plot
    plt.figure(figsize=(20, 15))
    
    # unique locations
    locations = merged_df['location'].unique()
    
    # create subplot grid
    fig, axes = plt.subplots(3, 2, figsize=(20, 15))
    axes = axes.ravel()  # Flatten axes array
    
    # weather metrics to analyze
    metrics = ['avg_temperature', 'precipitation', 'wind_speed']
    
    palette = sns.color_palette("husl", len(locations))
    
    # scatter plots for each metric
    for i, metric in enumerate(metrics):
        ax = axes[i]
        for j, location in enumerate(locations):
            location_data = merged_df[merged_df['location'] == location]
            ax.scatter(
                location_data[metric], 
                location_data['order_count'], 
                label=location, 
                color=palette[j], 
                alpha=0.7
            )
        ax.set_title(f'Orders vs {metric.replace("_", " ").title()}')
        ax.set_xlabel(f'{metric.replace("_", " ").title()}')
        ax.set_ylabel('Number of Orders')
        ax.legend()
    
    # correlation heatmap
    correlation_metrics = ['avg_temperature', 'precipitation', 'wind_speed', 'order_count']
    correlation_data = merged_df[correlation_metrics].corr()
    
    ax = axes[3]
    sns.heatmap(
        correlation_data,
        annot=True,
        cmap='coolwarm',
        center=0,
        ax=ax
    )
    ax.set_title('Correlation of Weather Metrics with Orders')
    
    # box plot of order counts by location
    ax = axes[4]
    sns.boxplot(
        x='location',
        y='order_count',
        data=merged_df,
        ax=ax
    )
    ax.set_title('Distribution of Order Counts by Location')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    
    # temp category analysis
    ax = axes[5]
    merged_df['temp_category'] = pd.cut(
        merged_df['avg_temperature'],
        bins=[-float('inf'), 10, 20, 30, float('inf')],
        labels=['Very Cold', 'Cold', 'Mild', 'Hot']
    )
    
    avg_orders = merged_df.groupby(['location', 'temp_category'])['order_count'].mean().unstack()
    avg_orders.plot(kind='bar', ax=ax)
    ax.set_title('Average Orders by Temperature Category and Location')
    ax.set_xlabel('Location')
    ax.set_ylabel('Average Number of Orders')
    
    plt.tight_layout()
    # save plot to file
    plt.savefig(output_file)
    plt.close()
    
    return {
        'overall_correlation': correlation_data,
        'order_distribution': merged_df.groupby('location')['order_count'].describe()
    }

def main():
    merged_data = pd.read_csv('intermediate/merged_data.csv')
    visualization_output = 'results/visualization.png'

    create_comprehensive_analysis(merged_data, visualization_output)

if __name__ == "__main__":
    main()