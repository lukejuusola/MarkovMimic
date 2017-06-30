# MarkovMimic
An extremely simple twitter markov chain bot. Trains on an account and tweets like they would

To set a bot up, first you need a keys for twitter applications, which you can find at apps.twitter.com.

Then run the following commands: <br />
  `git clone https://github.com/lukejuusola/markovmimic`
  `cd ./markovmimic` <br />
  `virtualenv -p python3 venv` <br />
  `source venv/bin/activate` <br />
  `pip install -r requirements.txt` <br />

Then add your keys to the botAuth.py file and the account name to train on to the ScrapeTweets.py file.
Finally, run the command: <br />
  `python MarkovMimic.py`

The bot should now be training on the data and should post to the account you've given it access to shortly!

*Note* For every new terminal you want to run this bot in, you need to rerun the commands: <br />
  `source venv/bin/activate` <br />
  `python MarkovMimic.py` <br />
This runs the virtual environment that we have downloaded the necessary dependencies in. 
