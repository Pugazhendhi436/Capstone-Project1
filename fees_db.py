import pandas as pd
import mysql.connector #pip install mysql-connector-python

# Read Excel file
df = pd.read_excel("fees_report.xlsx")

# Debug: Check DataFrame shape and columns
print(f"DataFrame shape: {df.shape}")  # Should be (num_rows, 11)
print(f"Columns: {list(df.columns)}")  # Should match the 11 fields

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="school"
)

cursor = conn.cursor()

# Insert query
query = """
INSERT INTO fees (
    id ,Name ,class, tuition, transport, hostel, paid, duedate,
    total_fees, late_fee, final_amount, balance, status
) VALUES (%s ,%s ,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""
print(df.shape[1])
# Convert DataFrame to list of tuples (ensure exactly 13 columns)
if df.shape[1] != 13:
    raise ValueError(f"Excel file must have exactly 13 columns, but has {df.shape[1]}")

# Convert DataFrame to list of tuples
data = [tuple(row) for row in df.to_numpy()]

# Debug: Check first tuple length
print(f"First data tuple length: {len(data[0])}")  # Should be 11

print("Inserting data into database...")




# ...existing code...
try:
    cursor.executemany(query, data)
    conn.commit()
    print("Data inserted successfully!")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    cursor.close()
    df = pd.read_sql("SELECT * FROM fees", conn)
    print(df.head())
    print(df.columns)
    print(f"Total records in database: {len(df)}")

    conn.close()

    # TRUNCATE TABLE `fees`;
    # SELECT * FROM `fees`