import mysql.connector
from mysql.connector import Error

def connect_to_database():
    try:
        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(
            host='localhost',        # Replace with your database host
            database='sdp',  # Replace with your database name
            user='root',             # Replace with your MySQL username
            password='admin123' # Replace with your MySQL password
        )

        if connection.is_connected():
            print("Successfully connected to the database")
            cursor = connection.cursor()

            # Step 2: Create a table
            create_table_query = """
            CREATE TABLE IF NOT EXISTS students (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                age INT,
                gender VARCHAR(10)
            )
            """
            cursor.execute(create_table_query)
            print("Table 'students' created successfully.")

            # Step 3: Insert records into the table (Create)
            insert_query = """
            INSERT INTO students (name, age, gender)
            VALUES (%s, %s, %s)
            """
            student_records = [
                ('Alice', 22, 'Female'),
                ('Bob', 24, 'Male'),
                ('Charlie', 23, 'Male')
            ]
            cursor.executemany(insert_query, student_records)
            connection.commit()
            print(f"{cursor.rowcount} records inserted into 'students' table.")

            # Step 4: Retrieve records from the table (Read)
            select_query = "SELECT * FROM students"
            cursor.execute(select_query)
            records = cursor.fetchall()
            print("Fetching data from 'students' table:")
            for row in records:
                print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Gender: {row[3]}")

            # Step 5: Update records in the table (Update)
            update_query = """
            UPDATE students
            SET age = %s
            WHERE name = %s
            """
            data_to_update = (25, 'Alice')
            cursor.execute(update_query, data_to_update)
            connection.commit()
            print(f"Record updated for {cursor.rowcount} student(s).")

            # Verify the update
            cursor.execute(select_query)
            records = cursor.fetchall()
            print("Data after update:")
            for row in records:
                print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Gender: {row[3]}")

            # Step 6: Delete records from the table (Delete)
            delete_query = "DELETE FROM students WHERE name = %s"
            name_to_delete = ('Bob',)
            cursor.execute(delete_query, name_to_delete)
            connection.commit()
            print(f"Record deleted for {cursor.rowcount} student(s).")

            # Verify the deletion
            cursor.execute(select_query)
            records = cursor.fetchall()
            print("Data after deletion:")
            for row in records:
                print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Gender: {row[3]}")

            # Step 7: Drop the table after operations (Cleanup)
            drop_table_query = "DROP TABLE IF EXISTS students"
            cursor.execute(drop_table_query)
            print("Table 'students' dropped successfully.")

            # Close the cursor
            cursor.close()

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

# Call the function to execute CRUD operations
connect_to_database()