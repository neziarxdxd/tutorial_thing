import mysql.connector as connectSQL
mySQL = connectSQL.connect(
    host = "localhost",
    user= "root",
    password= "",
    database = "db_school")
myCursor= mySQL.cursor()
sql = '''INSERT INTO tbl_student (first_name, last_name,section) 
        VALUES (%s, %s,%s)'''
values = ("Juan","Dela Cruz","C301")
myCursor.execute(sql, values)
mySQL.commit()
print(myCursor.rowcount)