import requests
import json
from directed_graph import DirectedGraph

class WhoFollowsYouBack:

    NIKOLA = "NikolaTsolov"
    SASHO = "AlexanderTankov"

    def __init__(self):
        self.current_lvl = []
        self.following = []
        self.followers = []
        self.graph = DirectedGraph()

    def requester(self, user, follow):
        r = requests.get('https://api.github.com/users/{}/{}?client_id=84a513cf63beb6315ac8&client_secret=5619ee8d52128ee89099690e250732289e1edef5'.format(user, follow))
        return r.text

    def the_talk(self, lvl, user, follow):
        self.add_followers_ing(user, follow)
        checked = []
        while lvl != 1:
            current_lvl = [follower for follower in self.following]
            self.following = []
            for follower in current_lvl:
                if follower not in checked:
                    self.add_followers_ing(follower, follow)
                    checked.append(follower)
            lvl -= 1
        self.following = []


    def add_followers_ing(self, user, follow):
        t_json = self.requester(user, follow)
        into_json = json.loads(t_json)
        for follower in into_json:
            if follow == "following":
                self.following.append(follower["login"])
                self.graph.add_edge(user, follower["login"])
            else:
                self.graph.add_edge(follower["login"], user)
                self.followers.append(follower["login"])

    def show_followers_of(self, user):
        print(self.json_reader(user))

    def do_you_follow(self, user):
        self.the_talk(1, self.NIKOLA, "following")
        return self.graph.path_between(self.NIKOLA, user)

    def do_you_follow_indireclty(self, user):
        self.the_talk(3, self.NIKOLA, "following")
        return self.graph.path_between(self.NIKOLA, user)

    def does_he_she_follows(self, user):
        self.the_talk(1, user, "following")
        return self.graph.path_between(user, self.SASHO)

    def does_he_she_follows_indirectly(self, user):
        self.the_talk(3, user, "following")
        return self.graph.path_between(user, self.SASHO)

    def who_followes_you_back(self):
        follow_back = []
        self.the_talk(1, self.SASHO, "followers")
        self.the_talk(3, self.SASHO, "following")
        for follower in self.followers:
            if self.graph.path_between(self.SASHO, follower):
                follow_back.append(follower)
        self.followers = []
        return follow_back



def main():
    hub = WhoFollowsYouBack()
    #print(hub.do_you_follow("RadoRado"))
    #print(hub.do_you_follow_indireclty("AntonioFilipov"))
    #print(hub.does_he_she_follows("AntonioFilipov"))
    #print(hub.does_he_she_follows_indirectly("pepincho"))
    #print(hub.who_followes_you_back())

if __name__ == '__main__':
    main()
