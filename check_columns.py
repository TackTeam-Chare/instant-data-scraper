import pandas as pd

def check_columns(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Columns in the file:")
        print(df.columns.tolist())
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_file = 'google.csv'
    check_columns(input_file)
