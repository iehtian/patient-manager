import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="painter_user",
    password="painter_pass",
    database="painter",
    port="3307"
)

def get_db_connection():
    return  mysql.connector.connect(
    host="localhost",
    user="painter_user",
    password="painter_pass",
    database="painter",
    port="3307"
    )

def select_all_painters():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM painters")
    results = cursor.fetchall()
    cursor.close()
    return results

def main():
    painters = select_all_painters()
    for painter in painters:
        print(painter)

if __name__ == "__main__":
    main()

print("数据库连接成功!")