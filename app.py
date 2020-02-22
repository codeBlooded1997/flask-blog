from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)  # created app
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"  # configuring setting required for database and defining which database are we using
db = SQLAlchemy(app)    # links the app and database to eachother

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
    return render_template('index.html')

@app.route('/posts')
def posts():
    return render_template('posts.html', posts=all_posts)

@app.route('/home/users/<string:name>/posts/<int:id>')  # defining a route
def hello(name, id):  # this code will run whenever we get to the URL in previous line
    return "Hello, " + name + ", your id is : " + str(id)

@app.route('/onlyget', methods=['POST'])
def get_req():
    return "You can only get this webopage 4."

if __name__ == "__main__":  # if we are running the app from command line(__main__)
    app.run(debug=True)  # it will turn on debug mode
