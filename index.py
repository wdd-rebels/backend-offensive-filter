from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/classify', methods = ['POST'])
def classifyTweet():
    json = request.get_json()
    tweet_responses = []
    for tweet in json['tweets']:
        tweet_responses.append(processTweet(tweet))
    response = {'tweets': tweet_responses}
    return jsonify(response)

def processTweet(tweet):
    polarity = TextBlob(tweet['text']).sentiment.polarity
    offensive_filter_value = True if polarity<0 else False
    response = {'id': tweet['id'], 'filter': offensive_filter_value}
    return response

if __name__ == '__main__':
    app.run(debug=True)