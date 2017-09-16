import itertools

from network import Network
import matplotlib.pyplot as plt


def main():
    network = Network()

    for node in network.nodes:
        for edge in network.get_node_edges(node):
            print(edge.pheromone)
        print("-" * 50)

    # Draw edges
    for edge in network.unique_edges:
        plt.plot([edge.from_node.location[0], edge.to_node.location[0]],
                 [edge.from_node.location[1], edge.to_node.location[1]], color='black', linewidth=1)

    # Draw all nodes
    plt.scatter([node.location[0] for node in network.nodes],
                [node.location[1] for node in network.nodes], color='black', linewidths=2)

    # Draw source nodes
    plt.scatter([node.location[0] for node in network.source_nodes],
                [node.location[1] for node in network.source_nodes], color='red', linewidths=6)

    # Draw destination nodes
    plt.scatter([node.location[0] for node in network.destination_nodes],
                [node.location[1] for node in network.destination_nodes], color='blue', linewidths=6)

    plt.show()


if __name__ == '__main__':
    main()
