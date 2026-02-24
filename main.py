import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
N = 301
center = N // 2
max_r = 60

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def euclidean_distance(x1, y1, x2, y2):
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

r_values = []
manhattan_counts = []
euclidean_counts = []
ratio = []

for r in range(1, max_r + 1):
    count_m = 0
    count_e = 0
    
    for i in range(N):
        for j in range(N):
            if manhattan_distance(center, center, i, j) <= r:
                count_m += 1
            if euclidean_distance(center, center, i, j) <= r:
                count_e += 1
    
    r_values.append(r)
    manhattan_counts.append(count_m)
    euclidean_counts.append(count_e)
    ratio.append(count_e / count_m)

    print(f"r={r:2d} | Manhattan={count_m:5d} | Euclidiana={count_e:5d}")

# =====================================
# FIGURA COMPOSTA – DOIS GRÁFICOS
# =====================================

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Gráfico 1 – Crescimento
axes[0].plot(r_values, manhattan_counts, color='red', label='Manhattan')
axes[0].plot(r_values, euclidean_counts, color='blue', label='Euclidiana')
axes[0].set_xlabel("Raio r")
axes[0].set_ylabel("Número de pontos")
axes[0].set_title("Crescimento da Bola Métrica")
axes[0].legend()

# Gráfico 2 – Razão
axes[1].plot(r_values, ratio, color='purple')
axes[1].set_xlabel("Raio r")
axes[1].set_ylabel("Razão N_E / N_M")
axes[1].set_title("Razão entre Métricas")

plt.tight_layout()
plt.show()
