reddit-caller
=============

A Flask app that renders the top Reddit headline as xml and call to the Twilio API to read it over the phone.


Details
-------------
In [run.py](https://github.com/eudaimonious/reddit-caller/blob/master/run.py), I've utilized [PRAW: The Python Reddit API Wrapper](https://github.com/praw-dev/praw) to grab the "top" (ie, not "hot") submission off Reddit's front page. I then render the result in [Twilio Markup XML](https://www.twilio.com/docs/api/2008-08-01/twiml) at https://reddit-caller.herokuapp.com/.

I've used Heroku Scheduler to kick off [make-call.py](https://github.com/eudaimonious/reddit-caller/blob/master/make-call.py). This calls the [Twilio REST API](https://www.twilio.com/docs/api/rest) which will make a phone call and read off the contents of the xml page. I've instituted the following environment variables: SID (Twilio account SID), TOKEN (Twilio auth token), TO (phone number to receive the call, in the format +5551231234) and FROM.
