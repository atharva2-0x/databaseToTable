import sqlite3

def map_consumer_data(consumer_data):
    mapped_data = []
    for consumer in consumer_data:
        try:
            name = consumer[1]
            first_name, last_name = name.split()
            address = consumer[2]
            # Split address into parts
            address_parts = [part.strip() for part in address.split(',')]
            if len(address_parts) >= 3:
                address_line_1 = address_parts[0]
                address_line_2 = address_parts[1]
                city = address_parts[-2]
                state = address_parts[-3]
                zip_code = address_parts[-1]
            else:
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
        except Exception as e:
            print(f"Error occurred while mapping consumer data: {e}")
    return mapped_data

def create_mapped_database(mapped_data, database_name):
    try:
        conn = sqlite3.connect(database_name)
        cur = conn.cursor()
        
        # Create a table to store the mapped data
        cur.execute('''
        CREATE TABLE IF NOT EXISTS mapped_consumers (
            id INTEGER PRIMARY KEY,
            consumer_id INTEGER,
            first_name TEXT,
            last_name TEXT,
            address_line_1 TEXT,
            address_line_2 TEXT,
            city TEXT,
            state TEXT,
            zip_code TEXT,
            phone_number TEXT,
            email_address TEXT
        )
        ''')
        
        for consumer in mapped_data:
            cur.execute('''
            INSERT INTO mapped_consumers 
            (consumer_id, first_name, last_name, address_line_1, address_line_2, city, state, zip_code, phone_number, email_address)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                consumer['Consumer ID'],
                consumer['First Name'],
                consumer['Last Name'],
                consumer['Address Line 1'],
                consumer['Address Line 2'],
                consumer['City'],
                consumer['State'],
                consumer['Zip Code'],
                consumer['Phone Number'],
                consumer['Email Address']
            ))
        
        conn.commit()
    except sqlite3.Error as e:
        print(f"SQLite error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

try:
    conn = sqlite3.connect('demo_database.db')
    cur = conn.cursor()
    
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
    
    cur.execute(sql_query)
    rows = cur.fetchall()
    mapped_data = map_consumer_data(rows)
    create_mapped_database(mapped_data, 'mapped_database_1.db')
finally:
    if cur:
        cur.close()
    if conn:
        conn.close()
