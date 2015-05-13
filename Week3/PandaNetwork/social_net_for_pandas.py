import re


class WrongEmail(Exception):
    pass

class PandaAlreadyThere(Exception):
    pass

class Panda:

    def check_email(self, email):
        regex = re.match(r"[^@]+@[^@]+\.[^@]+", email) != None
        return regex

    def __init__(self, name, email, gender):
        self._name = name
        self._gender = gender
        if self.check_email(email):
            self._email = email
        else:
            raise WrongEmail


    def name(self):
        return self._name

    def email(self):
        return self._email

    def isMale(self):
        return self._gender == "male"

    def isFemale(self):
        return self._gender == "female"

    def __str__(self):
        string = "I am {}, I am {} and my email is {}".format(self._name, self._gender, self._email)
        return string

    def __eq__(self, other):
        equal_names = self._name == other._name
        equal_emails = self._email == other._email
        equal_genders = self._gender == other._gender
        return equal_names and equal_emails and equal_genders

    def __hash__(self):
        return hash(self._email)

class PandaSocialNetwork:
    def __init__(self):
        self._pandas = {}

    def add_panda(self, panda):
        if panda in self._pandas.keys():
            raise PandaAlreadyThere
        self._pandas[panda] = []

    def has_panda(self, panda):
        if panda in self._pandas.keys():
            return True
        return False

    def make_friends(self, friend1, friend2):
        if friend1 not in self._pandas.keys():
            self.add_panda(friend1)
        if friend2 not in self._pandas.keys():
            self.add_panda(friend2)

        self._pandas[friend1].append(friend2)
        self._pandas[friend2].append(friend1)

    def are_friends(self, panda1, panda2):
        return self.bfs(self._pandas)


    def bfs(graph):
        visited = set()
        queue = []
        path_to = {}
        queue.append(start)
        visited.add(start)
        path_to[start] = None
        found = False
        path_length = 0

        while len(queue) != 0:
            current_node = queue.pop(0)
            if current_node == end:
                found = True
                break
            for neighbour in graph[current_node]:
                if neighbour not in visited:
                    path_to[neighbour] = current_node
                    visited.add(neighbour)
                    queue.append(neighbour)
        if found:
            while path_to[end] is not None:
                path_length += 1
                end = path_to[end]
#       print(json.dumps(path_to, sort_keys=True, indent=4))
        return found



'''
graph = {
    "1": ["2", "3", "5", "10"],
    "2": ["4", "1"],
    "3": ["1", "6"],
    "4": ["2", "5", "6"],
    "5": ["4", "1"],
    "6": ["3", "4", "7"],
    "7": ["6", "8"],
    "8": ["7", "9"],
    "9": ["8", "10"],
    "10": ["9", "1"],
    "11": ["12"],
    "12": ["11"]
}

def bfs(graph, start, end):
    visited = set()
    queue = []
    #path to[x] = y
    #if we fgo to x trough y
    path_to = {}
    queue.append(start)
    visited.add(start)
    while len(queue) != 0:
        current_node = queue.pop(0)
        if current_node == end:
            found = True
            break

        for neighbour in graph:
            if neighbour not in visited:
                path_to[neighbour] = current_node
                visited.add(neighbour)
                queue.append(neighbour)
    if found:
        while path_to[end] is not None:
            path_length += 1
            end = path_to[end]
        path_length
    return path_to
'''

def main():
    network = PandaSocialNetwork()
    ivo = Panda("Ivo", "ivo@pandamail.com", "male")
    rado = Panda("Rado", "rado@pandamail.com", "male")
    tony = Panda("Tony", "tony@pandamail.com", "female")

    for panda in [ivo, rado, tony]:
        network.add_panda(panda)


if __name__ == '__main__':
    main()

