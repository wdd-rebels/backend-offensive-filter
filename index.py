from flask import Flask, request, jsonify
from textblob import TextBlob
from profanity_check import predict
from nltk.stem import PorterStemmer

app = Flask(__name__)

@app.route("/healthcheck")
def hello():
    return "up!"

@app.route('/classify', methods = ['POST'])
def classifyTweet():
    json = request.get_json()
    tweet_responses = []
    for tweet in json['tweets']:
        tweet_responses.append(processTweet(tweet, json['categories']))
    response = {'tweets': tweet_responses}
    return jsonify(response)

def processTweet(tweet, categories):
    porter = PorterStemmer()

    categories_stemmed = set(list(map(lambda cat: porter.stem(cat), categories)))
    tweet_stems = set(list(map(lambda cat: porter.stem(cat), tweet['text'].split())))

    intersection = categories_stemmed.intersection(tweet_stems)

    contains_prohibited_categories = len(intersection) > 0
    is_polarising = TextBlob(tweet['text']).sentiment.polarity < -0.35
    is_profane = 1 in predict([tweet['text']])

    offensive_filter_value = is_polarising or is_profane or contains_prohibited_categories

    response = {'id': tweet['id'], 'filter': offensive_filter_value, 'categories': list(intersection)}
    return response

if __name__ == '__main__':
    app.run(debug=True)