import sqlite3
import re

class MyDatabase:
    def __init__(self):
        self.connection = self.create_connection()

    def create_connection(self):
        sqliteConnection = sqlite3.connect('./mydb.db', check_same_thread=False)
        cursor = sqliteConnection.cursor()
        print("Database created and Successfully Connected to mydb.db")

        sqlite_select_Query = "select sqlite_version();"
        cursor.execute(sqlite_select_Query)
        record = cursor.fetchall()
        print("SQLite Database Version is: ", record)
        cursor.close()

        return sqliteConnection

    def drop_table(self):
        sqlite_create_table_query = '''DROP TABLE IF EXISTS SqliteDb_developers'''
        cursor = self.connection.cursor()
        cursor.execute(sqlite_create_table_query)
        cursor.close()
        print("SQLite table Dropped")

    def create_table(self):
        sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS SqliteDb_developers (
                                        id INTEGER PRIMARY KEY,
                                        name TEXT NOT NULL,
                                        email text NOT NULL UNIQUE,
                                        joining_date datetime,
                                        salary REAL NOT NULL);'''

        cursor = self.connection.cursor()
        cursor.execute(sqlite_create_table_query)
        cursor.close()
        print("SQLite table created")

    def insert_Variable_Into_Table(self, id, name, email, joiningDate, salary, sqliteConnection=None):
        sqlite_insert = """INSERT INTO SqliteDb_developers
                                  (id, name, email, joining_date, salary) 
                                  VALUES (?, ?, ?, ?, ?);"""
        data_tuple = (id, name, email, joiningDate, salary)

        cursor = self.connection.cursor()
        cursor.execute(sqlite_insert, data_tuple)
        self.connection.commit()
        print("Python Variables inserted successfully into SqliteDb_developers table")
        cursor.close()

    def Select_Sqlite_Table(self):
        sqlite_select_query = """SELECT * from SqliteDb_developers"""
        cursor = self.connection.cursor()
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("\n")
        print("Total rows are: ", len(records))
        print("Printing each row")
        print("\n")

        return_dict = {}

        for row in records:
            print("Id: ", row[0])
            print("Name: ", row[1])
            print("Email: ", row[2])
            print("JoiningDate: ", row[3])
            print("Salary: ", row[4])
            print('\n')

            return_dict[row[0]] = {
                "Name": row[1],
                "Email": row[2],
                "JoiningDate": row[3],
                "Salary": row[4]
            }
        cursor.close()

        return return_dict

    def Select_Sqlite_Table_id(self, id):
        sqlite_select_query = f"""SELECT * from SqliteDb_developers WHERE id = {id}"""
        cursor = self.connection.cursor()
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("\n")
        print("Total rows are: ", len(records))
        print("Printing each row")
        print("\n")

        return_dict = {}

        for row in records:
            print("Id: ", row[0])
            print("Name: ", row[1])
            print("Email: ", row[2])
            print("JoiningDate: ", row[3])
            print("Salary: ", row[4])
            print('\n')

            return_dict[row[0]] = {
                "Name": row[1],
                "Email": row[2],
                "JoiningDate": row[3],
                "Salary": row[4]
            }
        cursor.close()
        return return_dict

    def update_sqlite_table(self ,id, name, email,joiningDate, salary):
        sql_update_query = f"""Update SqliteDb_developers set salary = {salary},name = '{name}',email = '{email}',joining_date = '{joiningDate}'  where id ={id} """
        print(f"Running following sql update query: \n {sql_update_query}")
        cursor = self.connection.cursor()
        cursor.execute(sql_update_query)
        print("Record Updated successfully ")
        self.connection.commit()
        cursor.close()

    def delete_record(self, id):
        sql_delete_query = f"""DELETE from SqliteDb_developers where id = {id} """
        print(f"Running following sql delete query: \n {sql_delete_query}")
        cursor = self.connection.cursor()
        cursor.execute(sql_delete_query)
        print("Record deleted successfully ")
        self.connection.commit()
        cursor.close()

    def validate_fields(self, id, name, email, joiningDate, salary):
        error_msg = ""
        raise_error = False
        if type(id) != int:
            raise_error = True
            error_msg = "ID can only be an INTEGER"
        if type(name) != str:
            raise_error = True
            error_msg = "NAME can only be a STRING"
        elif not re.fullmatch('[A-Za-z]{2,25}( [A-Za-z]{2,25})?', name):
            raise_error = True
            error_msg = "NAME can only have alphabet characters"
        if type(email) != str:
            raise_error = True
            error_msg = "Email can only be a STRING"
        elif not re.findall(
                r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$" ,
                email):
            raise_error = True
            error_msg = "Email is not VALID"
        if type(joiningDate) != str:
            raise_error = True
            error_msg = "Joining date can only be STRING"
        elif not re.findall(r"^[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}$", joiningDate):
            raise_error = True
            error_msg = "Joining Date IN_Valid. Allowed Format: YYYY-MM-DD"
        if type(salary) != int:
            raise_error = True
            error_msg = "Salary can only be a INTEGER "

        return raise_error, error_msg

if __name__=="__main__":
    pass

