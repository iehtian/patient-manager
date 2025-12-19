import psycopg2

def get_db_connection():
    return  psycopg2.connect(
    host="localhost",
    user="patient_user",
    password="iehtian",
    database="patient",
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

def select_medical_records_by_patient_id(patient_id):
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        query = "SELECT * FROM medical_records WHERE patient_id = %s"
        cur.execute(query, (patient_id,))
        results = cur.fetchall()
    finally:
        cur.close()
        conn.close()
    return results

def add_patient(patient_name, birth_date, gender):
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        query = "INSERT INTO patients (patient_name, birth_date, gender) VALUES (%s, %s, %s)"
        cur.execute(query, (patient_name, birth_date, gender))
        conn.commit()
    finally:
        cur.close()
        conn.close()

def add_medical_record(patient_id, record_date, description):
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        query = "INSERT INTO medical_records (patient_id, record_date, description) VALUES (%s, %s, %s)"
        cur.execute(query, (patient_id, record_date, description))
        conn.commit()
    finally:
        cur.close()
        conn.close()

def main():
    patients = select_patients_by_name("张三")
    for patient in patients:
        print(patient)

if __name__ == "__main__":
    main()
