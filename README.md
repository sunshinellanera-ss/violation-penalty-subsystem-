# Student Violation Management System (SVMS) – Violation Logging Subsystem

## Project Overview
The **Student Violation Management System (SVMS)** is a centralized platform designed to automate the recording, monitoring, and analysis of student behavioral violations. This subsystem focuses specifically on **violation logging and penalty computation**, replacing manual Excel-based tracking and reducing human error.

The subsystem automatically counts repeat offenses, assigns penalties according to predefined rules, and prevents duplicate violation entries, making disciplinary management **accurate, consistent, and efficient**.

---

## Objectives
- Maintain a centralized and secure record of student violations.  
- Automatically classify violations and compute penalties based on rules.  
- Prevent duplicate entries for the same violation and student.  
- Provide easy-to-use interfaces for adding, viewing, and deleting violations.  
- Enable testing of penalty computation logic using PyTest.

---

## Subsystem Description
**Violation Logging Subsystem**:  
Handles all aspects of violation management, including:  
- Recording student violation details   
- Counting repeat offenses automatically  
- Applying sanctions based on predefined rules  
- Managing current violation records

**Modules:**  
1. **Add Violation Module** – Add new violations through a form.  
2. **Violation Records Module** – List all violations with search, view, and delete functionality.  
3. **Penalty Computation Module** – Calculates penalties using the rules defined in `penalty_engine.py`.  

---

## Implemented Features
- Secure and centralized student violation database (`SQLite`).  
- Automatic penalty calculation based on offense count and violation type.  
- Duplicate violation prevention.  
- Web interface with a responsive design (HTML, CSS, JavaScript).  
- Modal popup for adding new violations and viewing.  
- Search feature for violations (currently non-functional / under development)
- PyTest integration for testing penalty engine logic.  

---

## System Architecture
- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Python Flask for handling routes and business logic  
- **Database:** SQLite  
- **Business Logic:** `violation_service.py` and `penalty_engine.py`  
- **Testing Framework:** PyTest  

**Flow:**  
User (Browser)
↓
Flask Routes (app.py)
↓
Violation Service (violation_service.py)
↓
Penalty Engine (penalty_engine.py)
↓
SQLite Database (database.db)

---

## Project Structure
svms-subsystem/
├── app/
│ ├── _init_.py
│ ├── app.py 
│ ├── database.py 
│ ├── violation_service.py 
│ └── penalty_engine.py
├── static/
│ ├── style.css 
│ └── script.js 
├── templates/
│ └── violations.html 
├── test/
│ └── test_svms_subsystem.py 
├── .gitignore
└── README.md

---

## Technologies Used
- **Python 3.10.7** – Backend logic  
- **Flask** – Web framework  
- **SQLite** – Database for storing violations  
- **HTML, CSS, JavaScript** – Frontend UI  
- **PyTest 9.0.2** – Testing framework  

---

## Development Environment
- **OS:** Windows 10  
- **IDE:** Visual Studio Code  
- **Git:** Version control and repository management  

---

## How to Run the Subsystem

1. Open terminal inside the project folder .

2. Install Flask (if not installed):
   pip install flask

3. Run the application:
   python -m app.app

4. Open browser:
   http://....

## Testing

Run:
pytest
output:
collected  items
tests/test_svms_subsystem.py ........ [100%]
8 passed in 0.42s

Component / File	         Status
penalty_engine.py	         ✅ Passed
database.py	               ✅ Passed
violation_service.py	      ✅ Passed
Flask App Routes (app.app)	✅ Passed

All core components, including penalty calculation, database operations, violation service, and web routes, are working correctly.

## Development Workflow

Version Control: Git with feature branches and meaningful commit messages.

TDD: Write tests → Implement logic → Re-run tests to ensure passing.

Incremental Integration: Add modules one by one, verify functionality, and merge.


## Git workflow evidence for report

- Repository initialized: git init
- Remote added: git remote add origin <https://github.com/sunshinellanera-ss/violation-penalty-subsystem-.git>
- Feature branch created: git checkout -b feature/violation-logging
- Files staged: git add .
- Commit made: git commit -m "Add penalty engine module"
- Branch pushed to GitHub: git push -u origin feature/violation-logging




