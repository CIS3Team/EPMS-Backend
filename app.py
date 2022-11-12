from flask import Flask, render_template, url_for, request, redirect, session
import pymysql
import bcrypt

app = Flask(__name__)
# test connect mysql
conn = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='epms_db'
    )

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password'].encode('utf-8')

        with conn:
          with conn.cursor() as cursor:
              # Read a single record
                sql = "SELECT * FROM admins WHERE username=%s"
                cursor.execute(sql, (username))
                result = cursor.fetchone()
                
                if len(result) > 0:
                    print(result[2])
                    if bcrypt.hashpw(password, result[2].encode('utf-8')) == result[2].encode('utf-8'):
                        session['username'] = result[1]
                        return render_template("html/index.html")
                else:
                    return "Error Password"
    else:
        return render_template("html/login.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


# @app.route('/index')
# def login():
#     return 

# Example src
# เส้นทางหน้าแรก
# @app.route("/")
# def start():
#     with conn:
#         cursor = conn.cursor()
#         cursor.execute('SELECT fname, lname, phone FROM StudentDB.dbo.stu01_Tables;')
#         rows = cursor.fetchall()
#         return render_template("index.html", datas = rows)

# # เส้นทางหน้าเพิ่มข้อมูล
# @app.route("/adduser")
# def showadduser():
#     return render_template("adduser.html")

# #เส้นทางลบข้อมูล
# @app.route("/delete/<string:id_data>", methods=['GET'])
# def delete(id_data):
#     with conn:
#         cursor = conn.cursor()
#         cursor.execute('DELETE FROM StudentDB.dbo.stu01_Tables WHERE id = ?;', (id_data))
#         conn.commit()
#     return redirect(url_for('start'))

# # เส้นทางเพิ่มข้อมูลเข้าฐานข้อมูล
# @app.route("/insert", methods=['POST'])
# def insert():
#     if request.method == "POST":
#         fname = request.form['fname']
#         lname = request.form['lname']
#         phone = request.form['phone']
#         with conn.cursor() as cursor:
#             sql = "INSERT INTO StudentDB.dbo.stu01_Tables (fname, lname, phone) VALUES (?, ?, ?);"
#             cursor.execute(sql, (fname, lname, phone))
#             conn.commit()
#         return redirect(url_for('start'))

# #เส้นทางอัพเดตข้อมูล
# @app.route("/update", methods=['POST'])
# def update():
#     if request.method == "POST":
#         id_update = request.form['id']
#         fname = request.form['fname']
#         lname = request.form['lname']
#         phone = request.form['phone']
#         with conn.cursor() as cursor:
#             sql = "UPDATE StudentDB.dbo.stu01_Tables SET fname = ?, lname = ?, phone = ? WHERE id = ?"
#             cursor.execute(sql, (fname, lname, phone,id_update))
#             conn.commit()
#         return redirect(url_for('start'))


if __name__ == "__main__":
    app.secret_key = "123#!mnk)(%"
    app.run(debug=True)