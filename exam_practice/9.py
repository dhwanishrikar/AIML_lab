import networkx as nx
import matplotlib.pyplot as plt

# Initialize a Directed Graph
G = nx.DiGraph()

# 1. Define nodes
enc = ["Enc1", "Enc2", "Enc3", "Enc4"]
dec = ["Dec1", "Dec2", "Dec3", "Dec4"]

G.add_nodes_from(enc + dec)

# 2. Sequential edges
for i in range(3):
    G.add_edge(enc[i], enc[i + 1])
    G.add_edge(dec[i], dec[i + 1])

# 3. Cross-Attention edges
for e in enc:
    for d in dec:
        G.add_edge(e, d)

# 4. Positions
pos = {n: (0, 4 - i) for i, n in enumerate(enc)}
pos.update({n: (2, 4 - i) for i, n in enumerate(dec)})

# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

nx.draw(
    G,
    pos,
    ax=ax,
    with_labels=True,
    node_size=2000,
    node_color="skyblue",
    font_weight="bold",
    arrows=True,
    connectionstyle="arc3, rad=0.1"
)

plt.title("Transformer Architecture: Encoder-Decoder Attention Flow")
plt.show()
