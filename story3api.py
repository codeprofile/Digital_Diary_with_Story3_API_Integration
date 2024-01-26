from constants import *
import requests


def create_story(data):
    # Make a POST request to the API endpoint
    headers = {
        'accept': 'application/json',
        'x-auth-token': API_KEY,
        'Content-Type': 'application/json'
    }
    response = requests.post(STORIES_URL, headers=headers, json=data, verify=False)
    if response.status_code == 200:
        return 'Diary entry saved successfully'
    else:
        return 'Failed to save diary entry'


def get_stories():
    headers = {
        'accept': 'application/json',
        'x-auth-token': API_KEY
    }
    params = {
        'limit': 25,
        'offset': 0
    }
    response = requests.get(STORIES_URL, headers=headers, params=params, verify=False)
    story_list = []

    if response.status_code == 200:
        stories = response.json()
        for story in stories:
            if story["nickname"] == "laxmi":
                print(story)
                date, image, title = story["title"].split("_")
                story_list.append({"title": title, "date": date, "image": image, "body": story["body"]})
        return story_list
