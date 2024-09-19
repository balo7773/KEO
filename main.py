from flask import Flask, render_template, request, redirect, url_for, flash, session
from post_and_validation import Post, login_manager, load_user, validation
import requests
from db import session as db_session, Signup
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import date, timedelta
from flask_login import login_user, logout_user, login_required, current_user
import os

app = Flask(__name__)

login_manager.login_view = "login"
login_manager.init_app(app)
app.secret_key = os.urandom(24)
#API url endoints
#url = " https://newsapi.org/v2/top-headlines"
#url_1 = "https://newsapi.org/v2/everything"

#parameters for the url
#qury = "q=world%20economy&sortBy=relevancy&pageSize=3&apiKey=7bce52cd1385491385d8146e1f2caaea"


#for date
current_date = date.today().isoformat()
three_days_bfor_cd = (date.today() - timedelta(days=3)).isoformat()

#Getting response from API and initializing them
response_2 = requests.get("https://financialmodelingprep.com/api/v3/fmp/articles?page=5&size=12&apikey=l0PIZQxrsDN5gjx2CvDaIwShIlCf9UwL")


if response_2.status_code == 200:
    print("pass_2")
    
    
post_data_2 = response_2.json()

article_2 = post_data_2.get('content', [])
store_post_2 = []

for post_2 in article_2:
    init_post_2 = Post (
                    author=post_2['author'],
                    title=post_2['title'],
                    description=post_2['tickers'],
                    image=post_2['image'],
                    publishedAt=post_2['date'],
                    content=post_2['content'],
                    url=post_2['link']
                )
    store_post_2.append(init_post_2)

print(store_post_2)


store_post = []
def get_post(keyname):
    response = requests.get(f"https://newsapi.org/v2/everything?q={keyname}&sortBy=popularity&pageSize=17&apiKey=7bce52cd1385491385d8146e1f2caaea")
    if response.status_code == 200:
        print("pass")
    posts_data = response.json()
    #get article list for each post
    article = posts_data.get('articles', [])
    for posts in article:
        init_post = Post(
                    author=posts['author'],
                    title=posts['title'],
                    description=posts['description'],
                    image=posts['urlToImage'],
                    publishedAt=posts['publishedAt'],
                    content=posts['content'][0:],
                    url=posts['url']
                )
        store_post.append(init_post) #each post is indexed in this list
        
    print(store_post)
    return store_post

search_post = []

@app.route('/')
def home():
    return render_template("home.html", posting_2=store_post_2)

@app.route('/get_post/<keyword>', methods=['GET'])
def get_all_posts(keyword):
    post = get_post(keyword)
        
    page_number = int(request.args.get('page_number', 1))
    page_size = 5  # Number of posts per page
    total_pages = len(store_post) // page_size + (1 if len(store_post) % page_size > 0 else 0)  # Total pages

    # Calculate the start and end indices for pagination
    start = (page_number - 1) * page_size
    end = start + page_size
    if end > len(store_post):
        end = len(store_post)

    # Handle "Next" and "Previous" button logic
    is_next = request.args.get('next')
    is_prev = request.args.get('prev')
    
    # If "Next" is clicked, increase page number
    if is_next == 'true' and page_number < total_pages:
        page_number += 1
    # If "Previous" is clicked, decrease page number
    elif is_prev == 'true' and page_number > 1:
        page_number -= 1

    # Recalculate start and end after changing page number
    start = (page_number - 1) * page_size
    end = start + page_size
    if end > len(store_post):
        end = len(store_post)

    return render_template("index.html", route_name='get_all_posts', keyword=keyword, posting=post[start:end], _end=end, _total_pages=total_pages, _page_number=page_number)
    

#read latest news
@app.route("/latest-news/<int:index>")
def news(index):
    requested_post_2 = None
    for post_2 in store_post_2:
        if post_2.id == index:
            requested_post_2 = post_2
            break
    return render_template("news.html", blog_2=requested_post_2)

@app.route("/search", methods=['GET'])
def search():
    search_keyword = request.args.get('query')
    if search_keyword == None:
        return redirect(url_for('home'))
    is_next = request.args.get('next')  # Check if the next button is clicked
    is_prev = request.args.get('prev')  # Check if the previous button is clicked
    page_number = 1
    page_size = 5
    global search_post
    search_post = []
    search_response = requests.get(f"https://newsapi.org/v2/everything?q={search_keyword}&from={three_days_bfor_cd}&to={current_date}&sortBy=popularity&pageSize=17&apiKey=7bce52cd1385491385d8146e1f2caaea")
    
    if search_response.status_code == 200:
        print("pass search")
        search_post_data = search_response.json()
        search_news = search_post_data.get('articles', [])
        # check for article
        if not search_news:
            return render_template("index.html", posting=[], _end=0, _total_pages=0)

        #for search post       
        for news in search_news:
            search_init = Post(
                    author=news['author'],
                    title=news['title'],
                    description=news['description'],
                    image=news['urlToImage'],
                    publishedAt=news['publishedAt'],
                    content=news['content'][0:],
                    url=news['url']
            )
            search_post.append(search_init)
        
        total_pages = len(search_post)
        start = (page_number - 1) * page_size
        end = start + page_size
        # Handle pagination logic for "Next" and "Previous" buttons
        if is_next == 'true':
            page_number += 1
            start = (page_number - 1) * page_size
            end = start + page_size
        elif is_prev == 'true':
            page_number -= 1
            start = (page_number - 1) * page_size
            end = start + page_size
        # Ensure we don't exceed the number of results
        if end > total_pages:
            end = total_pages

        return render_template("index.html", route_name='search', posting=search_post[start:end], _end=end, _total_pages=total_pages, _page_number=page_number)
    
    return render_template("index.html", posting=[], _end=0, _total_pages=0)
    

#for post
@app.route("/post/<int:index>")
def show_post(index):
    global search_post, store_post, store_post_2
    requested_post = None
    for post in store_post:
        if post.id == index:
            requested_post = post
            break
        else:
            continue
    
    for post in store_post_2:
        if post.id == index:
            requested_post = post
            break
        else:
            continue

    for post in search_post:
        if post.id == index:
            requested_post = post
            break
        else:
            continue
    return render_template("post.html", blog=requested_post)


#for signup
@app.route("/signup", methods=["GET", "POST"])
def signup():
    error_msg = None          
    new_user = None
    if request.method == "POST":
        s_username = request.form['username']
        s_password = request.form['password']
        email = request.form['email']

        valid = validation(username=s_username, password=s_password)
        hashed_password = generate_password_hash(s_password)
        if valid == True:
            new_user = Signup(uname=s_username, passwd=hashed_password, email=email)
            db_session.add(new_user)
            db_session.commit()
            flash('Signup successful! Please log in.', 'success')
            return redirect(url_for("login"))
        else:
            error_msg = "Validation failed"
            flash(error_msg, 'error')
            db_session.rollback()
    
    return render_template("signup.html", error=error_msg)

  
#for login
@app.route("/login", methods=["GET", "POST"])
def login():
    error_msg = None
    
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        valid = validation(username=username, password=password)
        
        if valid != True:
            error_msg = valid
            flash(error_msg, 'error')
            return render_template("login.html", warning=error_msg)
        
        # checking login details in database
        db_session.rollback()  # Used to ensure no previous query errors

        # Fetching a single user instead of a list
        user = db_session.query(Signup).filter_by(uname=username).first()
        if not user:
            error_msg = "Login details not found"
            flash(error_msg, 'error')
            return render_template("login.html", warning=error_msg)
        
        # Checking the password for the user
        if user and check_password_hash(user.passwd, password):
            login_user(user)  # Logging in the single user
            session['user_id'] = user.id  # Storing user ID in session

            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            error_msg = "Invalid username or password"
            flash(error_msg, 'error')
            return render_template("login.html", warning=error_msg)
    
    return render_template("login.html")

@app.route('/about')
def about():
    return render_template('about.html')

@login_required
@app.route("/logout")
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))


if __name__ == "__main__":
    # Clear lists to ensure fresh data on each run
    Post.postId = 0
    app.run(debug=True)


