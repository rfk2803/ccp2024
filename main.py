from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def route_home():
   return render_template('home.html')

@app.route('/contactus')
def route_contactus():
   return render_template('contactus.html')

@app.route('/login')
def route_login():
   return render_template('login.html')

@app.route('/quote')
def route_quote():
   return render_template('quote.html')

@app.route('/users')
def route_users():
   return render_template('users.html')



if __name__ == '__main__':
   app.run()
