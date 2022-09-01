#!/bin/python3

from flask import Flask, render_template
import requests
import json
import urllib.request

app = Flask(__name__)

def give_me_the_ip():
    return urllib.request.urlopen('https://v4.ident.me').read().decode('utf8')

def give_me_the_port():
    return 80

def give_me_the_route():
    return "api"

def give_me_the_refresh():
    return "http://{host}:{port}/{route}".format(host=give_me_the_ip(), port=give_me_the_port(), route=give_me_the_route())

def get_meme():
    #Uncomment these two lines and comment out the other url line if you want to use a specific meme subreddt
    # sr = "/wholesomememes"
    # url = "<https://meme-api.herokuapp.com/gimme>" + sr
    url = "https://meme-api.herokuapp.com/gimme"
    response = json.loads(requests.request("GET", url).text)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_large, subreddit

@app.route("/api", methods=['GET'])
def index():
    meme_pic,subreddit = get_meme()
    return render_template("index.html", meme_pic=meme_pic, subreddit=subreddit, refresh_url=give_me_the_refresh())

app.run(host=give_me_the_ip(), port=give_me_the_port())
