import psycopg2

def connexion_db():
    host = 'db'
    #host = "localhost"
    user = 'virginie'
    passwd = 'mysecretpassword'

    conn = psycopg2.connect(host=host, port=5432, user=user, password=passwd)
    conn.autocommit=True
    cursor = conn.cursor()
    return cursor

def create_db(cursor, db) : 
    query = "SELECT datname FROM pg_database"
    cursor.execute(query)
    all_db = cursor.fetchall()
    db_exist = False
    for elem in all_db : 
        print(elem[0])
        if elem[0] == db:
            db_exist = True
            print("DB already created")
    if db_exist == False : 
        query = "CREATE DATABASE " + db + ";"
        cursor.execute(query)

    query_table = "CREATE TABLE IF NOT EXISTS contact (id SERIAL PRIMARY KEY, name varchar(50), email varchar(50), phone varchar(50), message TEXT );"
    cursor.execute(query_table)

def test_table(cursor, db):
    query = "SELECT * FROM contact ;"
    cursor.execute(query)
    all_res = cursor.fetchall()

def remove_database(cursor, db):
    query = "DROP DATABASE " + db + ";"
    cursor.execute(query)
    query = "DROP TABLE contact ;"
    cursor.execute(query)

def insert_into_table(cursor, data):
    query = "INSERT INTO contact(name, email, phone, message) VALUES ("
    for elem in data : 
        query = query + "'" + str(elem) + "',"
    query = query[:-1] + ");"
    cursor.execute(query)

if __name__ == '__main__':
    #data = ['virginie', 'virginie@yopmail.com', '09*******', 'ohbvjhdbvjz::::']
    cursor = connexion_db()
    create_db(cursor, "app_v_r_d")
    # test_table(cursor, "app_v_r_d")
    # insert_into_table(cursor, data)
    # remove_database(cursor, "app_v_r_d")
