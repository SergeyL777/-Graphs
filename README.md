# Реализация ориентированного графа и алгоритмов обхода

Проект содержит реализацию ориентированного графа на Python с различными способами представления и алгоритмами обхода.

## Функциональность

Проект предоставляет следующие возможности:

* Класс `DirectedGraph` для работы с ориентированным графом.
* Алгоритм обхода в ширину (BFS).
* Представление графа в виде матрицы смежности.
* Представление графа в виде списка смежности.
* Функции преобразования между разными представлениями графа.
* Операции добавления вершин и рёбер для каждого представления.

### Требования

* Python 3.6+
* Стандартные библиотеки: `collections`

### Класс DirectedGraph

from graph import DirectedGraph, bfs

# Создаём граф
graph = DirectedGraph()

# Добавляем вершины и рёбра
graph.add_vertex('A')
graph.add_edge('A', 'B')
graph.add_edge('B', 'C')

# Обход в ширину
result = bfs(graph, 'A')  # ['A', 'B', 'C']

### Матрица смежности

from graph import create_adjacency_matrix, add_vertex_to_matrix, add_edge_to_matrix

edges = [('A', 'B'), ('B', 'C')]
matrix, vertices = create_adjacency_matrix(edges)

# Добавляем вершину и ребро
matrix, vertices = add_vertex_to_matrix(matrix, vertices, 'D')
add_edge_to_matrix(matrix, vertices, 'D', 'A')

### Список смежности

from graph import create_adjacency_list, add_vertex_to_list, add_edge_to_list

edges = [('A', 'B'), ('B', 'C')]
adj_list = create_adjacency_list(edges)

# Добавляем вершину и ребро
add_vertex_to_list(adj_list, 'D')
add_edge_to_list(adj_list, 'D', 'A')
