from network import Network
import matplotlib.pyplot as plt


def main():
    network = Network()
    plt.scatter([node.x for node in network.nodes], [node.y for node in network.nodes])
    plt.scatter([node.x for node in network.source_nodes], [node.y for node in network.source_nodes])
    plt.scatter([node.x for node in network.destination_nodes], [node.y for node in network.destination_nodes])
    plt.show()


if __name__ == '__main__':
    main()
