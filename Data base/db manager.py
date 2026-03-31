#

from os import name

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
def add_staff(name,email,enrolment_year):
    insert_query = """\
        INSERT INTO staff (name, email, enrolment_year)
        VALUES (%s, %s, %s);
        """
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(insert_query,(name,email,enrolment_year))
            connection.commit()
            print("Staff added successfully")
def get_all_staff():
    select_query = """\
        SELECT id, name, email, enrolment_year FROM staff;
        """
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(select_query)
            staff_list = cursor.fetchone()
            print("Staff List:", staff_list)
            # for staff in staff_list:
                # print(f"ID: {staff[0]}, Name: {staff[1]}, Email: {staff[2]}, Enrolment Year: {staff[3]}")
            return staff_list 
def clear_staff():
    delete_query = """\
        TRUNCATE TABLE staff RESTART IDENTITY;
        """
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(delete_query)
            connection.commit()
            print("All staff records cleared successfully")
            
if __name__=="__main__":
    create_table() 
    clear_staff()
    sample_students = [
    ("Alice Johnson", "alice.j@example.com", "2026001"),
    ("Bob Smith", "b.smith@provider.net", "2026002"),
    ("Charlie Davis", "charlie.d@university.edu", "2026003"),
    ("Diana Prince", "diana.p@webmail.com", "2026004"),
    ("Edward Norton", "ed.norton@demo.org", "2026005"),
    ("Fiona Gallagher", "fiona.g@service.com", "2026006"),
    ("George Miller", "g.miller@academy.io", "2026007")
]
    for i in sample_students:
        # print(f"add staff : {i[0]},{i[1]},{i[2]}")
        add_staff(i[0],i[1],i[2])
        
    get_all_staff()
    
    