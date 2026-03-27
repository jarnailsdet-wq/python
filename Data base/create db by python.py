#
import psycopg2 as g2
from psycopg2 import OperationalError
def test_database():
    db = {
        "host":"127.0.0.1",
        "database":"collage_erp",
        "user": "postgres",
        "password":"js12345",
        "port":"5432"        
    }
    connection=None
    try:
        connection = g2.connect(**db)
        crs = connection.cursor()
        crs.execute("SELECT version();")
        db_version = crs.fetchone()
        print(f"success connect : {db_version[0]}")
        crs.close()
    except OperationalError as e:
        print(f"An error occures: {e}")
    finally:
        if connection is not None:
            connection.close()
            print("data base connection closed")
if __name__=="__main__":
    test_database()                    