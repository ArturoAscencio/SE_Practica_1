import heapq

def dijkstra(graph, start):
    # Inicializar distancias y conjunto de nodos visitados
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    visited = set()

    # Crear una cola de prioridad (min-heap) para explorar nodos
    priority_queue = [(0, start)]

    while priority_queue:
        # Obtener el nodo con la distancia mínima
        current_distance, current_node = heapq.heappop(priority_queue)

        # Si ya hemos visitado este nodo, continuamos
        if current_node in visited:
            continue

        # Marcar el nodo como visitado
        visited.add(current_node)

        # Explorar los nodos adyacentes
        for neighbor, distance in graph[current_node].items():
            new_distance = current_distance + distance

            # Si encontramos una distancia menor, actualizamos
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return distances

# Ejemplo de uso
graph = {
    'Casa': {'Escuela': 5, 'Trabajo': 10, 'Gimnasio': 3},
    'Escuela': {'Casa': 5, 'Trabajo': 7, 'Gimnasio': 8},
    'Trabajo': {'Casa': 10, 'Escuela': 7, 'Gimnasio': 6},
    'Gimnasio': {'Casa': 3, 'Escuela': 8, 'Trabajo': 6}
}

start_node = 'Gimnasio'
result = dijkstra(graph, start_node)

print("Distancias más cortas desde el punto de inicio (", start_node, "):")
for node, distance in result.items():
    print("Hacia", node, ":", distance, "km")
