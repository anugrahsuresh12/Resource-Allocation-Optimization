import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_time_series(df, column, output_dir):
    """Plot and save a line plot for time-based trends."""
    if column in df.columns:
        plt.figure(figsize=(10, 6))
        # Convert 'EntryTimeandDate' column to datetime
        df['EntryTimeandDate'] = pd.to_datetime(df['EntryTimeandDate'])
        # Group by date and calculate the mean of the specified column
        df_grouped = df.groupby(df['EntryTimeandDate'].dt.date)[column].mean()
        df_grouped.plot(kind='line', color='skyblue')
        plt.title(f'Time-Based Trends for {column}')
        plt.xlabel('Date')
        plt.ylabel(column)
        plot_path = os.path.join(output_dir, f"{column}_time_series.png")
        plt.savefig(plot_path)  # Save the plot as a PNG file
        plt.close()  # Close the figure to avoid overlapping plots
        print(f"Saved {column} Time Series Plot to {plot_path}")
    else:
        print(f"Column '{column}' not found in the dataset.")

def plot_time_of_day_heatmap(df, column_name, output_dir):
    """Plot heatmap for time-of-day patterns for a specified column."""
    # Ensure that 'EntryTimeandDate' is in datetime format
    df['EntryTimeandDate'] = pd.to_datetime(df['EntryTimeandDate'], errors='coerce')  # Coerce any errors to NaT
    if df['EntryTimeandDate'].isnull().all():
        print("EntryTimeandDate column is not properly formatted or contains no valid values.")
        return

    # Extract the hour from 'EntryTimeandDate'
    df['Hour'] = df['EntryTimeandDate'].dt.hour

    # Pivot the data for heatmap (you may adjust depending on how you want to structure it)
    df_pivoted = df.pivot_table(values=column_name, index='Hour', aggfunc='mean')

    # Check if the pivoted data is empty
    if df_pivoted.empty:
        print(f"No data available for plotting heatmap of {column_name}.")
        return

    # Plot the heatmap if data is available
    plt.figure(figsize=(10, 6))
    sns.heatmap(df_pivoted, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title(f'{column_name} Time-of-Day Heatmap')
    plt.ylabel('Hour of Day')
    plt.xlabel(f'Column: {column_name}')

    # Save the heatmap
    output_path = os.path.join(output_dir, f'{column_name}_time_of_day_heatmap.png')
    plt.savefig(output_path)
    print(f"Saved {column_name} Time-of-Day Heatmap to {output_path}")
    plt.close()
