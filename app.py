from flask import Flask, render_template, request, redirect, flash,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Set up the database (SQLite for simplicity in this case)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///volunteers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'  # For flash messages
db = SQLAlchemy(app)

# Define a model for Volunteers
class Volunteer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(20), nullable=False)
    availability = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Volunteer {self.name}>'

# Route to display the volunteers
@app.route('/')
def index():
    # Query the database to get all volunteers
    volunteers = Volunteer.query.all()
    return render_template('index.html', volunteers=volunteers)

# Route to register a new volunteer
@app.route('/success')
def success():
    return render_template('success.html') 
@app.route('/rules')
def rules():
    return render_template('rules.html')
@app.route('/ridesuccess')
def ridesuccess():
    return render_template('ridesuccess.html') 

@app.route('/elderly')
def elderly():
    return render_template('elderly.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        contact = request.form['contact']
        availability = request.form['availability']

        new_volunteer = Volunteer(name=name, contact=contact, availability=availability)

        db.session.add(new_volunteer)
        db.session.commit()  # Save the new volunteer to the database

        flash("Registered Successfully!")  # Flash success message
        return redirect(url_for('success'))   # Redirect to the home page (to see the updated list)
    
    return render_template('register.html')  # Render the registration form

if __name__ == '__main__':
    # Create the database if it doesn't exist
    with app.app_context():
        db.create_all()  # This creates the database and tables
    app.run(debug=True)
