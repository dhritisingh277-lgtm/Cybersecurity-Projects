from flask import Flask, render_template_string, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "secretkey"

users = {}

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        hashed_password = generate_password_hash(password)

        users[username] = hashed_password

        return redirect('/login')

    return render_template_string('''
    <h2>Register</h2>

    <form method="POST">
        <input type="text" name="username" placeholder="Username" required><br><br>

        <input type="password" name="password" placeholder="Password" required><br><br>

        <button type="submit">Register</button>
    </form>
    ''')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        if username in users and check_password_hash(users[username], password):

            session['user'] = username

            return redirect('/dashboard')

        return "Invalid Username or Password"

    return render_template_string('''
    <h2>Login</h2>

    <form method="POST">
        <input type="text" name="username" placeholder="Username" required><br><br>

        <input type="password" name="password" placeholder="Password" required><br><br>

        <button type="submit">Login</button>
    </form>
    ''')

@app.route('/dashboard')
def dashboard():

    if 'user' in session:

        return f"""
        <h1>Welcome {session['user']} 😄</h1>

        <a href='/logout'>Logout</a>
        """

    return redirect('/login')

@app.route('/logout')
def logout():

    session.pop('user', None)

    return redirect('/login')

app.run(debug=True)
