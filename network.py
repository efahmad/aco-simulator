class Node(object):
    def __init__(self, name, num_users, adjacent_nodes):
        self.name = name
        self.num_users = num_users
        self.adjacent_nodes = adjacent_nodes