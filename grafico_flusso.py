import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

# Definizione dei nodi
nodi = ["Inizio", "Analisi Indizi", "Stallo", "Allucinazione", "Convergenza", "Risoluzione"]
G.add_nodes_from(nodi)

G.add_edges_from([
    ("Inizio", "Analisi Indizi"),
    ("Analisi Indizi", "Stallo"),
    ("Stallo", "Allucinazione"),
    ("Allucinazione", "Convergenza"),
    ("Convergenza", "Risoluzione")
])

# FISSAGGIAMO LE POSIZIONI (Manuale: x, y)
pos = {
    "Inizio": (0, 0),
    "Analisi Indizi": (2, 0),
    "Stallo": (4, 0),
    "Allucinazione": (6, 0),
    "Convergenza": (8, 0),
    "Risoluzione": (10, 0)
}

plt.figure(figsize=(14, 4)) # Formato più allungato per il flusso

# Disegno personalizzato (più pulito)
nx.draw(G, pos, with_labels=True, node_color='#ADD8E6', 
        node_size=4000, font_size=9, font_weight='bold', 
        arrows=True, arrowsize=20, edge_color='black', 
        width=2, node_shape='s') 

plt.title("Pipeline Decisionale Emergente", fontsize=16, fontweight='bold')
plt.margins(0.2) # Aggiunge spazio ai bordi per non tagliare le scritte
plt.tight_layout()

# Salvataggio
plt.savefig('flusso_decisionale_finale.png', dpi=300)
print("Creato 'flusso_decisionale_finale.png' - ora sarà perfetto.")
plt.show()