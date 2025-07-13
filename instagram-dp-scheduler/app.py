from flask import Flask, request, render_template, redirect
import os, json

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create uploads folder if not exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    if os.path.exists('schedule.json'):
        with open('schedule.json', 'r') as f:
            try:
                schedules = json.load(f)
                if not isinstance(schedules, list):
                    schedules = [schedules]
            except:
                schedules = []
    else:
        schedules = []

    return render_template('index.html', history=schedules)


@app.route('/upload', methods=['POST'])
def upload():
    username = request.form['username']
    password = request.form['password']
    schedule_time = request.form['time']
    image = request.files['dp_image']
    filename = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
    image.save(filename)

    # Save schedule info to a JSON file
    schedule_data = {
        'username': username,
        'password': password,
        'image_path': filename,
        'time': schedule_time
    }

    with open('schedule.json', 'w') as f:
        json.dump(schedule_data, f)

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
