from flask import Flask, render_template
from your_task_5_script import fetch_student_records  # Import your Task 5 function

app = Flask(__name)

@app.route('/')
def index():
    student_records = fetch_student_records()  # Call your Task 5 function

    return render_template('index.html', student_records=student_records)

if __name__ == '__main__':
    app.run()


<!DOCTYPE html>
<html>
<head>
    <title>Student Details</title>
</head>
<body>
    <h1>Student Details</h1>
    <table>
        <tr>
            <th>Student ID</th>
            <th>Name</th>
            <th>Age</th>
            <th>Gender</th>
            <th>Course</th>
        </tr>
        {% for student in student_records %}
        <tr>
            <td>{{ student.student_id }}</td>
            <td>{{ student.name }}</td>
            <td>{{ student.age }}</td>
            <td>{{ student.gender }}</td>
            <td>{{ student.course }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>


server {
    listen 80;
    server_name your_server_domain_or_ip;

    location / {
        proxy_pass http://localhost:5000;  # Assuming your Flask app runs on port 5000
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /static {
        alias /path/to/your/static/files;  # If you have static files
    }
}
