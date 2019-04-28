# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request, session, flash
from functools import wraps
from pymongo import MongoClient
import datetime

# create the application object
app = Flask(__name__)

# config
app.secret_key = 'my precious'

# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

# use decorators to link the function to a url
@app.route('/')
@login_required
def home():
    return "Hello, World!"  # return a string

@app.route('/welcome', methods=['GET', 'POST'])
@login_required
def welcome():

    client = MongoClient(
        "mongodb://priyagup:Codepri%40143@advancedropboxproject-shard-00-00-jdfx8.mongodb.net:27017,advancedropboxproject-shard-00-01-jdfx8.mongodb.net:27017,advancedropboxproject-shard-00-02-jdfx8.mongodb.net:27017/test?ssl=true&replicaSet=AdvanceDropboxproject-shard-0&authSource=admin&retryWrites=true")
    db = client["AdvanceDropboxproject"]
    col = db["Files"]
    doc = col.find({"access": session['uname']})
    result =[]
    for x in doc:
        result.append(x)
    if request.method == 'POST':
        session['file_name']=request.form['file_name']
        return redirect(url_for('show_edit'))

    return render_template('welcome.html',posts=result)  # render a template

@app.route('/show', methods=['GET','POST'])
@login_required
def show_edit():
    client = MongoClient(
        "mongodb://priyagup:Codepri%40143@advancedropboxproject-shard-00-00-jdfx8.mongodb.net:27017,advancedropboxproject-shard-00-01-jdfx8.mongodb.net:27017,advancedropboxproject-shard-00-02-jdfx8.mongodb.net:27017/test?ssl=true&replicaSet=AdvanceDropboxproject-shard-0&authSource=admin&retryWrites=true")

    db = client["AdvanceDropboxproject"]
    col = db["Files"]
    doc = col.find({"name": session['file_name']})
    result = []
    for x in doc:
        result.append(x)
    content = result[0]['content']
    show_his = db["History"]
    show_doc = show_his.find({"name": session['file_name']})
    history = []
    for i in show_doc:
        history.append(i)

    history_dict =[]
    if len(history)>5:
        for j in range(len(history), len(history)-5, -1):
            history_dict.append(history[j-1])
    else:
        history_dict=history.copy()


    if request.method == 'POST':
        to_update = request.form['awesome']
        his_col = db["History"]
        addr = request.remote_addr
        print(addr)
        now = datetime.datetime.now()
        lis = {"name": session['file_name'], "address": addr, "Time": now.strftime("%c"), "uname":session['uname']}
        his_col.insert_one(lis)
        col.update_one({'name': session['file_name']}, {"$set": {"content": to_update}}, upsert=False)
        return redirect(url_for('welcome'))


    # with open("wordfile.txt", "r") as f:
    #   content = f.read()

    return render_template('show.html', content=content, history=history_dict)


@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        with open(f.filename, "r") as fl:
            content = fl.read()
        client = MongoClient(
            "mongodb://priyagup:Codepri%40143@advancedropboxproject-shard-00-00-jdfx8.mongodb.net:27017,advancedropboxproject-shard-00-01-jdfx8.mongodb.net:27017,advancedropboxproject-shard-00-02-jdfx8.mongodb.net:27017/test?ssl=true&replicaSet=AdvanceDropboxproject-shard-0&authSource=admin&retryWrites=true")

        db = client["AdvanceDropboxproject"]
        col = db["Files"]
        row = {"name": f.filename, "content": content}
        x=col.insert_one(row)
        print(content)
        print(x)
        return 'Uploaded successfully'
    return render_template('upload.html')

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        client = MongoClient(
            "mongodb://priyagup:Codepri%40143@advancedropboxproject-shard-00-00-jdfx8.mongodb.net:27017,advancedropboxproject-shard-00-01-jdfx8.mongodb.net:27017,advancedropboxproject-shard-00-02-jdfx8.mongodb.net:27017/test?ssl=true&replicaSet=AdvanceDropboxproject-shard-0&authSource=admin&retryWrites=true")

        db = client["AdvanceDropboxproject"]
        col = db["Credentials"]
        my_query = {"uname":request.form['username']}
        doc=col.find(my_query)
        result=[]
        for x in doc:
            result.append(x)
        if len(result)==0:
            error = "Please check your credentials and try again"
        elif request.form['password']!=result[0]['pwd']:
            error =  'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            session['uname'] = request.form['username']
            flash('You were logged in.')
            return redirect(url_for('welcome'))
    return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were logged out.')
    return redirect(url_for('login'))

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 5500)
