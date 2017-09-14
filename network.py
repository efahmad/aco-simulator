class Node(object):
    def __init__(self, x, y, num_users):
        self.x = x
        self.y = y
        self.num_users = num_users


class Network(object):
    def __init__(self, left_boundary=0, right_boundary=1000, bottom_boundary=0, top_boundary=1000,
                 adj_distance=250, num_nodes=100):
        self.left_boundary = left_boundary
        self.right_boundary = right_boundary
        self.bottom_boundary = bottom_boundary
        self.top_boundary = top_boundary
        self.adj_distance = adj_distance
        self.num_nodes = num_nodes
