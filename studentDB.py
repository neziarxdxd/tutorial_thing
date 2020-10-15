import mysql.connector as connectSQL
mySQL = connectSQL.connect(
    host = "localhost",
    user= "root",
    password= "",
    database = "db_school")
myCursor= mySQL.cursor()
myCursor.execute("SHOW TABLES")
