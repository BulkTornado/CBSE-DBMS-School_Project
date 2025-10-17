import mysql.connector as _mysql
import sys


class ConnectToMySQL:
    def __init__(self, host: str, user: str, passwd: str, database: str, dev_mode: bool) -> None:
        self.host = host
        self.user = user
        self.passwd = passwd
        self.database = database

        self.dev_mode = dev_mode

        self.default_query = "SELECT school_id as 'School ID', school_name as 'School Name' FROM schools_data;"

    def connect_to_database(self) -> None:
        try:
            self.database_connection =_mysql.connect(host=self.host, database=self.database, user=self.user, passwd=self.passwd)
        except Exception as error:
            print("Database connection failed. Refer to following error report for more:\n")

            self.show_exception_traceback(error)

            print("\nTerminating script early.")
            sys.exit()

    def create_cursor_object(self) -> None:
        self.cursor_object = self.database_connection.cursor()

    def execute_sql_query(self, sql_query: str) -> None:
        try:
            if self.dev_mode:
                print(f"[DEV MODE] Executing SQL Query: \n{sql_query}\n")
            self.cursor_object.execute(sql_query)
        except Exception as error:
            self.show_exception_traceback(error)
            self.close_connection()

    def close_connection(self) -> None:
        self.database_connection.close()
        print("\nConnection successfully closed!")

    def show_exception_traceback(self, e: Exception) -> None:
        if self.dev_mode:
            print("[DEV MODE] Showing full exception traceback:\n")
            print(repr(e))
        else:
            print(e)

        return

    def __str__(self) -> str:
        return ""

    def __repr__(self) -> str:
        return ""

    def __exit__(self) -> None:
        return

if __name__ == "__main__":
    print("You are not supposed to run this program by itself.")
    sys.exit()
