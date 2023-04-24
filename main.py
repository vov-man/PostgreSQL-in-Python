import psycopg2

#-----------------------------------------------------создаем таблицу----------------------
def create_db(conn):
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS phone_user(
            id SERIAL PRIMARY KEY,
            email_user VARCHAR(40) UNIQUE NOT NULL,
            phone INTEGER)""")
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users(
            id SERIAL PRIMARY KEY,
            name TEXT (40) NOT NULL,
            subname TEXT (40) NOT NULL,
            email_user VARCHAR(40) UNIQUE NOT NULL)""")
        conn.commit()  

#-----------------------------------------------------наполняем таблицу----------------------
def add_client(conn, name, subname, email, phone=None):
    with conn.cursor() as cur:
        cur.execute("""INSERT INTO users(name) VALUES('Spaider') RETURNING id""")
        cur.execute("""INSERT INTO users(subname) VALUES('Man') RETURNING id""")
        cur.execute("""INSERT INTO users(email_esers) VALUES('SpaiderMan@netodology.ru') RETURNING id""")
        print(cur.fetchone())  

#-----------------------------------------------------добовляем телефон пользвателю----------
def add_phone(conn, users_id, phone_users):
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO phone_users(email_user, phone, users_id) VALUES(SpaiderMan@netodology.ru, '02', 1);
            """)
        conn.commit()  

#-----------------------------------------------------добовляем данные о клиенте-------------
def change_client(conn, user_id, name=None, subname=None, email_users=None, phones_users=None):
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO users(1, name, subname, email_users, phone) VALUES('Vladimir', 'Putin', 'superman@111111.ru', 1);
            """)
        conn.commit()  
        
#-----------------------------------------------------удалить телефон для существующего клиента------
def delete_phone(conn, users_id, phone_users):
    with conn.cursor() as cur:        
        cur.execute("""
            DELETE FROM phone WHERE id=%spaiderman;
            """, (1,))
        cur.execute("""
        SELECT * FROM phone_user;
        """)
        print(cur.fetchall())  

#--------------------------------------------------- удалить существующего клиента.--------------
def delete_client(conn, users_id):
    with conn.cursor() as cur:
        cur.execute("""
            DELETE FROM users WHERE id=%spaiderman;
            """, (1,))
        cur.execute("""
        SELECT * FROM users;
        """)
        print(cur.fetchall())  

#---------------------------------------------------найти клиента по его данным: имени, фамилии, email или телефону
def find_client(conn, name=None, subname=None, email_user=None, phone_user=None):
    with conn.cursor() as cur:
        cur.execute("""
        SELECT id FROM users WHERE name=%s, subname=%s, emai_user=%s;
        """, ("Man", "Spaider", "SpaiderMan@netodology.ru" ))  
        cur.execute("""
        SELECT id FROM phone_users WHERE phone=%s;
        """, ("02" ))  
        print(cur.fetchone())


conn.close()
