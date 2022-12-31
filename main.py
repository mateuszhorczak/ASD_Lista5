from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, node, visited, end_node, sum_of_weight, result_weight, weights, results_list):
        if node == end_node:
            if sum_of_weight + weights[node] == result_weight:
                results_list.append(node)
                print("koniec - udalo sie")
                print(results_list)
                exit()
            visited = set()

        if sum_of_weight + weights[node] > result_weight:
            return

        if node not in visited:
            if node != end_node:
                visited.add(node)
            sum_of_weight += weights[node]
            results_list.append(node)

            for neighbour in self.graph[node]:
                self.dfs(neighbour, visited, end_node, sum_of_weight, result_weight, weights, results_list)

            sum_of_weight -= weights[results_list[-1]]
            results_list.pop(-1)


if __name__ == '__main__':
    g = Graph()

    data = list(map(int, input().split()))
    number_of_chambers = data[0]  # n - liczba komnat
    number_of_corridors = data[1]  # m - liczba korytarzy
    start_chamber = data[2]  # w - numer konmaty wejsciowej
    end_chamber = data[3]  # k - numer komnaty ksiezniczki
    sum_of_money = data[4]  # s - kasa w sakiewce

    data = list(map(int, input().split()))
    chamber_cost_list = [0]  # oplaty za wejscie do komnat
    for i in range(number_of_chambers):  # wagi komnat dla i-tej kolumny
        chamber_cost_list.append(data[i])

    corridors = []  # korytarze, polaczenia w grafie
    for i in range(number_of_corridors):
        data = list(map(int, input().split()))
        corridors.append(data)  # do usuniecia cale corridors
        g.addEdge(data[0], data[1])
        g.addEdge(data[1], data[0])

    # print(number_of_chambers, number_of_corridors, start_chamber, end_chamber, sum_of_money)
    # print(chamber_cost_list)
    # print(corridors)

    visited_list = set()
    list_with_results = []
    g.dfs(start_chamber, visited_list, end_chamber, 0, sum_of_money, chamber_cost_list, list_with_results)

    # graph = {
    #     '1': ['2', '3', '5'],
    #     '2': ['3', '1', '4'],
    #     '3': ['1', '2'],
    #     '4': ['2', '5'],
    #     '5': ['1', '4']
    # }
