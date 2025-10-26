try:
    import networkx as nx
    import matplotlib.pyplot as plt
    from main import hamiltonian_path
except ImportError as e:
    print(f"Erro: {e}")
    print("Para usar a visualização, instale as dependências:")
    print("pip install networkx matplotlib")
    exit(1)


def encontrar_caminho_hamiltoniano(grafo_dict):
    n = len(grafo_dict)
    for start in grafo_dict:
        path = [start]
        visited = {start}
        if hamiltonian_path(grafo_dict, path, visited, n):
            return path
    return None


def converter_para_networkx(grafo_dict):
    G = nx.Graph()
    for vertice in grafo_dict.keys():
        G.add_node(vertice)
    arestas_adicionadas = set()
    for vertice, vizinhos in grafo_dict.items():
        for vizinho in vizinhos:
            aresta = tuple(sorted([vertice, vizinho]))
            if aresta not in arestas_adicionadas:
                G.add_edge(vertice, vizinho)
                arestas_adicionadas.add(aresta)
    return G


def visualizar_grafo_com_caminho(
    grafo_dict, caminho=None, titulo="Grafo", salvar_como=None
):
    G = converter_para_networkx(grafo_dict)
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G, seed=42, k=2, iterations=50)
    nx.draw_networkx_edges(G, pos, edge_color="lightgray", width=2, alpha=0.6)
    if caminho and len(caminho) > 1:
        arestas_caminho = [
            (caminho[i], caminho[i + 1]) for i in range(len(caminho) - 1)
        ]
        nx.draw_networkx_edges(
            G, pos, edgelist=arestas_caminho, edge_color="red", width=4, alpha=0.8
        )
    nx.draw_networkx_nodes(G, pos, node_color="lightblue", node_size=800, alpha=0.9)
    nx.draw_networkx_labels(G, pos, font_size=16, font_weight="bold")
    plt.title(titulo, fontsize=16, fontweight="bold", pad=20)
    plt.axis("off")
    if caminho:
        caminho_texto = " → ".join(map(str, caminho))
        plt.figtext(
            0.5,
            0.02,
            f"Caminho Hamiltoniano: {caminho_texto}",
            ha="center",
            fontsize=12,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="lightyellow"),
        )
    else:
        plt.figtext(
            0.5,
            0.02,
            "Nenhum caminho hamiltoniano encontrado",
            ha="center",
            fontsize=12,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="lightcoral"),
        )
    if salvar_como:
        plt.savefig(salvar_como, dpi=300, bbox_inches="tight")
        print(f"Gráfico salvo como: {salvar_como}")
    plt.tight_layout()
    plt.show()


def demonstrar_visualizacoes():
    import os

    if not os.path.exists("assets"):
        os.makedirs("assets")
    print("=" * 60)
    print("VISUALIZAÇÃO DE CAMINHOS HAMILTONIANOS")
    print("=" * 60)
    grafos_demo = [
        {
            "name": "Quadrado com diagonal",
            "graph": {0: [1, 2, 3], 1: [0, 2], 2: [0, 1, 3], 3: [0, 2]},
            "filename": "quadrado_diagonal.png",
        },
        {
            "name": "Estrela",
            "graph": {0: [1, 2, 3], 1: [0], 2: [0], 3: [0]},
            "filename": "estrela_sem_caminho.png",
        },
        {
            "name": "Saltos obrigatórios",
            "graph": {
                9: [2, 5],
                2: [9, 7, 1],
                7: [2, 0],
                0: [7, 5],
                5: [0, 9, 1],
                1: [2, 5],
            },
            "filename": "saltos_obrigatorios.png",
        },
        {
            "name": "Cubo modificado",
            "graph": {
                0: [1, 2, 6],
                1: [0, 3, 7],
                2: [0, 4],
                3: [1, 5],
                4: [2, 6],
                5: [3, 7],
                6: [0, 4],
                7: [1, 5],
            },
            "filename": "cubo_modificado.png",
        },
    ]
    for i, grafo_info in enumerate(grafos_demo, 1):
        print(f"\n{i}. Visualizando: {grafo_info['name']}...")
        caminho = encontrar_caminho_hamiltoniano(grafo_info["graph"])
        visualizar_grafo_com_caminho(
            grafo_info["graph"],
            caminho,
            grafo_info["name"],
            f"assets/{grafo_info['filename']}",
        )
    print("\n" + "=" * 60)
    print("Todas as visualizações foram salvas na pasta 'assets/'")
    print("=" * 60)


if __name__ == "__main__":
    demonstrar_visualizacoes()
