import numpy as np



for N in [1e2, 1e3, 1e4, 1e5, 1e6, 1e7]:
    N = int(N)
    n = 0
    # gerando as coordenadas dos pontos no quadrado unitário seguindo
    # uma distribuição uniforme entre 0 e 1.
    x = np.random.uniform(size=N)
    y = np.random.uniform(size=N)

    # percorrendo as listas geradas de x e y
    for i in range(N):
        # se o ponto dentro do quadrante, n é incrementado
        if x[i] ** 2 + y[i] ** 2 < 1:
            n += 1
    # como a area de um quadrante do circulo é pi/4,
    # multiplicamos a razao n/N por 4
    pi = 4 * n / N
    print(f"N = {N} => pi = {pi}")
