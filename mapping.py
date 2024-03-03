import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('demo_database.db')

# Create a cursor object to interact with the database
cur = conn.cursor()

# SQL query to extract consumer data
sql_query = '''
SELECT 
    consumer_id, 
    name, 
    address, 
    contact_number, 
    email_address, 
    account_number, 
    meter_number, 
    tariff_plan, 
    consumption_history, 
    payment_status 
FROM 
    consumers
'''

# Execute the SQL query
cur.execute(sql_query)

# Fetch all the rows from the database
rows = cur.fetchall()

# Close the cursor and connection
cur.close()
conn.close()

# Function to map the consumer data to the corresponding tables
def map_consumer_data(consumer_data):
    mapped_data = []
    for consumer in consumer_data:
        name = consumer[1]
        first_name, last_name = name.split()
        address = consumer[2]
        # Split address into parts
        address_parts = [part.strip() for part in address.split(',')]
        if len(address_parts) >= 3:
            # Extract address components
            address_line_1 = address_parts[0]
            address_line_2 = address_parts[1]
            city = address_parts[-3]
            state = address_parts[-2]
            zip_code = address_parts[-1]
        else:
            # Handle cases where address may not have all parts
            address_line_1 = address_parts[0] if address_parts else ''
            address_line_2 = ''
            city = state = zip_code = ''
            
        contact_number = consumer[3]
        email_address = consumer[4]
        
        mapped_consumer = {
            'Consumer ID': consumer[0],
            'First Name': first_name,
            'Last Name': last_name,
            'Address Line 1': address_line_1,
            'Address Line 2': address_line_2,
            'City': city,
            'State': state,
            'Zip Code': zip_code,
            'Phone Number': contact_number,
            'Email Address': email_address
        }
        mapped_data.append(mapped_consumer)
    return mapped_data

# Map the consumer data to the corresponding tables
mapped_data = map_consumer_data(rows)

# Print the mapped data
for consumer in mapped_data:
    print(consumer)
