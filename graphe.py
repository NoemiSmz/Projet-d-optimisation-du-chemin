import networkx as nx
import matplotlib.pyplot as plt
from scipy.optimize import linear_sum_assignment
G= nx.DiGraph()

main_axes = [
    ("Port-Louis", "Anse-Bertrand", 9),
    ("Anse-Bertrand", "Port-Louis", 9),
    ("Port-Louis", "Petit-Canal",  9),
    ("Petit-Canal","Port-Louis", 9),
    ("Petit-Canal", "Anse-Bertrand", 17),
    ("Anse-Bertrand", "Petit-Canal", 17),
    ("Petit-Canal", "Morne à l'eau", 8),
    ("Morne à l'eau", "Petit-Canal", 8),
    ("Morne à l'eau", "Moule",13),
    ("Moule", "Morne à l'eau", 13),
    ("Moule", "Saint-François", 14),
    ("Saint-François", "Moule", 14),
    ("Saint-François", "Sainte-Anne", 15),
    ("Sainte-Anne", "Saint-François", 15),
    ("Sainte-Anne", "Gosier",  14),
    ("Gosier", "Sainte-Anne", 14),
    ("Gosier", "Pointe à pitre", 9),
    ("Pointe à pitre", "Gosier", 9),
    ("Pointe à pitre", "Abymes", 5),
    ("Abymes", "Pointe à pitre", 5),
    ("Abymes", "Baie-Mahault", 12),
    ("Baie-Mahault","Abymes", 12),
    ("Pointe à pitre", "Baie-Mahault", 9),
    ("Baie-Mahault", "Pointe à pitre", 9),
    ("Baie-Mahault", "Petit Bourg", 10),
    ("Baie-Mahault", "Petit Bourg", 10),
    ("Petit Bourg", "Goyave", 8),
    ("Goyave", "Petit Bourg", 8),
    ("Goyave", "Capesterre", 12),
    ("Capesterre", "Goyave", 12),
    ("Capesterre", "Trois rivière", 13),
    ("Trois rivière","Capesterre", 13 ),
    ("Trois rivière", "Gourbeyre", 8),
    ("Gourbeyre", "Trois rivière", 8 ),
    ("Gourbeyre", "Basse Terre", 5),
    ("Basse Terre", "Gourbeyre", 5),
    ("Basse Terre", "Bailllif", 4),
    ("Bailllif", "Basse Terre", 4),
    ("Bailllif", "Vieux Habitants", 7),
    ("Vieux Habitants", "Bouillante", 11),
    ("Bouillante", "Vieux Habitants", 11),
    ("Bouillante", "Pointe Noire", 16),
    ("Pointe Noire", "Bouillante", 16),
    ("Pointe Noire", "Deshaies",  14),
    ("Deshaies", "Pointe Noire", 14),
    ("Deshaies", "Sainte rose", 17),
    ("Sainte rose", "Deshaies", 17),
    ("Lamentin", "Sainte rose",  12),
    ("Lamentin", "Baie-Mahault", 7),
    ("Lamentin", "Baie-Mahault", 7),
    ("Anse-Bertrand", "Moule", 32),
    ("Moule", "Anse-Bertrand", 32),
    ("Saint-François", "Moule", 17),
    ("Moule", "Saint-François", 17),
    ("Saint-François", "Gosier", 31),
    ("Gosier", "Saint-François", 31),
    ("Moule", "Sainte-Anne", 29),
    ("Sainte-Anne", "Moule", 29),
    ("Sainte-Anne", "Morne à l'eau",  33),
    ("Morne à l'eau", "Sainte-Anne", 33),
    ("Sainte-anne", "Abymes", 24),
    ("Abymes", "Sainte-anne", 24),
    ("Abymes", "Gosier", 12),
    ("Gosier", "Abymes", 12),
    ("Gosier", "Pointe à pitre", 12),
    ("Pointe à pitre", "Gosier", 12),
    ("Lamentin", "Petit Bourg", 14),
    ("Petit Bourg", "Lamentin", 14),
    ("Deshaies", "Sainte Rose", 22),
    ("Sainte Rose", "Deshaies", 22),
    ("Vieux Habitants", "Baillif", 13),
    ("Baillif", "Vieux Habitants", 13),
    ("Saint Claude", "Basse Terre", 6),
    ("Basse Terre", "Saint Claude", 6),
    ("Saint Claude", "Trois Rivière", 6),
    ("Trois Rivière", "Saint Claude", 6),
    ("Trois Rivière", "Vieux Fort", 13),
    ("Vieux Fort", "Trois Rivière", 13),
    ("Basse Terre", "Vieux Fort", 7),
    ("Vieux Fort", "Basse Terre", 7),
    ("Gourbeyre", "Vieux Fort", 10),
    ("Vieux Fort", "Gourbeyre", 10),
    ("Baillif", "Vieux Fort", 10),
    ("Vieux Fort", "Baillif", 10)

]


# Ajout des routes au graphe
G.add_weighted_edges_from(main_axes)

# Partie pour demander à l'utilisateur de saisir les informations
start_node = input("Entrez le sommet de départ : ")

destinations = []
for i in range(6):  # Changez ici pour le nombre de sommets d'arrivée que vous souhaitez
    destination = input(f"Entrez la destination {i+1} : ")
    destinations.append(destination)

# Vérification que les sommets saisis sont présents dans le graphe
if start_node not in G.nodes or any(dest not in G.nodes for dest in destinations):
    print("Certains sommets saisis ne sont pas présents dans le graphe.")
else:
    # Ajout du sommet de départ à la liste des destinations pour former un cycle
    destinations.insert(0, start_node)

    # Utiliser la fonction all_simple_paths pour trouver tous les chemins possibles
    all_paths = list(nx.all_simple_paths(G, source=start_node, target=destinations[-1]))

    # Calculer le poids total de chaque chemin et trouver le chemin de poids minimum
    min_weight = float('inf')
    min_path = None

    for path in all_paths:
        weight = sum(G[path[i]][path[i + 1]]['weight'] for i in range(len(path) - 1))
        if weight < min_weight:
            min_weight = weight
            min_path = path

    # Dessiner le graphe avec le chemin de poids minimum en rouge
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=8, arrowsize=10, edge_color='gray', font_color='black', width=1)

    edges = list(zip(min_path, min_path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='red', width=2)

    # Dessiner les sommets en rouge
    nx.draw_networkx_nodes(G, pos, nodelist=min_path, node_color='red', node_size=700)

    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Afficher le poids total du chemin
    print(f"Poids total du chemin : {min_weight}")

    plt.show()