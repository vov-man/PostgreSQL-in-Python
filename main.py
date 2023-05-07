import  psycopg2
from config import host, user, password, bd_name

def create_db(conn):
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS username (
                id SERIAL PRIMARY KEY,
                name VARCHAR(25) UNIQUE,
                surname varchar(25) NOT NULL,
                email varchar(30) NOT NULL
            );""")
        cur.execute("""
            CREATE TABLE IF NOT EXISTS phone (
                id SERIAL PRIMARY KEY,
                phon INTEGER,
                fk_phone INTEGER NOT NULL REFERENCES username(id)
            );""")
    conn.commit()    
    return cur.fetchone()[0]

def add_client(conn, name, subname, email, phon=None):
    with conn.cursor() as cur:
        cur.execute(f"INSERT INTO username (name, surname, email) VALUES ('{first_name}', '{last_name}', '{email}') RETURNING id;")
        cur.execute(f"INSERT INTO phone (phon) VALUES('{phones}');")
    conn.commit()
    return cur.fetchone()[0]  


with psycopg2.connect(host=host, database=bd_name, user=user, password=password)  as conn:
    #print('Возможные команды: 1, 2, 3, 4, 5, 6, 7')
    comand = input('Введите название команды ')
 
    if comand == '1':
        create_db(conn)
    
    elif comand == '2':
        first_name = input("Введите имя: ")
        last_name = input("Введите фамилию: ")
        email = input("Введите email: ")
        phones = input("Введите номер телефона: ")
        add_client(conn, first_name, last_name, email, phones)
    
    elif comand == '3':
        add_phone()
            
    elif comand == '4':
        change_client()

    elif comand == '5':
        delete_phone()

    elif comand == '6':
        delete_client()

    elif comand == '7':
        print(find_client())


    
        

conn.close()
