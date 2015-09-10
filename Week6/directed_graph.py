import re

class NotInRange(Exception):
    pass

class MissingNode(Exception):
    pass

class DirectedGraph:
    def __init__(self):
        self.__nodes = {}


    def add_edge(self, node_a, node_b):
        if node_a in self.__nodes:
            if node_b in self.__nodes[node_a]:
                return "{} Already In The List".format(node_b)
            else:
                self.__nodes[node_a].append(node_b)
        else:
            self.__nodes[node_a] = [node_b]


    def get_neighbours_for(self, node):
        if node in self.__nodes:
            return self.__nodes[node]
        else:
            raise MissingNode

    def path_between(self, node_a, node_b):
        visited = set()
        queue = []
        queue.append((node_a, 0))
        visited.add(node_a)

        while len(queue) != 0:
            current_data = queue.pop(0)
            current_node = current_data[0]
            current_level = current_data[1]
            if current_level > 4:
                raise NotInRange
            if current_node in self.__nodes:
                for neighbour in self.__nodes[current_node]:
                    if neighbour == node_b:
                        return True
                    elif neighbour not in visited:
                        visited.add(neighbour)
                        queue.append((neighbour, current_level + 1))
        return False

def main():
    pass

if __name__ == '__main__':
    main()
