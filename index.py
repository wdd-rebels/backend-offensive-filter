from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/classify', methods = ['POST'])
def classifyTweet():
    tweets = request.get_json()
    print(tweets)
    return "NICE"

# def processTweet(tweet):
#     sentiment = TextBlob(tweet['text']).sentiment
#     response = {}
#     response['id']=
#     return jsonify(tweet)

if __name__ == '__main__':
    app.run(debug=True)