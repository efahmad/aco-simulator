import numpy as np
import random


class Edge(object):
    def __init__(self, length, from_node, to_node):
        self.length = length
        self.from_node = from_node
        self.to_node = to_node


class Node(object):
    def __init__(self, location, num_users):
        self.location = location
        self.num_users = num_users


class Network(object):
    def __init__(self, left_boundary=0.0, right_boundary=1000.0, bottom_boundary=0.0, top_boundary=1000.0,
                 max_edge_length=250.0, num_nodes=100, num_sources=1, num_destinations=3):
        self.left_boundary = left_boundary
        self.right_boundary = right_boundary
        self.bottom_boundary = bottom_boundary
        self.top_boundary = top_boundary
        self.max_edge_length = max_edge_length
        self.num_nodes = num_nodes
        self.num_sources = num_sources
        self.num_destinations = num_destinations
        # ***************************************** #
        self.nodes = []
        self.edges = []
        self.unique_edges = []
        self.source_nodes = []
        self.destination_nodes = []
        # Create the network
        self.create()

    def create(self):
        # Get 100 random x,y between boundaries
        x_array = np.random.uniform(low=self.left_boundary, high=self.right_boundary, size=self.num_nodes)
        y_array = np.random.uniform(low=self.bottom_boundary, high=self.top_boundary, size=self.num_nodes)
        for x, y in zip(x_array, y_array):
            self.nodes.append(Node(np.array([x, y]), np.random.randint(low=1, high=20)))

        # Select source & destination nodes
        source_range = (self.left_boundary + self.right_boundary / 100,
                        self.right_boundary - self.right_boundary / 100)
        source_node_candidates = [node for node in self.nodes
                                  if node.location[0] < source_range[0] or node.location[0] > source_range[1]]
        self.source_nodes = random.sample(source_node_candidates, self.num_sources)
        self.destination_nodes = random.sample([node for node in self.nodes if node not in self.source_nodes],
                                               self.num_destinations)
        # Create edges between nodes
        self.init_edges()

    def init_edges(self):
        """Find edges between nodes."""
        for from_index, from_node in enumerate(self.nodes):
            for to_index, to_node in enumerate(self.nodes):
                distance = np.linalg.norm(from_node.location - to_node.location)
                if from_index != to_index and distance <= self.max_edge_length:
                    self.edges.append(Edge(distance, from_node, to_node))
                    if from_index < to_index:
                        self.unique_edges.append(self.edges[-1])