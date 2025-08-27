def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    tamanho = max(len(str(x)), len(str(y)))

    ponto_divisao = tamanho // 2

    x1, x0 = divmod(x, 10**ponto_divisao)
    y1, y0 = divmod(y, 10**ponto_divisao)

    produtos_altos = karatsuba(x1, y1)
    produtos_baixos = karatsuba(x0, y0)
    produtos_mistos = karatsuba(x1 + x0, y1 + y0) - produtos_altos - produtos_baixos

    return produtos_altos * 10**(2 * ponto_divisao) + (produtos_mistos * 10**ponto_divisao) + produtos_baixos



#test
if __name__ == "__main__":
    x = 12345678
    y = 87654321
    print(f"Multiplicação de Karatsuba para {x} e {y} é: {karatsuba(x, y)}")