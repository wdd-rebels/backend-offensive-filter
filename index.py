from flask import Flask, request, jsonify
from textblob import TextBlob
from profanity_check import predict

app = Flask(__name__)

@app.route("/healthcheck")
def hello():
    return "up!"

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
    is_profane = 1 in predict([tweet['text']])
    offensive_filter_value = polarity < -0.35 or is_profane
    response = {'id': tweet['id'], 'filter': offensive_filter_value}
    return response

if __name__ == '__main__':
    app.run(debug=True)