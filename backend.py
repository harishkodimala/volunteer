from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

volunteers = []
elderly_requests = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/volunteer.html')
def volunteer_page():
    return render_template('volunteer.html')

@app.route('/elderly.html')
def elderly_page():
    return render_template('elderly.html')

@app.route('/register_volunteer', methods=['POST'])
def register_volunteer():
    data = request.form
    volunteer = {
        'name': data['name'],
        'email': data['email'],
        'phone': data['phone'],
        'availability': data['availability']
    }
   
    return jsonify({'message': 'Volunteer registered successfully!'})
    
@app.route('/request_ride', methods=['POST'])
def request_ride():
    data = request.form
    request_data = {
        'name': data['name'],
        'phone': data['phone'],
        'pickup': data['pickup'],
        'destination': data['destination'],
        'date': data['date'],
        'time': data['time']
    }
    elderly_requests.append(request_data)
    print("Ride Requested:", request_data)
    return jsonify({'message': 'Ride requested successfully!'})

if __name__ == '__main__':
    app.run(debug=True)