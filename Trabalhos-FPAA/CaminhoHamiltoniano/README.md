# Projeto CaminhoHamiltoniano

## Sobre o Projeto

O CaminhoHamiltoniano é um projeto educativo desenvolvido para demonstrar a busca de caminhos hamiltonianos em grafos utilizando a técnica de divisão e conquista.

O código é implementado em Python puro, sem dependências externas, de forma simples e fácil de entender.

Ele mostra como a abordagem recursiva pode ser utilizada para resolver problemas básicos de busca de caminhos em uma estrutura de grafo.

---

## Uso do GitHub Copilot

O GitHub Copilot foi utilizado apenas para auxiliar na construção dos grafos de teste presentes na função `solve_hamiltonian()`, formatação do arquivo README, sugestões de melhorias e entendimento das bibliotecas utilizadas.

---

## O que é o Algoritmo de Caminho Hamiltoniano?

O algoritmo de Caminho Hamiltoniano é um método recursivo para encontrar um caminho que visita cada vértice de um grafo exatamente uma vez.

Ele segue a ideia de divisão e conquista:

1. Divide o problema em subproblemas menores (explorar cada vizinho)
2. Calcula o resultado de cada subproblema recursivamente
3. Combina os resultados verificando se encontrou um caminho válido

### Passos principais:

- Caso base: quando o caminho tem todos os vértices, esse valor é o caminho hamiltoniano completo
- Caso recursivo: divide a busca explorando cada vizinho não visitado e combina os resultados
- Caso médio: varia significativamente dependendo da estrutura do grafo

---

## Sobre as bibliotecas utilizadas

### Bibliotecas no main.py

Nenhuma biblioteca externa foi utilizada. O código usa apenas funções nativas do Python (dicionários, listas, sets, chamadas recursivas e print).

### Bibliotecas no view.py

Para a visualização gráfica opcional, são utilizadas:

- NetworkX: Para manipulação e representação de grafos
- Matplotlib: Para criação e exportação das visualizações

---

## Por que implementar este algoritmo?

- Demonstração prática da técnica de backtracking.
- Introdução a problemas NP-Completos em teoria dos grafos.
- Base para algoritmos mais complexos como Caixeiro Viajante.
- Exercício de recursão e otimização de busca.
- Fundamental em áreas como roteamento de redes e planejamento de rotas.

---

## Ambiente virtual

Passo 1: Criar e ativar o ambiente virtual

```bash
python3 -m venv .venv
```

Ativar o ambiente virtual:

- macOS/Linux:

```bash
source .venv/bin/activate
```

- Windows:

```bash
.venv\Scripts\activate
```

Passo 2: Executar o script

```bash
python main.py
```

## Ponto Extra - Visualização

Para utilizar a visualização gráfica dos grafos e caminhos hamiltonianos:

### Passo 1: Instalar as bibliotecas necessárias

```bash
pip install networkx matplotlib
```

### Passo 2: Executar a visualização

```bash
python view.py
```

### Resultado da Visualização

O arquivo view.py irá:

1. Desenhar o grafo original: Inclui todos os nós e arestas com etiquetas para identificação
2. Destacar o Caminho Hamiltoniano: As arestas do caminho encontrado são destacadas em vermelho
3. Exportar imagens PNG: Salva automaticamente na pasta assets/

### Imagens Geradas

- assets/quadrado_diagonal.png: Grafo quadrado com diagonal - mostra caminho hamiltoniano encontrado
- assets/estrela_sem_caminho.png: Grafo estrela - demonstra caso sem caminho hamiltoniano
- assets/saltos_obrigatorios.png: Grafo com numeração não-sequencial - exemplo de caminho interessante
- assets/cubo_modificado.png: Grafo cubo modificado - exemplo de grafo 3D simplificado

Características das Imagens:

- Alta resolução: 300 DPI para qualidade de impressão
- Caminhos destacados: Arestas do caminho hamiltoniano em vermelho
- Numeração clara: Nós bem rotulados e legíveis
- Formato PNG: Compatível com documentos e apresentações

---

## Versão do Python

Este projeto foi desenvolvido em Python 3.12.3, mas funciona normalmente em qualquer versão Python 3.8+.

---

## Explicação das funções

### Arquivo main.py

- hamiltonian_path(graph, path, visited, n):
  Função recursiva de backtracking que busca o caminho hamiltoniano.

  - Se o caminho tem todos os vértices, encontrou solução
  - Para cada vizinho não visitado, tenta adicionar ao caminho
  - Se não funciona, faz backtrack removendo o vértice

- solve_hamiltonian():
  Função principal que define o grafo e executa a busca.

  - Cria um grafo exemplo
  - Tenta encontrar caminho começando de cada vértice
  - Imprime o resultado encontrado

---

## Saída da Execução

Exemplo de execução:

```
1. Testando: Quadrado com diagonal
   Vértices: [0, 1, 2, 3] (n=4)
   [OK] Caminho encontrado: 0 -> 1 -> 2 -> 3

2. Testando: Triângulo completo K3
   Vértices: [0, 1, 2] (n=3)
   [OK] Caminho encontrado: 0 -> 1 -> 2

3. Testando: Estrela (centro + 3 pontas)
   Vértices: [0, 1, 2, 3] (n=4)
   [X] Caminho não encontrado

4. Testando: Caminho linear 0-1-2-3-4
   Vértices: [0, 1, 2, 3, 4] (n=5)
   [OK] Caminho encontrado: 0 -> 1 -> 2 -> 3 -> 4

5. Testando: Pentágono (ciclo C5)
   Vértices: [0, 1, 2, 3, 4] (n=5)
   [OK] Caminho encontrado: 0 -> 1 -> 2 -> 3 -> 4

6. Testando: Grafo completo K4
   Vértices: [0, 1, 2, 3] (n=4)
   [OK] Caminho encontrado: 0 -> 1 -> 2 -> 3

...

(Total de 22 grafos testados)
```

---

# Análise da Complexidade Ciclomática

## 1. Fluxo de controle da função `backtrack_hamiltoniano`

1. Entrada na função
2. Decisão (`if len(caminho) == total_vertices`)
   - Verdadeiro → retorna True (caso base)
   - Falso → continua a busca
3. Loop (`for vizinho in grafo.get(vertice_atual, [])`)
4. Decisão (`if vizinho not in visitados`)
   - Verdadeiro → tenta este vizinho
   - Falso → pula para próximo vizinho
5. Decisão (`if backtrack_hamiltoniano(...)`)
   - Verdadeiro → retorna True (solução encontrada)
   - Falso → faz backtrack e continua
6. Retorna False (nenhuma solução encontrada)

---

## 2. Grafo de fluxo (nós e arestas)

Nós (N): blocos de execução ou decisões
Arestas (E): transições entre nós

### Nós identificados

1. Entrada da função
2. Decisão do caso base
3. `return True` (caso base)
4. Início do loop
5. Decisão de vizinho não visitado
6. Adicionar ao caminho
7. Chamada recursiva
8. Decisão do resultado recursivo
9. `return True` (solução encontrada)
10. Backtrack (remover do caminho)
11. Volta ao loop
12. `return False` (fim)

N = 12

---

### Arestas identificadas

- (1) → (2)
- (2) → (3) (verdadeira)
- (2) → (4) (falsa)
- (4) → (5)
- (5) → (6) (verdadeira)
- (5) → (4) (falsa, volta ao loop)
- (6) → (7)
- (7) → (8)
- (8) → (9) (verdadeira)
- (8) → (10) (falsa)
- (10) → (11)
- (11) → (4) (volta ao loop)
- (4) → (12) (fim do loop)

E = 13

---

## 3. Cálculo da complexidade ciclomática

Fórmula:

$$
M = E - N + 2P
$$

- $E = 13$ (arestas)
- $N = 12$ (nós)
- $P = 1$ (componente conectado)

$$
M = 13 - 12 + 2(1) = 3
$$

---

## Resultado

A complexidade ciclomática da função `backtrack_hamiltoniano` é 3.

Existem 3 caminhos independentes no fluxo de execução:

1. Caminho do caso base (todos os vértices visitados)
2. Caminho de sucesso na recursão (solução encontrada)
3. Caminho de backtrack (tenta próximo vizinho)

---

# Análise da Complexidade Assintótica

## 1. Complexidade Temporal

O algoritmo utiliza backtracking para explorar todas as possibilidades:

- No pior caso, precisa testar todas as permutações possíveis de vértices
- Para cada vértice inicial, pode explorar até (n-1)! caminhos
- Cada verificação de vizinho é O(1) com dicionários

A recorrência no pior caso é:

$$
T(n) = n \cdot (n-1) \cdot (n-2) \cdot ... \cdot 1 = O(n!)
$$

Com otimizações de poda (verificação de vizinhos), o algoritmo pode ser mais eficiente na prática, mas mantém a complexidade teórica exponencial.

---

## 2. Complexidade Espacial

- O algoritmo usa recursão com profundidade máxima de n (número de vértices)
- Estruturas auxiliares:
  - `caminho`: lista com até n elementos → O(n)
  - `visitados`: set com até n elementos → O(n)
  - Pilha de recursão: até n chamadas → O(n)

Portanto, a complexidade espacial é:

$$
O(n)
$$

---

## 3. Casos Principais

### Melhor Caso

- Grafo com apenas 1 vértice: retorna imediatamente
- Ou quando o primeiro caminho testado é hamiltoniano
- Complexidade:

$$
O(1) \text{ ou } O(n)
$$

### Caso Médio

- Depende significativamente da estrutura do grafo:
  - Grafos densos (muitas arestas): encontra soluções mais rapidamente
  - Grafos esparsos: pode precisar explorar muitos caminhos
- Complexidade típica:

$$
O(k \cdot n!) \text{ onde } k < 1
$$

### Pior Caso

- Grafo sem caminho hamiltoniano: explora todas as possibilidades
- Ou grafo onde o caminho está na última permutação testada
- Complexidade:

$$
O(n!)
$$

---

## 4. Aplicação do Teorema Mestre

O Teorema Mestre não se aplica a este algoritmo porque:

1. Não segue divisão e conquista: O algoritmo usa backtracking, não divide o problema em subproblemas independentes de tamanho similar
2. Número variável de chamadas recursivas: Em cada nível, o número de chamadas recursivas depende do grau do vértice atual, não é constante
3. Subproblemas sobrepostos: O mesmo estado pode ser alcançado por diferentes caminhos

O Teorema Mestre se aplica a recorrências da forma:
$$T(n) = aT(n/b) + f(n)$$

Nosso algoritmo tem uma estrutura de árvore de decisão exponencial, não uma divisão logarítmica.

---

# Análise de Classes de Complexidade

## 1. Classes P, NP, NP-Completo e NP-Difícil

### Problema do Caminho Hamiltoniano:

- Classe NP: ✓ SIM

  - Dado um caminho, podemos verificar em tempo polinomial O(n) se é hamiltoniano
  - Basta verificar se visita todos os vértices exatamente uma vez e se as arestas existem

- Classe P: ✗ NÃO (não conhecido)

  - Não existe algoritmo conhecido que resolva o problema em tempo polinomial
  - O melhor algoritmo conhecido é exponencial O(n!)

- Classe NP-Completo: ✓ SIM

  - O problema do Caminho Hamiltoniano é NP-Completo
  - Qualquer problema em NP pode ser reduzido a ele em tempo polinomial

- Classe NP-Difícil: ✓ SIM (por consequência)
  - Todo problema NP-Completo é também NP-Difícil

---

## 2. Relação com o Problema do Caixeiro Viajante

O Problema do Caixeiro Viajante (TSP) está intimamente relacionado:

### Caminho Hamiltoniano → TSP:

- TSP busca o ciclo hamiltoniano de menor custo
- Caminho Hamiltoniano busca apenas um caminho que visite todos os vértices
- TSP é "mais difícil" pois adiciona a restrição de retornar ao início + otimização de custo

### Redução Polinomial:

- Podemos reduzir o Problema do Caminho Hamiltoniano ao TSP:
  1. Dado um grafo G, adicione um vértice artificial v'
  2. Conecte v' a todos os vértices de G com peso 1
  3. Se TSP encontrar ciclo de custo n+1, então G tem caminho hamiltoniano

### Implicações:

- Como TSP é NP-Difícil, e Caminho Hamiltoniano se reduz a TSP, confirma que Caminho Hamiltoniano é NP-Completo
- Ambos são problemas fundamentais em otimização combinatória
- Usados em roteamento, logística, design de circuitos, bioinformática

---

## Conclusão

- Tempo:

  - Melhor caso: O(1) ou O(n)
  - Caso médio: O(k·n!) onde k < 1
  - Pior caso: O(n!)

- Espaço: O(n)

- Classificação: NP-Completo

- Teorema Mestre: Não aplicável (backtracking ≠ divisão e conquista)

- Aplicações práticas: Problemas de roteamento, planejamento, otimização em grafos

---

## Estrutura do Projeto

```
CaminhoHamiltoniano/
├── main.py              # Implementação principal do algoritmo
├── view.py               # Visualização gráfica (ponto extra)
├── README.md             # Documentação completa do projeto
└── assets/              # Pasta para imagens geradas
    ├── quadrado_diagonal.png
    ├── estrela_sem_caminho.png
    ├── saltos_obrigatorios.png
    └── cubo_modificado.png
```

### Arquivos:

- main.py: Contém a implementação completa do algoritmo de backtracking para encontrar caminhos hamiltonianos
  - Nota: Os grafos de teste foram criados com auxílio do GitHub Copilot apenas para estruturação dos dados
- view.py: Arquivo de visualização gráfica usando NetworkX e Matplotlib (ponto extra)
- README.md: Documentação completa com análises teóricas e instruções de uso
- assets/: Pasta onde são salvos os gráficos PNG gerados pela visualização

---
