import sqlite3


def create_connection():
    sqliteConnection = sqlite3.connect('./mydb.db')
    cursor = sqliteConnection.cursor()
    print("Database created and Successfully Connected to mydb.db")

    sqlite_select_Query = "select sqlite_version();"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    print("SQLite Database Version is: ", record)
    cursor.close()

    return sqliteConnection

def create_table(cursor):
    sqlite_create_table_query = '''CREATE TABLE SqliteDb_developers (
                                    id INTEGER PRIMARY KEY,
                                    name TEXT NOT NULL,
                                    email text NOT NULL UNIQUE,
                                    joining_date datetime,
                                    salary REAL NOT NULL);'''

    print("Successfully Connected to mydb")
    cursor.execute(sqlite_create_table_query)
    print("SQLite table created")


def insert_Variable_Into_Table(cursor, id, name, email, joiningDate, salary):
    sqlite_insert = """INSERT INTO SqliteDb_developers
                          (id, name, email, joining_date, salary) 
                          VALUES (?, ?, ?, ?, ?);"""

    data_tuple = (id, name, email, joiningDate, salary)
    cursor.execute(sqlite_insert , data_tuple)
    sqliteConnection.commit()
    print("Python Variables inserted successfully into SqliteDb_developers table")


def Select_Sqlite_Table():
    sqlite_select_query = """SELECT * from SqliteDb_developers"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    print("\n")
    print("Total rows are: ", len(records))
    print("Printing each row")
    print("\n")

    for row in records:
        print("Id: ", row[0])
        print("Name: ", row[1])
        print("Email: ", row[2])
        print("JoiningDate: ", row[3])
        print("Salary: ", row[4])
        print('\n')


def update_sqlite_table():
    sql_update_query = """Update SqliteDb_developers set salary = 1000 where id = 2"""
    cursor.execute(sql_update_query)
    print("Record Updated successfully ")


def delete_record():
    sql_delete_query = """DELETE from SqliteDb_developers where id = 2"""
    cursor.execute(sql_delete_query)
    sqliteConnection.commit()
    print("Record deleted successfully ")


if __name__=="__main__":
    try:

        sqliteConnection = create_connection()
        cursor = sqliteConnection.cursor()

        # create_table(cursor)

        # insert_Variable_Into_Table(cursor, 1, "Ahmer", 'ahmer@gamil.com', '2019-05-19', 9000)
        # insert_Variable_Into_Table(cursor, 2, "Abdullah", 'abdullah@gmail.com', '2019-02-23', 9500)

        Select_Sqlite_Table()

        update_sqlite_table()
        delete_record()
    except sqlite3.Error as error:
        print(error)

    finally:
        if sqliteConnection:
            cursor.close()
            sqliteConnection.commit()
            sqliteConnection.close()
            print("The SQLite connection is closed")

