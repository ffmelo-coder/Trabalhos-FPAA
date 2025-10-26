# -*- coding: utf-8 -*-


def hamiltonian_path(graph, path, visited, n):
    if len(path) == n:
        return True
    current = path[-1]
    for neighbor in graph[current]:
        if neighbor not in visited:
            path.append(neighbor)
            visited.add(neighbor)
            if hamiltonian_path(graph, path, visited, n):
                return True
            path.pop()
            visited.remove(neighbor)
    return False


def solve_hamiltonian():
    graphs = [
        {
            "name": "Quadrado com diagonal",
            "graph": {0: [1, 2, 3], 1: [0, 2], 2: [0, 1, 3], 3: [0, 2]},
        },
        {"name": "Triângulo completo K3", "graph": {0: [1, 2], 1: [0, 2], 2: [0, 1]}},
        {
            "name": "Estrela (centro + 3 pontas)",
            "graph": {0: [1, 2, 3], 1: [0], 2: [0], 3: [0]},
        },
        {
            "name": "Caminho linear 0-1-2-3-4",
            "graph": {0: [1], 1: [0, 2], 2: [1, 3], 3: [2, 4], 4: [3]},
        },
        {
            "name": "Pentágono (ciclo C5)",
            "graph": {0: [1, 4], 1: [0, 2], 2: [1, 3], 3: [2, 4], 4: [3, 0]},
        },
        {
            "name": "Grafo completo K4",
            "graph": {0: [1, 2, 3], 1: [0, 2, 3], 2: [0, 1, 3], 3: [0, 1, 2]},
        },
        {"name": "Grafo desconectado", "graph": {0: [1], 1: [0], 2: [3], 3: [2]}},
        {
            "name": "Roda (centro + ciclo)",
            "graph": {
                0: [1, 2, 3, 4],
                1: [0, 2],
                2: [0, 1, 3],
                3: [0, 2, 4],
                4: [0, 3, 1],
            },
        },
        {
            "name": "Hexágono (ciclo C6)",
            "graph": {0: [1, 5], 1: [0, 2], 2: [1, 3], 3: [2, 4], 4: [3, 5], 5: [4, 0]},
        },
        {
            "name": "Grafo completo K5",
            "graph": {
                0: [1, 2, 3, 4],
                1: [0, 2, 3, 4],
                2: [0, 1, 3, 4],
                3: [0, 1, 2, 4],
                4: [0, 1, 2, 3],
            },
        },
        {
            "name": "Grade 2x3",
            "graph": {
                0: [1, 3],
                1: [0, 2, 4],
                2: [1, 5],
                3: [0, 4],
                4: [1, 3, 5],
                5: [2, 4],
            },
        },
        {
            "name": "Árvore binária",
            "graph": {
                0: [1, 2],
                1: [0, 3, 4],
                2: [0, 5, 6],
                3: [1],
                4: [1],
                5: [2],
                6: [2],
            },
        },
        {
            "name": "Grafo zigzag",
            "graph": {0: [3], 1: [4], 2: [5], 3: [0, 4], 4: [1, 3, 5], 5: [2, 4]},
        },
        {
            "name": "Petersen simplificado",
            "graph": {0: [1, 4], 1: [0, 2], 2: [1, 3], 3: [2, 4], 4: [0, 3, 5], 5: [4]},
        },
        {
            "name": "Estrela dupla conectada",
            "graph": {0: [1, 2], 1: [0, 3], 2: [0, 4], 3: [1, 4], 4: [2, 3]},
        },
        {
            "name": "Grafo borboleta",
            "graph": {
                0: [1, 2, 4],
                1: [0, 2],
                2: [0, 1, 3, 4],
                3: [2, 4],
                4: [0, 2, 3],
            },
        },
        {
            "name": "Prisma triangular",
            "graph": {
                0: [1, 2, 3],
                1: [0, 2, 4],
                2: [0, 1, 5],
                3: [0, 4, 5],
                4: [1, 3, 5],
                5: [2, 3, 4],
            },
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
        },
        {
            "name": "Ordem reversa",
            "graph": {
                8: [3, 6],
                6: [8, 1, 4],
                4: [6, 2],
                2: [4, 0, 3],
                3: [8, 2],
                1: [6],
                0: [2],
            },
        },
        {
            "name": "Intercalado complexo",
            "graph": {
                9: [3, 7],
                3: [9, 1, 5],
                1: [3, 8],
                8: [1, 5, 2],
                5: [3, 8, 7],
                7: [9, 5, 2],
                2: [8, 7],
            },
        },
        {
            "name": "Zigzag numerado",
            "graph": {
                10: [4, 7],
                4: [10, 1, 8],
                1: [4, 6],
                6: [1, 3, 8],
                3: [6, 7],
                7: [10, 3, 8],
                8: [4, 6, 7],
            },
        },
    ]

    for i, test in enumerate(graphs, 1):
        print(f"\n{i}. Testando: {test['name']}")
        print(f"   Vértices: {list(test['graph'].keys())} (n={len(test['graph'])})")

        found = False

        for start in test["graph"]:
            path = [start]
            visited = {start}

            if hamiltonian_path(test["graph"], path, visited, len(test["graph"])):
                print(f"   [OK] Caminho encontrado: {' -> '.join(map(str, path))}")
                found = True
                break

        if not found:
            print(f"   [X] Caminho não encontrado")


if __name__ == "__main__":
    solve_hamiltonian()
