from flask import Flask, render_template, request, redirect, url_for
from app.database import init_db
from app.violation_service import add_violation_record, delete_record, get_all_violations

app = Flask(__name__, template_folder="../templates", static_folder="../static")

# Initialize database
init_db()

@app.route('/')
def violations():
    violations = get_all_violations()
    return render_template('violations.html', violations=violations)

@app.route('/add', methods=['POST'])
def add_violation():
    add_violation_record(request.form)
    return redirect(url_for('violations'))

@app.route('/delete/<int:id>')
def delete_violation(id):
    delete_record(id)
    return redirect(url_for('violations'))

if __name__ == '__main__':
    app.run(debug=True)