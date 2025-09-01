# Projeto MaxMinSelect

## Sobre o Projeto

O **MaxMinSelect** é um projeto educativo desenvolvido para demonstrar como encontrar o **maior** e o **menor elemento** de um array utilizando a técnica de **divisão e conquista**.

O código é implementado em **Python puro**, sem dependências externas, de forma simples e fácil de entender.

Ele mostra como a abordagem recursiva pode ser utilizada para resolver problemas básicos de seleção de valores em uma lista.

---

## O que é o Algoritmo MaxMinSelect?

O algoritmo **MaxMinSelect** é um método recursivo para encontrar os valores máximo e mínimo em uma lista.

Ele segue a ideia de **divisão e conquista**:

1. Divide a lista em duas metades.
2. Calcula o máximo e o mínimo de cada metade recursivamente.
3. Combina os resultados comparando os maiores e menores encontrados.

### Passos principais:

* Caso base: quando a lista tem apenas **1 elemento**, esse valor é **máximo e mínimo ao mesmo tempo**.
* Caso recursivo: divide a lista em duas partes, resolve cada parte e combina os resultados.

---

## O que é a notação Big-O?

A **notação Big-O** mede como o tempo de execução cresce em função da entrada.

No caso deste algoritmo:

* **Força bruta:** percorrendo a lista inteira, teria **O(n)**.
* **MaxMinSelect com divisão e conquista:** também tem **O(n)**, mas organiza o processo de forma recursiva.

---

## Sobre as bibliotecas utilizadas

Nenhuma biblioteca externa foi utilizada.
O código usa apenas funções nativas do **Python** (`max`, `min`, chamadas recursivas e `print`).

---

## Por que usar este algoritmo?

* Demonstração prática da técnica de **divisão e conquista**.
* Útil em **exercícios de recursão** e **análise de algoritmos**.
* Pode ser expandido para problemas mais complexos, como **estatísticas em grandes datasets**.

---

## Ambiente virtual

Passo 1: Criar e ativar o ambiente virtual

```bash
python3 -m venv .venv
```

Ativar o ambiente virtual:

* macOS/Linux:

```bash
source .venv/bin/activate
```

* Windows:

```bash
.venv\Scripts\activate
```

Passo 2: Executar o script

```bash
python main.py
```

---

## Versão do Python

Este projeto foi desenvolvido em **Python 3.12.3**, mas funciona normalmente em qualquer versão **Python 3.8+**.

---

## Explicação das funções

### Arquivo **main.py**

* **maxmin\_select(arr):**
  Função recursiva que encontra o **máximo e mínimo** em uma lista.

  * Caso base: se o tamanho da lista é 1, retorna `(arr[0], arr[0])`.
  * Caso recursivo: divide a lista em duas metades (`left` e `right`), encontra máximo e mínimo de cada metade, e retorna `max(left_max, right_max)` e `min(left_min, right_min)`.

* **main():**
  Inicializa um array de exemplo `[12, 45, 7, 23, 56, 89, 34]`, chama a função `maxmin_select` e imprime os resultados.

---

## Saída da Execução

Exemplo de execução:

```
Maior elemento: 89
Menor elemento: 7
```

---

# Análise da Complexidade Ciclomática

## 1. Fluxo de controle da função `maxmin_select`

1. **Entrada** na função
2. **Decisão (`if len(arr) == 1`)**

   * **Verdadeiro** → retorna `(arr[0], arr[0])`
   * **Falso** → continua o cálculo recursivo
3. Executa as operações:

   * calcula `mid`
   * chama `maxmin_select(arr[:mid])`
   * chama `maxmin_select(arr[mid:])`
   * retorna `max(left_max, right_max), min(left_min, right_min)`

---

## 2. Grafo de fluxo (nós e arestas)

**Nós (N):** blocos de execução ou decisões
**Arestas (E):** transições entre nós

### Nós identificados

1. Entrada da função
2. Decisão do `if`
3. `return (arr[0], arr[0])` (caso base)
4. `mid = len(arr) // 2`
5. chamada recursiva esquerda
6. chamada recursiva direita
7. `return max(...), min(...)`

**N = 7**

---

### Arestas identificadas

* (1) → (2)
* (2) → (3) (verdadeira)
* (2) → (4) (falsa)
* (4) → (5)
* (5) → (6)
* (6) → (7)

**E = 6**

---

### Grafo de fluxo



---

## 3. Cálculo da complexidade ciclomática

Fórmula:

$$
M = E - N + 2P
$$

* \$E = 6\$ (arestas)
* \$N = 7\$ (nós)
* \$P = 1\$ (componente conectado)

$$
M = 6 - 7 + 2(1) = 1
$$

---

## Resultado

A **complexidade ciclomática da função `maxmin_select` é 1**.

Isso significa que existe apenas **1 caminho de execução independente** (decisão simples entre caso base e recursão).

---

# Análise da Complexidade Assintótica

## 1. Complexidade Temporal

O algoritmo percorre todos os elementos da lista.

A cada divisão, ele chama recursivamente as duas metades até listas unitárias.
Portanto, a recorrência é:

$$
T(n) = 2T\left(\frac{n}{2}\right) + O(1)
$$

Aplicando o Teorema Mestre:

$$
T(n) = O(n)
$$

---

## 2. Complexidade Espacial

* O algoritmo usa **recursão**, então o espaço é dominado pela **profundidade da pilha**.
* A cada nível, o array é dividido em duas partes.
* A profundidade máxima é:

$$
O(\log n)
$$

Além da pilha, não há armazenamento adicional significativo.

Portanto:

$$
O(\log n)
$$

---

## 3. Casos Principais

### Melhor Caso

* Quando a lista tem **1 elemento**, o algoritmo retorna imediatamente.
* Complexidade:

$$
O(1)
$$

### Caso Médio

* Para listas de tamanho arbitrário \$n\$, o algoritmo precisa analisar todas as divisões.
* Complexidade:

$$
O(n)
$$

### Pior Caso

* Igual ao caso médio, pois todos os elementos precisam ser percorridos.
* Complexidade:

$$
O(n)
$$

---

## Conclusão

* **Tempo**:

  * Melhor caso: \$O(1)\$
  * Caso médio: \$O(n)\$
  * Pior caso: \$O(n)\$

* **Espaço**:

  * \$O(\log n)\$ devido à pilha de chamadas recursivas

---
