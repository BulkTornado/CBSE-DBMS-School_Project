"""
Python program to access MySQL database.
"""

from functional_modules import ConnectToMySQL
import mysql.connector as _mysql
from tabulate import tabulate
import argparse
import atexit
import sys


def str_to_bool(v: str) -> bool:
    true_opt = ("yes", "y", "true", "t", "1")
    false_opt = ("no", "n", "false", "f", "0")

    if v.lower() in true_opt:
        return True
    elif v.lower() in false_opt:
        return False
    else:
        raise argparse.ArgumentTypeError(
            f"Boolean value excepted, evaluated from following option set: True = {true_opt}, False = {false_opt}"
        )


parser = argparse.ArgumentParser(description="Python script to run SQL queries.")

parser.add_argument(
    "-d",
    "--dev",
    type=str_to_bool,
    default=False,
    help="Run in developer mode for detailed errors.",
)

args = parser.parse_args()


host = "localhost"
user = "root"
passwd = "tks@123?"
database = "example_cbse_database"
default_query = (
    "SELECT school_id as 'School ID', school_name as 'School Name' FROM schools_data;"
)
developer_mode = args.dev

connection_object = ConnectToMySQL(host, user, passwd, database, developer_mode)


def show_error(e: Exception):
    if developer_mode:
        print("[DEV MODE] Showing full exception trace:\n")
        print(repr(e))
    else:
        print(e)


try:
    database_connection = _mysql.connect(
        host=host, database=database, user=user, passwd=passwd
    )
except Exception as error:
    print("Database connection failed. Refer to following error report for more:\n")

    show_error(error)

    print("\nTerminating script early.")
    sys.exit()


@atexit.register
def close_database_connection():
    if "database_connection" in globals() and database_connection.is_connected():
        database_connection.close()
        print("\nConnections successfully closed!")


def display_menu():
    print(f"{'| CBSE Database |':=^80}\n")


def get_sql_query() -> str:
    multi_line_sql_query = []
    line_count = 1

    print("Enter SQL query(end final line with ';' to complete the query):\n")
    while True:
        single_line_query = input(f"{line_count}. ").strip()

        # Skip adding to list if user presses ENTER key
        if single_line_query == "":
            print("Refrain from pressing ENTER key without writing a query.")
            continue

        multi_line_sql_query.append(single_line_query)
        line_count += 1

        if single_line_query.endswith(";"):
            break

    final_query = " ".join(multi_line_sql_query)

    if final_query == ";":
        print(f"\nNo query specified. Using the defualt query:\n{default_query}\n")
        return default_query

    print(f"\nFinal query: {final_query}\n")
    return final_query


def main() -> None:
    display_menu()

    cursor = database_connection.cursor()

    sql_query = get_sql_query()

    try:
        if developer_mode:
            print(f"[DEV MODE] Executing SQL Query:\n{sql_query}\n")
        cursor.execute(sql_query)
    # '_mysql' refers to _mysql.connector
    # _mysql.errors.ProgrammingError
    except Exception as error:
        show_error(error)
        return

    if cursor.description is None:
        print("Query executed successfully (no result set)")

        # cursor.execute("COMMIT;")
        print("COMMIT successful.")
        return

    data = cursor.fetchall()

    # DEBUG: DO NOT REMOVE
    # print(type(data))
    # print(data)
    # print(repr(data))

    # Fetch column names from cursor
    columns = [desc[0] for desc in cursor.description]

    # Pretty print results in a table format
    # OPTS : "simple", "grid"
    print(tabulate(data, headers=columns, tablefmt="simple"))

    print(f"\nRows retrieved: {cursor.rowcount}")


if __name__ == "__main__":
    main()
