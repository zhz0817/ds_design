def undirected_adjacency_matrix():
    matrix = []
    for i in range(5):
        temp = [0] * 5
        matrix.append(temp)
    matrix[0][1] = 1
    matrix[0][2] = 1
    matrix[1][3] = 1
    matrix[1][4] = 1
    matrix[2][3] = 1
    matrix[3][4] = 1
    for i in range(5):
        for j in range(i + 1, 5):
            if matrix[i][j] == 1:
                matrix[j][i] = 1
    return matrix


def directed_adjacency_matrix():
    matrix = []
    for i in range(5):
        temp = [0] * 5
        matrix.append(temp)
    matrix[0][1] = 1
    matrix[0][2] = 1
    matrix[1][3] = 1
    matrix[1][4] = 1
    matrix[2][3] = 1
    matrix[3][4] = 1
    return matrix


def dfs(graph, index, is_visited):
    for i in range(len(graph[index])):
        if graph[index][i] == 1 and not is_visited[i]:
            print(i)
            is_visited[i] = True
            dfs(graph, i, is_visited)


if __name__ == '__main__':
    graph1 = undirected_adjacency_matrix()
    graph2 = directed_adjacency_matrix()
    is_visited = [False] * 5
    is_visited[0] = True
    print(0)
    dfs(graph1, 0, is_visited)
