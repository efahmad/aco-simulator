import numpy as np


class Node(object):
    def __init__(self, x, y, num_users):
        self.x = x
        self.y = y
        self.num_users = num_users


class Network(object):
    def __init__(self, left_boundary=0.0, right_boundary=1000.0, bottom_boundary=0.0, top_boundary=1000.0,
                 adj_distance=250, num_nodes=100, num_sources=1, num_destinations=3):
        self.left_boundary = left_boundary
        self.right_boundary = right_boundary
        self.bottom_boundary = bottom_boundary
        self.top_boundary = top_boundary
        self.adj_distance = adj_distance
        self.num_nodes = num_nodes
        self.num_sources = num_sources
        self.num_destinations = num_destinations
        # ***************************************** #
        self.nodes = []
        self.source_nodes = []
        self.destination_nodes = []
        # Create the network
        self.create()

    def create(self):
        # Get 100 random x,y between boundaries
        x_array = np.random.uniform(low=self.left_boundary, high=self.right_boundary, size=self.num_nodes)
        y_array = np.random.uniform(low=self.bottom_boundary, high=self.top_boundary, size=self.num_nodes)
        for x, y in zip(x_array, y_array):
            self.nodes.append(Node(x, y, np.random.randint(low=1, high=20)))
        # Convert to numpy array
        self.nodes = np.array(self.nodes)
        # Randomly select source and destination nodes
        self.source_nodes = self.nodes[np.random.randint(low=0, high=self.num_nodes, size=self.num_sources)]
        self.destination_nodes = self.nodes[np.random.randint(low=0, high=self.num_nodes, size=self.num_destinations)]
