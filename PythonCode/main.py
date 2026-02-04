# main.py
from eda import perform_eda

def main():
    # Define the path to your cleaned Excel file
    cleaned_data_path = 'cleaned_data.xlsx'

    # Perform the exploratory data analysis (EDA)
    perform_eda(cleaned_data_path)

if __name__ == "__main__":
    main()
