import random
import os

class Grafos:
    def __init__(self, grafo):
        self.grafo = grafo
        self.fila = len(grafo)

    def BFS(self, s, t, parent):

        # Marca vertices que no han sido visitados
        visited = [False] * self.fila
        # Create nueva lista para BFS
        queue = [s]
        # Marca la nueva busqueda del nodo como visitada
        visited[s] = True

        while queue:
            u = queue.pop(0)

            for ind, val in enumerate(self.grafo[u]):
                if visited[ind] is False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False

    def FordFulkerson(self, fnte, sum):

        parent = [-1] * self.fila
        max_flow = 0

        while self.BFS(fnte, sum, parent):
            path_flow = float("Inf")
            s = sum
            while s != fnte:
                path_flow = min(path_flow, self.grafo[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            v = sum
            while v != fnte:
                u = parent[v]
                self.grafo[u][v] -= path_flow
                self.grafo[v][u] += path_flow
                v = parent[v]

        return max_flow

numero_de_simulaciones = int(input("¿Cuantas simulaciones quieres hacer?: "))

if numero_de_simulaciones > 0:
    for i in range(numero_de_simulaciones):
        red = []

        for i in range(6):
            lista = []

            for x in range(6):
                lista.append(random.randint(0, 10))
            
            red.append(lista)

        g = Grafos(red)
        fuente = 0
        sumidero = 5

        print("Red:")
        for fila, index in enumerate(red):
            print("  ", index)
        print("Flujo maximo: {} ".format(g.FordFulkerson(fuente, sumidero)))
        print("")
    
    os.system("PAUSE")
else:
    numero_de_simulaciones = int(input("¿Cuantas simulaciones quieres hacer?: "))