from fastapi import FastAPI, status, HTTPException
from db_task import MyDatabase


app = FastAPI(title="Shehryar ki App",)
database = MyDatabase()

@app.get("/Select_Table")
def select_table():
    response = database.Select_Sqlite_Table()
    return response


@app.post("/Insert_Table", status_code=status.HTTP_201_CREATED)
def insert_Variable_Into_Table(id:int, name:str, email:str, joiningDate:str, salary:int):
  return database.insert_Variable_Into_Table(id, name, email, joiningDate, salary)



@app.post("/Insert_Multiple_Record_Table")
def insert_multiple_records_table(list_of_records: list):
    for record in list_of_records:
        if type(record) != list:
            raise_error = True
            error_msg = "Record can only accept List's"
            break

        print("Inserting: {}".format(record))
        id, name, email, joiningDate, salary = record
        raise_error, error_msg = database.validate_fields(id, name, email, joiningDate, salary)
        if raise_error:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                detail=error_msg)
        database.insert_Variable_Into_Table(id, name, email, joiningDate, salary)


@app.get("/Select_Table/{id}")
def select_table_id(id: int):
    return database.Select_Sqlite_Table_id(id)


@app.put("/Update_Table/")
def update_table(id: int, name: str, email: str, joiningDate: str, salary: int):
    return database.update_sqlite_table(id, name, email, joiningDate, salary)


@app.put("/Update_Multiple_Table")
def update_multiple_table(list_of_records: list):
    for record in list_of_records:
        if type(record) != list:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Record can only accept List's.")
        print("Updating: {}".format(record))
        id , name, email, joiningDate, salary = record
        raise_error, error_msg = database.validate_fields(id, name, email, joiningDate, salary)
        if raise_error:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                detail=error_msg)
        database.update_sqlite_table(id, name, email, joiningDate, salary)


@app.delete("/Delete_Record/")
def delete_record(id: int):
    return database.delete_record(id)


@app.delete("/Delete_Multiple_Record/")
def delete_multiple_record(list_of_ids: list):
    for id in list_of_ids:
        if type(id) != int:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                detail="Can only accept ID's as INTEGER.")
        print("Deleting: {}".format(id))
        database.delete_record(id)


@app.get("/Select_Table")
def select_table():
    database.Select_Sqlite_Table()
    return "read todo list"
