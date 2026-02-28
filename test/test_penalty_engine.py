import sys
import os
import pytest
import sqlite3

# Add parent directory (svms-subsystem) to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import your modules
from app.penalty_engine import calculate_penalty
from app.database import init_db, get_db_connection
from app.violation_service import add_violation_record, get_all_violations, delete_record
from app.app import app as flask_app

# ------------------------
# Penalty Engine Tests
# ------------------------
def test_dresscode_penalties():
    assert calculate_penalty("Dresscode", 1) == "Memorize Mission-Vision"
    assert calculate_penalty("Dresscode", 2) == "Community Service"
    assert calculate_penalty("Dresscode", 3) == "Suspension"
    assert calculate_penalty("Dresscode", 5) == "Suspension"  # above max

def test_no_motor_sticker_penalties():
    assert calculate_penalty("No Motor Sticker", 1) == "Warning"
    assert calculate_penalty("No Motor Sticker", 2) == "Parent Conference"
    assert calculate_penalty("No Motor Sticker", 3) == "Suspension"
    assert calculate_penalty("No Motor Sticker", 10) == "Suspension"

def test_unknown_violation():
    assert calculate_penalty("Random Violation", 1) == "Warning"


# ------------------------
# Database Tests
# ------------------------
def test_db_creation():
    init_db()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='violations'")
    table = cursor.fetchone()
    conn.close()
    assert table is not None


# ------------------------
# Violation Service Tests
# ------------------------
@pytest.fixture
def setup_db():
    # Initialize fresh DB before tests
    init_db()
    yield
    # Clean up after tests
    conn = get_db_connection()
    conn.execute("DELETE FROM violations")
    conn.commit()
    conn.close()

def test_add_violation(setup_db):
    form_data = {
        "student": "John Doe",
        "course": "BSCS",
        "year": "3",
        "violation_type": "Dresscode",
        "status": "Pending",
        "officer": "Admin"
    }
    add_violation_record(form_data)
    violations = get_all_violations()
    assert len(violations) >= 1
    assert violations[0]["student"] == "John Doe"

def test_delete_violation(setup_db):
    # Add record first
    form_data = {
        "student": "Delete Me",
        "course": "BSCS",
        "year": "2",
        "violation_type": "Late Submission",
        "status": "Pending",
        "officer": "Admin"
    }
    add_violation_record(form_data)
    violations = get_all_violations()
    delete_record(violations[0]["id"])
    violations_after = get_all_violations()
    assert all(v["student"] != "Delete Me" for v in violations_after)


# ------------------------
# Flask App Tests
# ------------------------
@pytest.fixture
def client():
    flask_app.config["TESTING"] = True
    with flask_app.test_client() as client:
        yield client

def test_home_page(client, setup_db):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Violation Management" in response.data

def test_add_page(client, setup_db):
    response = client.post("/add", data={
        "student": "Jane Doe",
        "course": "BSCS",
        "year": "3",
        "violation_type": "Late Submission",
        "status": "Pending",
        "officer": "Admin"
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Jane Doe" in response.data