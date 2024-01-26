import json

from flask import Flask, render_template, request
from story3api import get_stories, create_story
import os

app = Flask(__name__)

UPLOAD_FOLDER = './static/images/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/diary")
def diary():
    return render_template("diary.html")


@app.route("/save_diary_entry", methods=['POST'])
def save_diary_entry():
    # Get data from the request
    image = request.files.get("image")
    date = request.form.get('date')
    title = request.form.get('title')
    body = request.form.get('story')
    # Prepare the data for the API request
    if image:
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
        image = image.filename
    else:
        image = "images/default.jpg"
    data = {
        'title': str(date) + "_" + str(image) + "_" + str(title),
        'body': body
    }
    print(data)
    return create_story(data)


@app.route("/story_list")
def story_list():
    story_list = get_stories()
    print("Printing all received stories", story_list)
    return render_template("story_list.html", stories=story_list)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
