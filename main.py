from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, node, end_node, sum_of_weight, result_weight, weights, results_list):
        if node == end_node:
            if sum_of_weight + weights[node] == result_weight:
                results_list.append(node)
                print(results_list)
                exit()

        if sum_of_weight + weights[node] > result_weight:
            return

        if node != end_node:
            sum_of_weight += weights[node]
            results_list.append(node)

            for neighbour in self.graph[node]:
                self.dfs(neighbour, end_node, sum_of_weight, result_weight, weights, results_list)

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

    for i in range(number_of_corridors):
        data = list(map(int, input().split()))
        g.addEdge(data[0], data[1])
        g.addEdge(data[1], data[0])

    list_with_results = []
    g.dfs(start_chamber, end_chamber, 0, sum_of_money, chamber_cost_list, list_with_results)
