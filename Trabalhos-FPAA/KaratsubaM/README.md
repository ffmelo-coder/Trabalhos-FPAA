# Projeto KaratsubaM

## Sobre o Projeto

O **KaratsubaM** é um projeto educativo desenvolvido para demonstrar a multiplicação eficiente de inteiros grandes utilizando o **algoritmo de Karatsuba**.
O código é implementado em **Python puro**, sem dependências externas, de forma simples e fácil de entender.

Ele mostra como a técnica de **divisão e conquista** pode reduzir a complexidade da multiplicação tradicional ($O(n^2)$) para aproximadamente $O(n^{1.58})$.

---

## O que é o Algoritmo de Karatsuba?

O algoritmo de **Karatsuba** é um método recursivo de multiplicação de números inteiros.
Ele reduz o número de multiplicações necessárias, substituindo parte delas por somas e subtrações.

### Fórmula

$$
x \cdot y = (x1 \cdot y1) \cdot 10^{2m} + ((x1 + x0)(y1 + y0) - (x1 \cdot y1) - (x0 \cdot y0)) \cdot 10^m + (x0 \cdot y0)
$$

Onde:

* $x1, x0$: partes alta e baixa do número $x$
* $y1, y0$: partes alta e baixa do número $y$
* $m$: ponto de divisão

Isso reduz **4 multiplicações** para apenas **3**, tornando o algoritmo mais eficiente.

---

## O que é a notação Big-O?

A **notação Big-O** mede como o tempo de execução cresce em função da entrada.

* **Multiplicação tradicional:** $O(n^2)$
* **Karatsuba:** $O(n^{\log_2 3}) \approx O(n^{1.58})$

Isso significa que o algoritmo de Karatsuba é muito mais rápido para números com muitos dígitos.

---

## Diferença entre Big-O e Karatsuba

* **Big-O:** descreve a eficiência de algoritmos em tempo e memória.
* **Karatsuba:** é um **algoritmo específico** que melhora a eficiência da multiplicação de inteiros grandes.

---

## Sobre as bibliotecas utilizadas

Nenhuma biblioteca externa foi utilizada.
O código usa apenas funções nativas do **Python**, como `divmod()` para dividir números em partes.

---

## Por que usar o algoritmo de Karatsuba?

* Demonstração prática de **divisão e conquista**.
* Multiplicação mais eficiente para inteiros muito grandes.
* Base para algoritmos mais avançados em **criptografia** e **cálculo numérico**.
* Exercício de **recursão** e **análise de algoritmos**.

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

* **karatsuba(x, y):**
  Função recursiva que implementa o algoritmo de Karatsuba.

  * Divide os números em duas partes (`x1, x0`, `y1, y0`) usando `divmod`.
  * Calcula os produtos: altos, baixos e mistos.
  * Combina os resultados usando a fórmula de Karatsuba.
  * Caso base: quando os números têm apenas 1 dígito, a multiplicação é feita diretamente.

* **if **name** == "**main**":**
  Executa um teste multiplicando `12345678` por `87654321` e imprime o resultado.

---

## Saída da Execução

Exemplo de execução:

```
Multiplicação de Karatsuba para 12345678 e 87654321 é: 1082152022374638
```

Resultado esperado (checagem manual):

```
12345678 * 87654321 = 1082152022374638
```

---

# Análise da Complexidade Ciclomática

## 1. Fluxo de controle da função `karatsuba`

1. **Entrada** na função
2. **Decisão (`if x < 10 or y < 10`)**

   * **Verdadeiro** → retorna `x * y`
   * **Falso** → continua o cálculo recursivo
3. Executa as operações:

   * calcula `tamanho`
   * calcula `ponto_divisao`
   * calcula `x1, x0`
   * calcula `y1, y0`
   * chama `karatsuba(x1, y1)`
   * chama `karatsuba(x0, y0)`
   * calcula `produtos_mistos`
   * retorna a combinação final

---

## 2. Grafo de fluxo (nós e arestas)

**Nós (N):** blocos de execução ou decisões
**Arestas (E):** transições entre nós

### Nós identificados

1. Entrada da função
2. Decisão do `if`
3. `return x * y` (saída do caso base)
4. `tamanho = ...`
5. `ponto_divisao = ...`
6. `x1, x0 = divmod(...)`
7. `y1, y0 = divmod(...)`
8. `produtos_altos = karatsuba(x1, y1)`
9. `produtos_baixos = karatsuba(x0, y0)`
10. `produtos_mistos = ...`
11. `return produtos_altos * ...` (final)

**N = 11**

---

### Arestas identificadas

* (1) Entrada → (2) if
* (2) if → (3) return (verdadeira)
* (2) if → (4) tamanho (falsa)
* (4) → (5)
* (5) → (6)
* (6) → (7)
* (7) → (8)
* (8) → (9)
* (9) → (10)
* (10) → (11) return

**E = 11**

---

### Grafo de fluxo

```

```

---

## 3. Cálculo da complexidade ciclomática

Fórmula:

$$
M = E - N + 2P
$$

* $E = 11$ (arestas)
* $N = 11$ (nós)
* $P = 1$ (componente conectado)

$$
M = 11 - 11 + 2(1) = 2
$$

---

## Resultado

A **complexidade ciclomática da função `karatsuba` é 2**.

Existem **2 caminhos independentes** no fluxo de execução:

1. Caminho do caso base (`if verdadeiro → return x * y`)
2. Caminho recursivo (`if falso → cálculos até return final`)

---

Boa! Vamos agora analisar a **complexidade assintótica** do seu algoritmo de **Karatsuba** seguindo exatamente esse padrão.

---

# Análise da Complexidade Assintótica

## 1. Complexidade Temporal

O algoritmo de Karatsuba segue a ideia de **divisão e conquista**:

* Divide os números em duas partes ($x1, x0$ e $y1, y0$)
* Realiza **3 chamadas recursivas** ao invés de 4 multiplicações tradicionais
* Faz operações adicionais de soma, subtração e deslocamento em potências de 10, que são de custo linear ($O(n)$)

A recorrência do tempo de execução é:

$$
T(n) = 3T\left(\frac{n}{2}\right) + O(n)
$$

Aplicando o Teorema Mestre, obtemos:

$$
T(n) = O(n^{\log_2 3}) \approx O(n^{1.585})
$$

---

## 2. Complexidade Espacial

* A função é **recursiva**, então o espaço é dominado pela **profundidade da pilha de recursão**.
* A cada nível, os números são divididos pela metade.
* A profundidade máxima da recursão é:

$$
O(\log n)
$$

* Além da pilha, o algoritmo usa apenas variáveis auxiliares de tamanho proporcional a $O(n)$.

Portanto, a **complexidade espacial** é:

$$
O(n + \log n) \approx O(n)
$$

---

## 3. Casos Principais

### Melhor Caso

* Ocorre quando os números são pequenos (menores que 10).
* O algoritmo não entra em recursão, retornando diretamente:

$$
O(1)
$$

### Caso Médio

* Para números com tamanho arbitrário $n$, o algoritmo segue a divisão recursiva padrão.
* Complexidade:

$$
O(n^{\log_2 3}) \approx O(n^{1.585})
$$

### Pior Caso

* Igual ao caso médio, pois não há cenários que degradem além da lógica normal de divisão recursiva.
* Complexidade:

$$
O(n^{\log_2 3})
$$

---

## Conclusão

* **Tempo**:

  * Melhor caso: $O(1)$
  * Caso médio: $O(n^{1.585})$
  * Pior caso: $O(n^{1.585})$

* **Espaço**:

  * $O(n)$, dominado pela manipulação dos números em cada nível de recursão.

---

