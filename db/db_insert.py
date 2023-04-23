#Connecting to the SQL server:
import pymysql

conn = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'polandamir',
    db = 'semanki',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor

)

#we use a try finally block to make sure the 
#db is closed.

try: 
    with conn.cursor() as cursor:
        #Create a new record
        sql = "INSERT INTO cards (front_text,back_text) VALUES ({},{}) "
        cursor.execute(sql,('Who is the POTUS?','Joe Biden'))
    
    conn.commit()    

    print("Record inserted successfuly")
finally:
    conn.close()