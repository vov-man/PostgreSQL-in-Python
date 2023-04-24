import psycopg2

#-----------------------------------------------------создаем таблицу----------------------
def create_db(conn):
    conn.cursor() as cur:
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phone_user(
            id SERIAL PRIMARY KEY,
            email_user VARCHAR(40) UNIQUE NOT NULL,
        phone_user INTEGER)""")
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id SERIAL PRIMARY KEY,
            name TEXT (40) NOT NULL,
            subname TEXT (40) NOT NULL,
            email_user VARCHAR(40) UNIQUE NOT NULL)""")
    conn.commit()  # фиксируем в БД        
    print(f'[INFO] Table created successfully')


#-----------------------------------------------------наполняем таблицу----------------------
def add_client(conn, name, subname, email, phones=None):
    with conn.cursor() as cur:
        cur.execute("""
        INSERT INTO users(name) VALUES('Spaider') RETURNING id;
        """)
        conn.cursor() as cur:
        cur.execute("""
        INSERT INTO users(subname) VALUES('Man') RETURNING id;
        """)
        conn.cursor() as cur:
        cur.execute("""
        INSERT INTO users(email_esers) VALUES('SpaiderMan@netodology.ru') RETURNING id;
        """)
        print(cur.fetchone())  # запрос данных автоматически зафиксирует изменения


#-----------------------------------------------------добовляем телефон пользвателю----------
with psycopg2.connect(database="netology_db", user="postgres", password="postgres") as conn:
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO phone_users(email_user, phone, users_id) VALUES(SpaiderMan@netodology.ru, '02', 1);
            """)
        conn.commit()  # фиксируем в БД


#-----------------------------------------------------добовляем данные о клиенте-------------
with psycopg2.connect(database="netology_db", user="postgres", password="postgres") as conn:
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO users(name, subname, email_users, users_id) VALUES('Vladimir', 'Putin', 'superman@111111.ru', 1);
            """)
        conn.commit()  # фиксируем в БД        
#-----------------------------------------------------удалить телефон для существующего клиента------
with psycopg2.connect(database="netology_db", user="postgres", password="postgres") as conn:
    with conn.cursor() as cur:        
        cur.execute("""
            DELETE FROM phone_user WHERE id=%spaiderman;
            """, (1,))
        cur.execute("""
        SELECT * FROM phone_user;
        """)
        print(cur.fetchall())  # запрос данных автоматически зафиксирует изменения
#--------------------------------------------------- удалить существующего клиента.--------------
with psycopg2.connect(database="netology_db", user="postgres", password="postgres") as conn:
    with conn.cursor() as cur:
        cur.execute("""
            DELETE FROM user WHERE id=%spaiderman;
            """, (1,))
        cur.execute("""
        SELECT * FROM user;
        """)
        print(cur.fetchall())  # запрос данных автоматически зафиксирует изменения
#---------------------------------------------------найти клиента по его данным: имени, фамилии, email или телефону
with psycopg2.connect(database="netology_db", user="postgres", password="postgres") as conn:
    with conn.cursor() as cur:
        cur.execute("""DELETE FROM users WHERE id=%s;""", (1,))
        cur.execute("""SELECT * FROM users""")
        print(cur.fetchall())  # запрос данных автоматически зафиксирует изменения
  