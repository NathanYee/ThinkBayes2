
# coding: utf-8

# In[1]:

from twython import TwythonStreamer


# In[2]:

def getKeys(file_path):
    keys = []
    with open(file_path, 'r') as f:
        for line in f:
            keys.append(line.replace('\n', ''))
    return keys

APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET = getKeys('../../twitterKeys.txt')


# In[3]:

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print(data['text'])

    def on_error(self, status_code, data):
        print(status_code)

        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        self.disconnect()


# In[4]:

def append_to_file(path, data):
    """
    append_to_file appends a line of data to specified file.  Then adds new line
    
    Args:
        path (string): the file path
    
    Return:
        VOID
    """
    with open(path, 'a') as file:
        file.write(data + '\n')


# In[5]:

def set_to_file(tweets, file_name):
    """
    set_to_file iterates through a set, each tweet is a new line in the file
    
    ARGS:
        links (set): a set that contains tweets
        file_name (string): the name of the file we want to write to
        
    Return:
        VOID
    """
    for tweet in tweets:
        append_to_file(file_name, tweet)


# In[6]:

stream = MyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
stream.statuses.filter(track='#python, #java, #javascript, #haskell, #clojure')


# In[ ]:



