from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
def home():
    request = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = request.json()
    return render_template("index.html", posts=all_posts)


@app.route('/post/<post_id>')
def get_post(post_id):
    request = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = request.json()
    requested_post = None
    for post in all_posts:
        if post["id"] == int(post_id):
            requested_post = post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
