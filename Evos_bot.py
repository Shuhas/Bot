import sqlite3

con = sqlite3.connect('Databaza.db', check_same_thread=False)
cur = con.cursor()


def create_table():
    cur.execute("""
        CREATE TABLE "user" ("user_id"	INTEGER,
        "user_name"	TEXT UNIQUE,
        "first_name"	TEXT,
        "number"	TEXT,
        "location"	TEXT,
        PRIMARY KEY("user_id")
        );
        """)
    con.commit()


def create_table_log():
    cur.execute("""
        CREATE TABLE "log" (
        "user_id"	INTEGER,
        "message"	TEXT,
        PRIMARY KEY("user_id")
        );
        """)
    con.commit()


def get_one(pk):
    cur.execute(f"select * from user where user_id={pk}")
    root = cur.fetchone()
    return root


def create_user(user_id, username):
    sql = f"insert into user (user_id, user_name) values ({user_id}, '{username}')"
    cur.execute(sql)
    con.commit()
    return get_one(user_id)


