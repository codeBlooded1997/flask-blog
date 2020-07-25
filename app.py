from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Defining app object
app = Flask(__name__)  # created app
# Specifying configuration for app.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"  # configuring setting required for database and defining which database are we using
db = SQLAlchemy(app)  # links the app and database to eachother


# MODEL
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default='N/A')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # prints out when we created new blog post
    def __repr__(self):
        return 'Blog post ' + str(self.id)

all_posts = [
    {'title': 'post1',
     'content': 'This is content of post 1. lalalala....',
     'author': 'arian'
     },
    {'title': 'post2',
     'content': 'This is content of post 2. hahaha....'
     }
]

@app.route('/')
def index():
    return render_template('index.html')    # sending to front-end

@app.route('/posts', methods=['GET', 'POST'])
def posts():
    if request.method == 'POST':
        print('if is running')
        post_title = request.form['title']
        post_content = request.form['content']
        new_post = BlogPost(title=post_title, content=post_content, author='Kareyo')   # creating postst from inputs to save in db

        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:
        all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()   # reading posts form db
        print('else is running')
        return render_template('posts.html', posts=all_posts)   # sending to front-end


if __name__ == "__main__":  # if we are running the app from command line(__main__)
    app.run(debug=True)  # it will turn on debug mode
