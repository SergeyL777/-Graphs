class DirectedGraph:
    def __init__(self):
        self.vertices = set()  # Множество вершин
        self.edges = {}      # Словарь смежности: вершина -> множество соседних вершин

    def add_vertex(self, vertex):
        """Добавление вершины в граф"""
        self.vertices.add(vertex)
        if vertex not in self.edges:
            self.edges[vertex] = set()

    def add_edge(self, from_vertex, to_vertex):
        """Добавление направленного ребра от from_vertex к to_vertex"""
        # Добавляем вершины, если их ещё нет
        self.add_vertex(from_vertex)
        self.add_vertex(to_vertex)
        # Добавляем ребро
        self.edges[from_vertex].add(to_vertex)

    def __str__(self):
        return f"Vertices: {self.vertices}\nEdges: {self.edges}"

# Создаём граф
graph = DirectedGraph()

# Добавляем вершины
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')

# Добавляем рёбра
graph.add_edge('A', 'B')
graph.add_edge('B', 'C')
graph.add_edge('C', 'A')
graph.add_edge('A', 'C')

print(graph)

# Обход в ширину (BFS)
from collections import deque

def bfs(graph, start_vertex):
    """
    Обход ориентированного графа в ширину (Breadth-First Search)
    
    Args:
        graph: экземпляр DirectedGraph
        start_vertex: начальная вершина для обхода
    
    Returns:
        Список вершин в порядке обхода
    """
    if start_vertex not in graph.vertices:
        raise ValueError(f"Вершина {start_vertex} не существует в графе")

    visited = set()           # Множество посещённых вершин
    queue = deque([start_vertex])  # Очередь для BFS
    result = []               # Результат обхода

    while queue:
        current = queue.popleft()
        
        if current not in visited:
            visited.add(current)
            result.append(current)
            
            # Добавляем всех соседей текущей вершины в очередь
            for neighbor in graph.edges.get(current, []):
                if neighbor not in visited:
                    queue.append(neighbor)

    return result

# Используем созданный граф
print("BFS обход начиная с A:", bfs(graph, 'A'))
print("BFS обход начиная с B:", bfs(graph, 'B'))

# Матрица смежности
def create_adjacency_matrix(edges, vertices=None):
    """
    Создание матрицы смежности из списка рёбер
    
    Args:
        edges: список кортежей (from_vertex, to_vertex)
        vertices: опциональный список вершин (если не указан, берётся из рёбер)
    
    Returns:
        tuple: (матрица смежности, список вершин)
    """
    # Определяем все вершины
    if vertices is None:
        vertices = sorted(set(v for edge in edges for v in edge))
    else:
        vertices = sorted(vertices)
    
    n = len(vertices)
    # Создаём матрицу n x n, заполненную нулями
    matrix = [[0] * n for _ in range(n)]
    
    # Сопоставление вершины с индексом
    vertex_to_index = {vertex: i for i, vertex in enumerate(vertices)}
    
    # Заполняем матрицу
    for from_v, to_v in edges:
        i = vertex_to_index[from_v]
        j = vertex_to_index[to_v]
        matrix[i][j] = 1
    
    return matrix, vertices

def add_vertex_to_matrix(matrix, vertices, new_vertex):
    """
    Добавление вершины в матрицу смежности
    
    Args:
        matrix: текущая матрица смежности
        vertices: текущий список вершин
        new_vertex: новая вершина
    
    Returns:
        tuple: (обновлённая матрица, обновлённый список вершин)
    """
    if new_vertex in vertices:
        return matrix, vertices  # Вершина уже существует
    
    vertices.append(new_vertex)
    n = len(vertices)
    
    # Расширяем матрицу: добавляем строку и столбец
    for row in matrix:
        row.append(0)  # Добавляем столбец
    
    # Добавляем новую строку
    matrix.append([0] * n)
    
    return matrix, vertices

def add_edge_to_matrix(matrix, vertices, from_vertex, to_vertex):
    """
    Добавление ребра в матрицу смежности
    
    Args:
        matrix: текущая матрица смежности
        vertices: список вершин
        from_vertex: начальная вершина ребра
        to_vertex: конечная вершина ребра
    """
    if from_vertex not in vertices or to_vertex not in vertices:
        raise ValueError("Одна из вершин не существует в графе")
    
    i = vertices.index(from_vertex)
    j = vertices.index(to_vertex)
    matrix[i][j] = 1

# ТЕСТИРУЕМ МАТРИЦУ СМЕЖНОСТИ
# Список рёбер
edges = [('A', 'B'), ('B', 'C'), ('C', 'A'), ('A', 'C')]

# Создаём матрицу смежности
matrix, vertices = create_adjacency_matrix(edges)
print("Матрица смежности:")
for row in matrix:
    print(row)
print("Вершины:", vertices)

# Добавляем новую вершину
matrix, vertices = add_vertex_to_matrix(matrix, vertices, 'D')
print("\nПосле добавления вершины D:")
for row in matrix:
    print(row)
print("Вершины:", vertices)

# Добавляем ребро из D в A
add_edge_to_matrix(matrix, vertices, 'D', 'A')
print("\nПосле добавления ребра D->A:")
for row in matrix:
    print(row)

# Список смежности
def create_adjacency_list(edges):
    """
    Создание списка смежности из списка рёбер
    
    Args:
        edges: список кортежей (from_vertex, to_vertex)
    
    Returns:
        dict: словарь смежности {вершина: [список соседних вершин]}
    """
    adjacency_list = {}
    
    for from_v, to_v in edges:
        if from_v not in adjacency_list:
            adjacency_list[from_v] = []
        if to_v not in adjacency_list:
            adjacency_list[to_v] = []  # Инициализируем вершину, даже если у неё нет исходящих рёбер
        
        adjacency_list[from_v].append(to_v)
    
    return adjacency_list

def add_vertex_to_list(adjacency_list, vertex):
    """
    Добавление вершины в список смежности
    
    Args:
        adjacency_list: текущий словарь смежности
        vertex: новая вершина
    """
    if vertex not in adjacency_list:
        adjacency_list[vertex] = []

def add_edge_to_list(adjacency_list, from_vertex, to_vertex):
    """
    Добавление ребра в список смежности

    Args:
        adjacency_list: текущий словарь смежности
        from_vertex: начальная вершина ребра
        to_vertex: конечная вершина ребра
    """
    # Добавляем вершины, если их нет
    add_vertex_to_list(adjacency_list, from_vertex)
    add_vertex_to_list(adjacency_list, to_vertex)

    # Добавляем ребро (если его ещё нет)
    if to_vertex not in adjacency_list[from_vertex]:
        adjacency_list[from_vertex].append(to_vertex)

# Тестирование списка смежности
# Список рёбер для тестирования
edges = [('A', 'B'), ('B', 'C'), ('C', 'A'), ('A', 'C')]

# Создаём список смежности из списка рёбер
adj_list = create_adjacency_list(edges)
print("Список смежности:")
for vertex, neighbors in adj_list.items():
    print(f"{vertex}: {neighbors}")

# Добавляем новую вершину
add_vertex_to_list(adj_list, 'D')
print("\nПосле добавления вершины D:")
for vertex, neighbors in adj_list.items():
    print(f"{vertex}: {neighbors}")

# Добавляем ребро из D в A
add_edge_to_list(adj_list, 'D', 'A')
print("\nПосле добавления ребра D->A:")
for vertex, neighbors in adj_list.items():
    print(f"{vertex}: {neighbors}")

# Полное тестирование всех реализаций
print("=" * 50)
print("ПОЛНОЕ ТЕСТИРОВАНИЕ ВСЕХ РЕАЛИЗАЦИЙ")
print("=" * 50)

# Исходные данные
edges = [('A', 'B'), ('B', 'C'), ('C', 'A'), ('A', 'C'), ('D', 'A')]

print("Исходные рёбра:", edges)

# 1. Тестирование DirectedGraph
print("\n1. DirectedGraph:")
graph = DirectedGraph()
for from_v, to_v in edges:
    graph.add_edge(from_v, to_v)
print(graph)
print("BFS от A:", bfs(graph, 'A'))

# 2. Тестирование матрицы смежности
print("\n2. МАТРИЦА СМЕЖНОСТИ:")
matrix, vertices = create_adjacency_matrix(edges)
print("Вершины:", vertices)
print("Матрица:")
for row in matrix:
    print(row)

# Добавляем вершину E и ребро E->B
matrix, vertices = add_vertex_to_matrix(matrix, vertices, 'E')
add_edge_to_matrix(matrix, vertices, 'E', 'B')
print("\nПосле добавления E и ребра E->B:")
print("Вершины:", vertices)
for row in matrix:
    print(row)

# 3. Тестирование списка смежности
print("\n3. СПИСОК СМЕЖНОСТИ:")
adj_list = create_adjacency_list(edges)
for vertex, neighbors in sorted(adj_list.items()):
    print(f"{vertex}: {neighbors}")

# Добавляем вершину E и ребро E->B
add_vertex_to_list(adj_list, 'E')
add_edge_to_list(adj_list, 'E', 'B')
print("\nПосле добавления E и ребра E->B:")
for vertex, neighbors in sorted(adj_list.items()):
    print(f"{vertex}: {neighbors}")
