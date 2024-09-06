from flask import Flask, render_template, request, redirect, url_for
from post import Post, validation
import requests
from db import session, users, Signup
from werkzeug.security import check_password_hash

app = Flask(__name__)

#API url endoints
#url = " https://newsapi.org/v2/top-headlines"
#url_1 = "https://newsapi.org/v2/everything"

#parameters for the url
#qury = "q=world%20economy&sortBy=relevancy&pageSize=3&apiKey=7bce52cd1385491385d8146e1f2caaea"


#Getting response from API and initializing them
response = requests.get(f"https://newsapi.org/v2/everything?q=economy&sortBy=relevancy&pageSize=3&apiKey=7bce52cd1385491385d8146e1f2caaea")
if response.status_code == 200:
    print("pass")

    
posts_data = response.json()

#get article list for each post
article = posts_data.get('articles', [])

store_post = []

for posts in article:
    init_post = Post(
                    author=posts['author'],
                    title=posts['title'],
                    description=posts['description'],
                    image=posts['urlToImage'],
                    publishedAt=posts['publishedAt'],
                    content=posts['content'],
                    url=posts['url']
                )
    store_post.append(init_post) #each post is indexed in this list


@app.route('/')
def get_all_posts():
    return render_template("index.html", posting=store_post)

#for post
@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for post in store_post:
        if post.id == index:
            requested_post = post
            break
    return render_template("post.html", blog=requested_post)
'''
#@app.route("/search/<keyword>")
#def search(keyword):
    
'''
#for signup
@app.route("/signup", methods=["GET", "POST"])
def sign_up():
    error = None
    new_user = None
    if request.method == "POST":
        s_username = request.form['username']
        s_password = request.form['password']
        email = request.form['email']

        valid = validation(username=s_username, password=s_password)
        
        if valid == True:
            new_user = Signup(username=s_username, password=s_password, email=email)
            session.add(new_user)
            session.commit()
            return redirect(url_for("recieve_data"))
        else:
            error = "Validation failed"
    
    return render_template("signup.html", error=error)
    
#for login
@app.route("/login", methods=["GET", "POST"])
def receive_data():
    error = None
    
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
    
        valid = validation(username=username, password=password)
        
        if valid != True:
            error = valid
            return render_template("login.html", warning=error)
        
        #checking login details in database
        user = session.query(users).filter_by(uname=username).all()
        if user != True:
            error = "login details not found"
            return render_template("login.html", warning=error)
        
        authenticated = False
        for _user in user:
            if  _user and check_password_hash(_user.passwd, password):
                authenticated = True
                break
        
        if authenticated == True:
            return redirect(url_for('get_all_posts'))
        else:
            error = "Invalid username or password"
            return render_template("login.html", warning=error)
    
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)


