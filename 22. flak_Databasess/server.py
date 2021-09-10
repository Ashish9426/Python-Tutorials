from flask import Flask, jsonify, render_template, request
from mydatabase import Database

# create a server
app = Flask(__name__)

# used for performing all the db queries
db = Database()

# server url
server_url = "http://localhost:4000/"


@app.route('/', methods=['GET'])
def get_root():
    # get the file named index.html from templates directory
    return render_template('index.html')


@app.route('/signin', methods=['GET'])
def get_signin():
    return render_template("signin.html")


@app.route('/signin', methods=['POST'])
def post_signin():
    email = request.form.get('email')
    password = request.form.get('password')

    query = f"select firstName, lastName from user where email = '{email}' and password = '{password}';"
    result = db.select_query(query)
    if len(result) == 0:
        # user does not exist
        print("USER NOT EXIST")
        return render_template("signin.html")
    else:
        # result is a list of tuples
        user_info = result[0]

        # create user name dynamically
        name = user_info[0] + ' ' + user_info[1]
        print(f"name = {name}")

        # user does exist
        return render_template("home.html", username=name)


@app.route('/signup', methods=['GET'])
def get_signup():
    return render_template("signup.html")


@app.route('/signup', methods=['POST'])
def post_signup():
    # used when the data is received using query string parameters
    # print(f"args = {request.args}")

    # used when the data is received using form tag
    # print(f"form = {request.form}")

    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    password = request.form.get('password')

    query = f"insert into user (firstName, lastName, email, password) values ('{first_name}', '{last_name}', '{email}', '{password}')"
    db.execute_query(query)

    return render_template("signin.html")


@app.route('/home', methods=['GET'])
def get_home():
    return render_template("home.html")


@app.route('/chart', methods=['GET'])
def get_chart():
    return render_template("chart.html")


@app.route('/about_us', methods=['GET'])
def get_about_us():
    return render_template("about_us.html")


@app.route('/contact_us', methods=['GET'])
def get_contact_us():
    return render_template("contact_us.html")


@app.route('/help', methods=['GET'])
def get_help():
    return render_template("help.html")


# start server on port 4000
app.run(host='0.0.0.0', port=4000, debug=True)
