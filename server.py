from flask import Flask, redirect, url_for, render_template, request


app = Flask(__name__)


#   Homepage
@app.route("/")
def home():
    return render_template('index.html')
#   Homepage re-route
@app.route("/index.html/")
def home_reroute():
    return redirect(url_for("home"))
#Wheelbase page
@app.route("/steeringwheels.html")
def steer():
    return render_template('steeringwheels.html')
#monitors
@app.route("/monitors.html")
def monitosr():
    return render_template('comingsoon.html')
#pc specs
@app.route("/PC.html")
def pc():
    return render_template('PC.html')
#rigs
@app.route("/rig.html")
def rigs():
    return render_template('comingsoon.html')
#vr
@app.route("/vr.html")
def vr():
    return render_template('comingsoon.html')
#contact me
@app.route('/contact.html', methods=['post', 'get'])
def contact():
    message = ''
    if request.method == 'POST':
        name = request.form.get('Name')  # access the data inside 
        email = request.form.get('Email')
        phone = request.form.get('Phone No.')
        msg = request.form.get('Message')
        print(msg)
        message='Sent'

# #    Sign In and Sign Up
# @app.route('/signup.html', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         userdata = [request.form.get('email'), request.form.get('password'), request.form.get('fname'), request.form.get('lname'),request.form.get('passwordconfirm')]
#         if userdata[1]==userdata[4]:
#             with open('users.csv', 'a') as file:
#                 writer=csv.writer(file)
#                 writer.writerow(userdata[:4])
#         print(userdata)
#         return redirect(url_for("login"))
#     return render_template('signup.html')
#
#
#
# @app.route('/signin.html', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         userdata = [request.form.get('username'), request.form.get('password')]
#         print(userdata)
#         return 'Submitted Form'
#     return render_template('signin.html')



#about page
# @app.route("/about.html")
# def about():
#     return render_template('about.html')
#
# #lineup generator
# @app.route("/lineup-generator.html")
# def lineup():
#     return render_template('lineup-generator.html')
# #lineup re-route
# @app.route("/lineup/")
# def lineup_reroute():
#     return redirect(url_for("lineup"))
#
#
#
#
#
#
# #use this to route to specific drivers
# @app.route("/<name>/")
# def user(name):
#     return f"Hello {name}!"
#
# #admin page
# @app.route("/admin/")
# def admin():
#     return redirect(url_for("name"))

if __name__=="__main__":
    app.run()