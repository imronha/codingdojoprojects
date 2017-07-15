from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'the_wall')
app.secret_key = "dkajsd"
import re
import md5

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    full_name = request.form['first_name'] + request.form['last_name']
    email = request.form['email']
    password = request.form['pw']
    pwconfirm = request.form['pwconfirm']
    errors = False
    if len(request.form["first_name"]) < 2:
        flash("Your first name must be at least 2 letters long!")
        errors = True
    if len(request.form["last_name"]) < 2:
        flash("Your last name must be at least 2 letters long!")
        errors = True
    if len(request.form["last_name"])<2 and len(request.form["first_name"]) <2 and full_name.isalpha()==False:
            flash("Your name cannot contain any numbers or special characters.")
            errors = True
    if len(email) == 0:
        flash("You must include an email!")
        errors = True
    elif not EMAIL_REGEX.match(email):
        flash("Please enter a valid email")
        errors = True
    if len(password) == 0:
        flash("You must include a password!")
        errors = True
    elif len(password) < 8:
        flash("Your password must be at least 8 letters long!")
        errors = True
    elif password != pwconfirm:
        flash("Your password confirmation must be the same as your password!")
        errors = True
    if not errors:
        hashed_pw = md5.new(request.form['pw']).hexdigest()
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
        data = {
            "first_name": request.form['first_name'],
            "last_name": request.form['last_name'],
            "email": request.form['email'],
            "password": hashed_pw
        }
        mysql.query_db(query, data)
        flash("Thank you for submitting your information")
    return redirect('/')

@app.route('/login', methods=["POST"])
def login():
    query_login = "SELECT * FROM users WHERE email = :em"
    data = {
        "em": request.form['email']
    }
    found_user = mysql.query_db(query_login, data)
    hashed_pw = md5.new(request.form['pw']).hexdigest()
    if len(found_user)>0 and hashed_pw == found_user[0]['password']:
        session["user_id"] = found_user[0]['id']
        session["user_name"] = found_user[0]['first_name']+ " "+found_user[0]['last_name']
        return redirect('/wall')
    else:
        return redirect('/')

@app.route('/messages', methods=["POST"])
def create_message():
    query_message = "INSERT INTO messages (user_id, content, created_at, updated_at) VALUES (:u_id, :msg, NOW(), NOW())"
    data = {
        "u_id": session['user_id'],
        "msg": request.form['message'],
    }
    mysql.query_db(query_message, data)
    return redirect('/wall')

@app.route('/comments/<message_id>', methods=["POST"])
def create_comment(message_id):
    query_comments = "INSERT INTO comments (user_id, message_id, content, created_at, updated_at) VALUES (:u_id, :m_id, :cmt, NOW(), NOW())"
    data = {
        "u_id": session['user_id'],
        "m_id": message_id,
        "cmt": request.form['comment']
    }
    mysql.query_db(query_comments, data)
    return redirect('/wall')



@app.route('/wall')
def wall():
    query = "SELECT users.first_name, users.last_name, DATE_FORMAT(messages.created_at, '%M-%D %Y') as created_at, messages.content, messages.id FROM messages JOIN users ON users.id = messages.user_id ORDER BY messages.created_at DESC LIMIT 10"
    all_messages = mysql.query_db(query)
    print all_messages
    for message in all_messages:
        message['comments'] = []
        query = "SELECT users.first_name, users.last_name, DATE_FORMAT(comments.created_at, '%M-%D %Y') as created_at, comments.content, comments.id FROM comments JOIN users ON users.id = comments.user_id WHERE comments.message_id = :m_id ORDER BY comments.created_at DESC LIMIT 10"
        data = {
            "m_id":message['id']
        }
        message['comments'] = (mysql.query_db(query,data))
    return render_template('wall.html', messages = all_messages)
# @app.route('/login', methods=['POST'])
# def login():
#
#     query = "SELECT email, password, id, first_name FROM users"
#     query_return = mysql.query_db(query)
#     # Hash the users entered pw
#     pw_entered = md5.new(request.form['pw']).hexdigest()
#     # Iterate through the db to see if users input matches email and stored hashed password
#     for i in range(0,len(query_return)):
#         if query_return[i]['email'] == request.form['email'] and query_return[i]['password'] == pw_entered:
#             session["id"] = query_return[i]['id']
#             session["first_name"] = query_return[i]['first_name']
#             select_msgs = "SELECT * FROM messages JOIN users ON users.id = messages.user_id ORDER BY messages.created_at DESC LIMIT 8"
#             stored_msgs = mysql.query_db(select_msgs)
#             # print stored_msgs
#             return render_template('wall.html', all_messages=stored_msgs)
#     if query_return[i]['email'] != request.form['email']:
#         flash("Your email or password was incorrect!")
#         return redirect('/')
#
# @app.route('/send', methods=['POST'])
# def send():
#     message = request.form['message']
#     query = "INSERT INTO messages (content, created_at, updated_at, user_id) VALUES (:message, NOW(), NOW(), :id)"
#     data = {
#         "message": message,
#         "id": session['id']
#     }
#     mysql.query_db(query, data)
#     select_msgs = "SELECT * FROM messages JOIN users ON users.id = messages.user_id ORDER BY messages.created_at DESC LIMIT 8"
#     stored_msgs = mysql.query_db(select_msgs)
#     return render_template('wall.html', all_messages=stored_msgs)
#
# @app.route('/comment', methods=['POST'])
# def comment():
#     comment = request.form['comment']
#     select_msgs = "SELECT * FROM messages JOIN users ON users.id = messages.user_id ORDER BY messages.created_at DESC LIMIT 8"
#     stored_msgs = mysql.query_db(select_msgs)
#     print stored_msgs[0]['id']
#     query = "INSERT INTO comments (content, created_at, updated_at, user_id, message_id) VALUES (:comment, NOW(), NOW(), :user_id, :msg_id)"
#     data = {
#         "comment": request.form['comment'],
#         "user_id": session['id'],
#         "msg_id": 1
#     }
#     mysql.query_db(query, data)
#     select_comments = "SELECT * FROM comments JOIN messages ON messages.id = comments.message_id ORDER BY comments.created_at DESC LIMIT 2"
#     stored_comments = mysql.query_db(select_comments)
#     # print stored_comments
#     return render_template('wall.html', all_messages=stored_msgs, all_comments=stored_comments)

app.run(debug=True)
