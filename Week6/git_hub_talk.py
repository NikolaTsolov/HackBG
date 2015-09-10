import requests
import json
from directed_graph import DirectedGraph

class WhoFollowsYouBack:

    NIKOLA = "NikolaTsolov"

    def __init__(self):
        self.current_lvl = []
        self.followers = []
        self.graph = DirectedGraph()

    def requester(self, user, follow):
        r = requests.get('https://api.github.com/users/{}/{}?client_id=84a513cf63beb6315ac8&client_secret=5619ee8d52128ee89099690e250732289e1edef5'.format(user, follow))
        print(r.status_code)
        return r.text

    def the_talk(self, lvl, user, follow):
        self.json_reader(user, follow)
        checked = []
        while lvl != 1:
            current_lvl = [follower for follower in self.followers]
            self.followers = []
            for follower in current_lvl:
                if follower not in checked:
                    self.json_reader(follower, follow)
                    checked.append(follower)
                    print(follower)
            lvl -= 1
        self.followers = []


    def json_reader(self, user, follow):
        t_json = self.requester(user, follow)
        into_json = json.loads(t_json)
        for follower in into_json:
            self.followers.append(follower["login"])
            self.graph.add_edge(user, follower["login"])

    def show_followers_of(self, user):
        print(self.json_reader(user))

    def do_you_follow(self, user):
        self.the_talk(1, self.NIKOLA, "following")
        return self.graph.path_between(self.NIKOLA, user)

    def do_you_follow_indireclty(self, user):
        self.the_talk(3, self.NIKOLA, "following")
        return self.graph.path_between(self.NIKOLA, user)

    def does_he_she_follows(user):
        pass

    def does_he_she_follows_indirectly(user):
        pass

    def who_followes_you_back():
        pass


def main():
    hub = WhoFollowsYouBack()
    print(hub.do_you_follow("RadoRado"))
    print(hub.do_you_follow_indireclty("AntonioFilipov"))

if __name__ == '__main__':
    main()
