# eda.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from timeseries import plot_time_series, plot_time_of_day_heatmap

def load_data(file_path):
    """Load cleaned data from the provided Excel file."""
    df = pd.read_excel(file_path)
    return df

def perform_eda(file_path):
    """Perform Exploratory Data Analysis (EDA) on the cleaned dataset."""

    # Load the data
    df = load_data(file_path)

    # Create a directory for saving the plots
    output_dir = os.path.join(os.path.dirname(file_path), 'eda_plots')
    os.makedirs(output_dir, exist_ok=True)

    # Display basic descriptive statistics
    print("Descriptive Statistics:")
    print(df.describe())
    print("\n")

    # Check for missing values
    print("Missing Values:")
    print(df.isnull().sum())
    print("\n")

    # Check data types
    print("Data Types:")
    print(df.dtypes)
    print("\n")

    # Plot correlation heatmap for numeric columns
    def plot_correlation_heatmap(df):
        """Plot the correlation heatmap for numeric columns."""
        # Select only numeric columns for correlation
        numeric_df = df.select_dtypes(include=['float64', 'int64'])  # Selecting numeric columns only

        # Calculate the correlation matrix
        correlation_matrix = numeric_df.corr()

        # Plot heatmap if there are numeric columns
        if not correlation_matrix.empty:
            plt.figure(figsize=(10, 8))  # Set figure size
            sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)  # Plot heatmap
            plt.title('Correlation Heatmap')  # Add title
            plt.show()
        else:
            print("No numeric columns available for correlation.")

    # Plot correlation heatmap
    plot_correlation_heatmap(df)

    # Plot histogram for a selected numeric column
    def plot_histogram(df, column):
        """Plot histogram for a specified column."""
        plt.figure(figsize=(8, 6))
        sns.histplot(df[column], kde=True, bins=30, color='skyblue')
        plt.title(f'{column} Distribution')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.show()

    # Example of plotting histograms for specific columns
    plot_histogram(df, 'Medication Revenue')
    plot_histogram(df, 'Lab Cost')

    # Perform time-based analysis
    plot_time_series(df, 'Consultation Revenue', output_dir)  # Example column: 'Consultation Revenue'
    plot_time_of_day_heatmap(df, 'Consultation Revenue', output_dir)  # Example column: 'Consultation Revenue'

    # More visualizations can be added as needed
    print("EDA completed!")
