import sqlite3
from Client import Client
from settings import DB_SQL_STRUCTURE, DB_NAME


conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()


def create_clients_table():
    with open(DB_SQL_STRUCTURE, "r") as f:
        conn.executescript(f.read())
        conn.commit()


def change_message(new_message, logged_user):
    update_sql = "UPDATE clients SET message = '%s' WHERE id = '%s'" % (new_message, logged_user.get_id())
    cursor.execute(update_sql)
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    update_sql = "UPDATE clients SET password = '%s' WHERE id = '%s'" % (new_pass, logged_user.get_id())
    cursor.execute(update_sql)
    conn.commit()


def register(username, password):
    insert_sql = "insert into clients (username, password) values ('%s', '%s')" % (username, password)
    cursor.execute(insert_sql)
    conn.commit()


def login(username, password):
    select_query = "SELECT id, username, balance, message FROM clients WHERE username = '%s' AND password = '%s' LIMIT 1" % (username, password)

    cursor.execute(select_query)
    user = cursor.fetchone()

    if(user):
        return Client(user[0], user[1], user[2], user[3])
    else:
        return False
