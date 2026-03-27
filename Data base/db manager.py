#

import psycopg2 as ps
db = {
        "host":"127.0.0.1",
        "database":"collage_erp",
        "user": "postgres",
        "password":"js12345",
        "port":"5432"        
    }
def get_connection():
    return ps.connect(**db)
def create_table():
    create_table_query = """\
        CREATE TABLE IF NOT EXISTS staff (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL
            ,enrolment_year INTEGER NOT NULL
        );
        """
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(create_table_query)
            connection.commit()
            print("Table created successfully")   
if __name__=="__main__":
    create_table() 