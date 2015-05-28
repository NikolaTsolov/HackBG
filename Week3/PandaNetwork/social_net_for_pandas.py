import re
import json


class WrongEmail(Exception):
    pass

class PandaAlreadyThere(Exception):
    pass

class PandaAlreadyFriends(Exception):
    pass

class Panda:

    def check_email(self, email):
        regex = re.match(r"[^@]+@[^@]+\.[^@]+", email) != None
        return regex

    def __init__(self, name, email, gender):
        self.__name = name
        self.__gender = gender
        if self.check_email(email):
            self.__email = email
        else:
            raise WrongEmail


    def name(self):
        return self.__name

    def email(self):
        return self.__email

    def gender(self):
        return self.__gender

    def isMale(self):
        return self.__gender == "male"

    def isFemale(self):
        return self.__gender == "female"

    def __str__(self):
        return "I am {}, I am {} and my email is {}".format(self.__name, self.__gender, self.__email)

    def __eq__(self, other):
        equal_names = self.__name == other.__name
        equal_emails = self.__email == other.__email
        equal_genders = self.__gender == other.__gender
        return equal_names and equal_emails and equal_genders

    def __repr__(self):
        return "Panda('{}', '{}', '{}')".format(self.__name,self.__email, self.__gender)

    def __hash__(self):
        return hash(self.__str__())

class PandaSocialNetwork:
    def __init__(self):
        self.pandas = {}

    def add_panda(self, panda):
        if panda in self.pandas:
            raise PandaAlreadyThere
        self.pandas[panda] = []

    def has_panda(self, panda):
        if panda in self.pandas:
            return True
        return False

    def make_friends(self, panda1, panda2):
        if not self.has_panda(panda1):
            self.add_panda(panda1)
        if not self.has_panda(panda2):
            self.add_panda(panda2)

        if panda1 not in self.pandas[panda2]:
            self.pandas[panda1].append(panda2)
            self.pandas[panda2].append(panda1)
        else:
            raise PandaAlreadyFriends

    def friends_of(self, panda):
        if self.has_panda(panda):
            return self.pandas[panda]
        else:
            return False

    def are_friends(self, panda1, panda2):
        if self.has_panda(panda1) and self.has_panda(panda2):
            if panda1 in self.pandas[panda2]:
                return True
        else:
            return False

    def conection_level(self, panda1, panda2):
        if self.has_panda(panda1) and self.has_panda(panda2):
            table = self.bfs(panda1)
            if panda2 in table:
                return table[panda2]
            else:
                return -1
        else:
            return False

    def are_connected(self, panda1, panda2):
        if self.has_panda(panda1) and self.has_panda(panda2):
            if self.conection_level(panda1, panda2) > 0:
                return True
        else:
            return False

    def how_many_gender_in_network(self, level, panda1, gender):
        count = 0
        if self.has_panda(panda1):
            table = self.bfs(panda1)
            for panda in table:
                if table[panda] > 0 and table[panda] <= level and panda.gender() == gender:
                    count += 1
            return count
        else:
            return False

    def __repr__(self):
        for_save = {}
        for panda in self.pandas:
            friends = [repr(panda_friend) for panda_friend in self.pandas[panda]]
            for_save[repr(panda)] = friends

        return json.dumps(for_save, indent=True)

    def save(self, filename):
        with open(filename, "w") as f:
            f.write(self.__repr__())

    @staticmethod
    def load(filename):
        network = PandaSocialNetwork()
        with open(filename, "r") as f:
            contents = f.read()
            json_network = json.loads(contents)
            for panda in json_network:
                for friend in json_network[panda]:
                    panda1 = eval(panda)
                    panda2 = eval(friend)
                    if not network.are_friends(panda1, panda2):
                        network.make_friends(panda1, panda2)
        return network



    def bfs(self, start):
        visited = set()
        queue = []
        panda_level = {}
        queue.append((start, 0))
        visited.add(start)

        while len(queue) != 0:
            current_data = queue.pop(0)
            current_node = current_data[0]
            current_level = current_data[1]
            panda_level[current_node] = current_level
            for neighbour in self.pandas[current_node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append((neighbour, current_level + 1))

        return panda_level




if __name__ == '__main__':
    main()

