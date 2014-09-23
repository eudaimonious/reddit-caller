import os
import praw
from flask import Flask, Response, render_template

app = Flask(__name__)

def get_top_submission():
  user_agent = "github.com/eudaimonious/reddit-caller by /u/eudaimonious"
  # connecting to reddit api
  r = praw.Reddit(user_agent=user_agent)
  # getting top submission
  submissions = r.get_top(limit=1)
  # converting from generator
  sub_list = [str(x) for x in submissions]
  top = sub_list[0]
  # grabbing just the headline
  start = top.rfind(':') + 2
  headline = top[start:]
  return headline


@app.route('/')
def home():
  return Response(render_template('reddit-top.xml', headline=get_top_submission()), mimetype='text/xml')

if __name__ == "__main__":
    app.run(debug=True)