import os
from flask import Flask, Response, render_template
import praw

app = Flask(__name__)

def get_top_submission():
  # connect to reddit api
  user_agent = "github.com/eudaimonious/reddit-caller by /u/eudaimonious"
  r = praw.Reddit(user_agent=user_agent)
  # get title of top submission
  for submission in r.get_top(limit=1):
    headline = str(submission.title)
  return headline


@app.route('/', methods=['GET', 'POST'])
def home():
  return Response(render_template('reddit-top.xml', headline=get_top_submission()), mimetype='text/xml')

if __name__ == "__main__":
    app.run(debug=True)