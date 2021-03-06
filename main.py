import itertools

from network import Network
import matplotlib.pyplot as plt


def main():
    network = Network()

    # Print network info
    print("Source Nodes:")
    for node in network.source_nodes:
        print(node)
    print("-" * 50)
    print("Destination Nodes:")
    for node in network.destination_nodes:
        print(node)
    print("-" * 50)
    print("Pheromones:\n")
    network.print_pheromones()

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
