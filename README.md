# Método Manhattan vs Euclidiano

## Simulação Computacional e Análise Geométrica em ℤ²

Este repositório apresenta uma implementação em **Python** para comparação entre as métricas **Manhattan (L1)** e **Euclidiana (L2)** em um plano discreto bidimensional, com geração de resultados numéricos e visualizações gráficas.

O objetivo é demonstrar:

* Diferenças geométricas entre as bolas métricas
* Crescimento do número de pontos inteiros dentro de cada raio
* Aproximação assintótica das métricas
* Representação visual (losango vs círculo)

---

## 📌 Conceitos Matemáticos

### 🔷 Distância Manhattan (L1)

[
d_1((x_1,y_1),(x_2,y_2)) = |x_1-x_2| + |y_1-y_2|
]

A bola discreta de raio `r` forma um **losango** no plano.

Número de pontos inteiros:

[
|B_1(r)| = 1 + 2r(r+1)
]

---

### 🔷 Distância Euclidiana (L2)

[
d_2((x_1,y_1),(x_2,y_2)) = \sqrt{(x_1-x_2)^2 + (y_1-y_2)^2}
]

A bola discreta de raio `r` aproxima um **círculo**.

Número de pontos inteiros:

[
|B_2(r)| \approx \pi r^2
]

---

## 📊 Exemplo de Saída no Terminal

```
r= 1 | Manhattan=    5 | Euclidiana=    5
r= 2 | Manhattan=   13 | Euclidiana=   13
r= 3 | Manhattan=   25 | Euclidiana=   29
r=10 | Manhattan=  221 | Euclidiana=  317
r=20 | Manhattan=  841 | Euclidiana= 1257
r=60 | Manhattan= 7321 | Euclidiana=11289
```

Observação:

* Para raios pequenos os valores são próximos.
* Para raios grandes, a métrica Euclidiana cresce mais rapidamente.
* Assintoticamente:

[
|B_1(r)| \sim 2r^2
]
[
|B_2(r)| \sim \pi r^2
]

Como ( \pi \approx 3.1416 > 2 ), a bola Euclidiana contém mais pontos.

---

## 📈 Visualizações Geradas

O programa produz dois gráficos lado a lado:

1. Crescimento do número de pontos em função do raio
2. Diferença entre as métricas (L2 − L1)

Além disso, pode gerar:

* Visualização do losango (L1)
* Visualização do círculo discreto (L2)

---

## 🎨 Representação Geométrica

### 🔶 Bola L1 (Losango)

* Crescimento quadrático
* Simetria em relação aos eixos

### 🔵 Bola L2 (Círculo discreto)

* Crescimento proporcional a πr²
* Contorno mais suave

---

## ⚙️ Requisitos

* Python 3.8+
* NumPy
* Matplotlib

Instalação:

```bash
pip install numpy matplotlib
```

---

## ▶️ Como Executar

```bash
python main.py
```

ou

```bash
python comparacao_metricas.py
```

(dependendo do nome do arquivo principal)

---

## 📂 Estrutura Esperada

```
bm/
│
├── main.py
├── comparacao_metricas.py
├── figuras/
│   ├── grafico_metricas.png
│   └── bolas_metricas.png
└── README.md
```

---

## 📚 Aplicações

* Geometria Discreta
* Teoria dos Grafos
* Modelagem Urbana (grid city blocks)
* Inteligência Artificial (heurísticas A*)
* Análise de complexidade espacial

---

## 📖 Referências Teóricas

* Métricas Lp em espaços normados
* Problema do Círculo de Gauss
* Geometria em ℤ²
* Análise assintótica

---

## 📌 Conclusão

A comparação entre as métricas Manhattan e Euclidiana evidencia como diferentes noções de distância produzem estruturas geométricas distintas no plano discreto. Embora ambas cresçam quadraticamente, seus coeficientes principais diferem significativamente, refletindo propriedades geométricas fundamentais.


