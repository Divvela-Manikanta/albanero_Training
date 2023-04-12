from flask import Flask,request,redirect,url_for

app = Flask(__name__)

# @app.route('/hello')
# def hello_world():
#     return "hello world"

# @app.route('/')
# def hii_world():
#     return "hii"


# app.route('/<username>')
# def mani(username):
#     return username

# mani('mani')


# @app.route('/projects/')
# def projects():
#     return 'The project page'

# @app.route('/about')
# def about():
#     return 'The about page'


# from markupsafe import escape

# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return f'User {username}'

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return f'Post {post_id}'

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return f'Subpath {(subpath)}'


# @app.route('/login', methods =['GET','POST'])
# def login():
#     if(request.method == 'POST'):
#         return 'you are tried to  login'
#     else:
#         return redirect(url_for(hii_world))

@app.route('/login')
def login():
    return "You are redirected to login page becz you have selected post method"

@app.route('/view')
def view():
    return 'you are redirected to the get page'

@app.route('/',methods=['GET','POST'])
def main():
    if(request.method == 'GET'):
        return redirect(url_for(view))
    else:
        return redirect(url_for(login))

    
if __name__ =='__main__':
    app.run()
    
