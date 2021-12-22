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
        "user_id"	INTEGER UNIQUE,
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


def create_user_log(user_id):
    s = "{\'state\': 0}"
    sql = f"""insert into log (user_id, message) values ({user_id}, "{s}")"""
    cur.execute(sql)
    con.commit()


def get_user_log(user_id):
    cur.execute(f"select message from log where user_id={user_id}")
    return cur.fetchone()


def change_log(user_id, message):
    sql = f'update log set message = "{message}" where user_id = {user_id}'
    cur.execute(sql)
    con.commit()
    return get_user_log(user_id)
