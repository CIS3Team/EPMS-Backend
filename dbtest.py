import pymysql

conn = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='epms_db',
                             cursorclass=pymysql.cursors.DictCursor)

if conn:
    print("db connect")
else:
    print("error")

with conn:
   with conn.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM `test`"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)