import numpy as np
import random


class Edge(object):
    def __init__(self, length, from_node, to_node, pheromone=0):
        self.length = length
        self.from_node = from_node
        self.to_node = to_node
        self.pheromone = pheromone

    def __str__(self):
        return "From {0} To {1}".format(self.from_node, self.to_node)


class Node(object):
    def __init__(self, name, location, num_users):
        self.location = location
        self.num_users = num_users
        self.name = name

    def __str__(self):
        return self.name


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
        counter = 0
        for x, y in zip(x_array, y_array):
            counter += 1
            name = "Node_{0}".format(counter)
            self.nodes.append(Node(name, np.array([x, y]), np.random.randint(low=1, high=20)))

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

        # Init pheromone for each edge
        self.init_pheromones()

    def init_edges(self):
        """Find edges between nodes."""
        for index, from_node in enumerate(self.nodes):
            for to_node in self.nodes[index + 1:]:
                distance = np.linalg.norm(from_node.location - to_node.location)
                if distance <= self.max_edge_length:
                    self.edges.append(Edge(distance, from_node, to_node))
                    self.unique_edges.append(self.edges[-1])
                    self.edges.append(Edge(distance, to_node, from_node))

    def get_node_neighbors(self, node):
        return [edge.to_node for edge in self.get_node_edges(node)]

    def get_node_edges(self, node):
        return [edge for edge in self.edges if edge.from_node is node]

    def init_pheromones(self):
        for node in self.nodes:
            edges = self.get_node_edges(node)
            Ni = len(edges)
            sigma_Wi = sum(edge.to_node.num_users for edge in edges
                           if edge.to_node in self.destination_nodes)
            for edge in edges:
                self.init_edge_pheromone(edge, Ni, sigma_Wi)

    def init_edge_pheromone(self, edge, Ni, sigma_Wi):
        Wi = edge.to_node.num_users
        if sigma_Wi > 0 and edge.to_node in self.destination_nodes:
            edge.pheromone = (Ni * (Wi / sigma_Wi) + 1) / (2 * Ni)
        elif sigma_Wi > 0:
            edge.pheromone = 1 / (2 * Ni)
        else:
            edge.pheromone = 1 / Ni

    def print_pheromones(self):
        for node in self.nodes:
            for edge in self.get_node_edges(node):
                print("{0}: {1}".format(edge, edge.pheromone))
            print()
