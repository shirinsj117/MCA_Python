import csv

file_name = 'car.csv'
columns_to_read = ['Company', 'Car Model']

try:
    with open(file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        
        # Check for missing columns
        missing_columns = [col for col in columns_to_read if col not in reader.fieldnames]
        
        if missing_columns:
            print(f"Error: Missing columns in the file: {', '.join(missing_columns)}")
        else:
            # If all required columns are present, print the column headers
            print(", ".join(columns_to_read))
            
            # Iterate over the rows in the CSV file
            for row in reader:
                print(", ".join(row[col] for col in columns_to_read))
                
except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
