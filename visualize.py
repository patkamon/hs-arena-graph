import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(graph, highlight_nodes=None):
    G = nx.Graph()

    # Add nodes and edges
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    # Default: no highlight
    highlight_nodes = set(highlight_nodes or [])

    # Layout
    pos = nx.spring_layout(G, seed=42)

    # Prepare node colors
    node_colors = []
    for node in G.nodes():
        if node in highlight_nodes:
            node_colors.append("red")
        else:
            node_colors.append("lightblue")

    # Draw the graph
    plt.figure(figsize=(16, 12))
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=300)
    nx.draw_networkx_edges(G, pos, edge_color='gray', width=1)
    nx.draw_networkx_labels(G, pos, font_size=8)

    plt.title("Card Connection Graph (Highlighted Nodes in Red)", fontsize=16)
    plt.axis("off")
    plt.show()
