import psycopg2

def get_db_connection():
    return  psycopg2.connect(
    host="localhost",
    user="painter_user",
    password="iehtian",
    database="painter",
    port="5433"
    )

def select_all_patients():
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM patients")
        results = cur.fetchall()
    finally:
        cur.close()
        conn.close()
    return results

def select_patients_by_name(name):
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        query = "SELECT * FROM patients  WHERE patient_name ILIKE %s"
        cur.execute(query, (f"%{name}%",))
        results = cur.fetchall()
    finally:
        cur.close()
        conn.close()
    return results

def main():
    patients = select_patients_by_name("张三")
    for patient in patients:
        print(patient)

if __name__ == "__main__":
    main()
