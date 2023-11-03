import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="gh0rhe1rf",
    # auth_plugin="gh0rhe1rf"
)

my_cursor = mydb.cursor()
my_cursor.execute("CRETE DATABASE our_users")
my_cursor.execute("SHOW DATABASES")

for db in my_cursor:
    print(db)
