from flask import Flask,request,redirect,url_for,render_template,abort

app = Flask(__name__)


# @app.route('/login')
# def login():
#     return "username and password are correct"

# @app.route('/view')
# def view():
#     return 'username and password are not correct'

# @app.route('/<username>/<int:password>')
# def main2(username,password):
#     # if(request.method == 'GET'):
#     #     return redirect(url_for('view'))
#     # else:
#     #     return redirect(url_for('login'))
#     if(username=='mani' and password== 1234):
#         return redirect(url_for('login'))
#     else:
#         return redirect(url_for('view'))

# @app.route('/login2')
# def valid_login(name,pw):
#     return name
#     return 'in valid login'

# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return f"{request.form['username']}"
#         else:
#             error = 'Invalid username/password'
#     # the code below is executed if the request method
#     # was GET or the credentials were invalid
#     return render_template('login.html', error=error)
       



# @app.route('/log')
# def log():
#     # abort(400)
#     return {
#         "username": "mani",
#         "theme": "black"    
#     }
# @app.errorhandler(400)
# def under_mainaince_error(error):
#     return render_template('error.html')

# app.logger.debug("this is a debug message")
# app.logger.error("this is a error message")

@app.route('/about')
def about1():
    return "in about1"

@app.route('/about/')
def about2():
    return "in about2"
if __name__ =='__main__':
    app.run(port=8000,debug=True)