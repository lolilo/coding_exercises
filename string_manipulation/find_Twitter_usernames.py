# Given a Tweet, find all usernames within the Tweet.
import re
USERNAME_PATTERN = re.compile('[^\w!]@[\w]+')
# \w indicates a word chracter
# A word character is a character from a-z, A-Z, 0-9, 
# including the _ (underscore) character.

def find_usernames(tweet):
    username_list = re.findall(USERNAME_PATTERN, tweet)

    for i in range(len(username_list)):
        username_list[i] = username_list[i][2:] # strip off delimiter and '@' from username
        # check if username is valid. 
        # if so, keep it in the list. 
        # if not, delete it.

    return username_list

def main():
    tweet = "Hello ^@Perforce! Hi?@Michael! This[@isatest. Does this )@pass?"
    print find_usernames(tweet)

if __name__ == "__main__":
    main()
