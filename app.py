from flask import Flask, make_response, request
import tweepy
import config

app = Flask(__name__)

client = tweepy.Client(bearer_token=config.BEARER_TOKEN,
                       consumer_key=config.API_KEY,
                       consumer_secret=config.API_KEY_SECRET,
                       access_token=config.ACCESS_TOKEN,
                       access_token_secret=config.ACCESS_TOKEN_SECRET)


@app.route("/sendTweet", methods=["POST", "GET"])
def send_tweet():
    response = client.create_tweet(text=request.args['text'])
    resp = make_response(response.data)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route("/getTweet", methods=["POST", "GET"])
def get_tweet():
    response = client.get_tweet(id=request.args['id'])
    resp = make_response(response.data['data'])
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route("/deleteTweet", methods=["POST", "GET"])
def delete_tweet():
    response = client.delete_tweet(id=request.args['id'])
    resp = make_response(response.data)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

if __name__ == '__main__':
    app.run()
