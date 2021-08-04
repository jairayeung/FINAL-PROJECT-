users = {
    "chums@example.com":{"password":"Ch@ng3m3!",
                         "first_name":"Matthew",
                         "last_name":"Uy",
                         "org":"MedGrocer",
                         "brand":"Sinovac"},
    "joben@example.com":{"password":"Ch@ng3m3!",
                         "first_name":"Joben",
                         "last_name":"Ilagan",
                         "org":"MedGrocer",
                         "brand":"Sinovac"},
    "bong@example.com":{"password":"Ch@ng3m3!",
                        "first_name":"Bong",
                        "last_name":"Olpoc",
                        "org":"MedGrocer",
                        "brand":"Sinovac"},
    "joaqs@example.com":{"password":"Ch@ng3m3!",
                         "first_name":"Joaqs",
                         "last_name":"Gonzales",
                         "org":"MedGrocer",
                         "brand":"Sinovac"},
    "gihoe@example.com":{"password":"Ch@ng3m3!",
                         "first_name":"Gio",
                         "last_name":"Hernandez",
                         "org":"MedGrocer",
                         "brand":"Sinovac"},
    "vic@example.com":{"password":"Ch@ng3m3!",
                       "first_name":"Vic",
                       "last_name":"Reventar",
                       "org":"MedGrocer",
                       "brand":"Sinovac"},
    "joe@example.com":{"password":"Ch@ng3m3!",
                       "first_name":"Joe",
                       "last_name":"Ilagan",
                       "org":"MedGrocer",
                       "brand":"Sinovac"},
    "janna@example.com":{"password":"tan",
                         "first_name":"Janna",
                         "last_name":"Tan",
                         "org":"MedGrocer",
                         "brand":"Sinovac"}
}

def get_user(username):
    try:
        return users[username]
    except KeyError:
        return None

from flask import Flask,redirect
from flask import Flask, url_for
from flask import request
from flask import session
app = Flask(__name__)

@app.route("/signup", methods =['GET', 'POST'])
def signup():
    if request.method == "POST":
        firstname = request.form['first_name']
        lastname = request.form['last_name']
        emailad = request.form['username']
        pw = request.form['password']
        cp = request.form['cpassword']
        vo = request.form['org']
        brand = request.form['brand']
        return redirect(url_for('Registered', fname = firstname, lname = lastname, name = emailad,passwrd = pw, cpasswrd =cp , org = vo, b = brand ))
    else:
        firstname = request.args.get['first_name']
        lastname = request.args.get['last_name']
        emailad = request.args.get['username']
        pw = request.args.get['password']
        cp = request.args.get['cpassword']
        vo = request.args.get['org']
        brand = request.args.get['brand']
        return redirect(url_for('Registered', fname = firstname, lname = lastname, name = emailad,passwrd = pw, cpasswrd =cp, org = vo, b = brand ))

@app.route('/registered/<fname>/<lname>/<name>/<passwrd>/cpasswrd/<org>/<b>/')
def registered(fname,lname,name,passwrd,org,b):
    if passwrd==cpasswrd:
        users.update({name:{"password":passwrd,
                             "first_name":fname,
                             "last_name":lname,
                             "org":org,
                             "brand":b}})
        return "<h1>You have successfully signed up!!</h1>"
    else:
        return "<h1>Password doesn't match</h1>"
