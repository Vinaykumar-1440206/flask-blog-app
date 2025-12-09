from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {"title": "My First Blog", "content": "Welcome to my first Flask blog!"},
    {"title": "Learning Flask", "content": "Flask is a very simple and powerful web framework."},
]

@app.route("/")
def index():
    return render_template("index.html", posts=posts)

if __name__ == "__main__":
    app.run(debug=True)
