from instaloader import *
from credentials import *
class Controller:
    def __init__(self):
        self.loader = Instaloader()
        self.loader.login(user,password)

    def getUnfollowers(self, username):
        profile = Profile.from_username(self.loader.context, username)
        followers = set(profile.get_followers())
        followees = set(profile.get_followees())
        return followees-followers

