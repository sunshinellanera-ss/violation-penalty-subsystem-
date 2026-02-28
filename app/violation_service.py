from .database import get_db_connection
from .penalty_engine import calculate_penalty

def add_violation_record(form_data):
    student = form_data['student'].strip()
    course = form_data['course']
    year = form_data['year']
    violation_type = form_data['violation_type']
    status = form_data['status']
    officer = form_data['officer']

    conn = get_db_connection()

    previous_count = conn.execute(
        "SELECT COUNT(*) FROM violations WHERE student=? AND violation_type=?",
        (student, violation_type)
    ).fetchone()[0]

    offense_count = previous_count + 1
    penalty = calculate_penalty(violation_type, offense_count)

    conn.execute(
        "INSERT INTO violations (student, course, year, violation_type, offense_count, penalty, status, officer) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (student, course, year, violation_type, offense_count, penalty, status, officer)
    )
    conn.commit()
    conn.close()

def get_all_violations():
    conn = get_db_connection()
    violations = conn.execute("SELECT * FROM violations ORDER BY id DESC").fetchall()
    conn.close()
    return violations

def delete_record(record_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM violations WHERE id=?", (record_id,))
    conn.commit()
    conn.close()