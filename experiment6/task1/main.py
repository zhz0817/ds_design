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


def undirected_adjacency_list():
    adjacency_list = []
    for i in range(5):
        adjacency_list.append([i])
    adjacency_list[0].append(1)
    adjacency_list[1].append(0)
    adjacency_list[0].append(2)
    adjacency_list[2].append(0)
    adjacency_list[1].append(3)
    adjacency_list[3].append(1)
    adjacency_list[1].append(4)
    adjacency_list[4].append(1)
    adjacency_list[2].append(3)
    adjacency_list[3].append(2)
    adjacency_list[3].append(4)
    adjacency_list[4].append(3)


def directed_adjacency_list():
    adjacency_list = []
    for i in range(5):
        adjacency_list.append([i])
    adjacency_list[0].append(1)
    adjacency_list[0].append(2)
    adjacency_list[1].append(3)
    adjacency_list[1].append(4)
    adjacency_list[2].append(3)
    adjacency_list[3].append(4)


if __name__ == '__main__':
    undirected_adjacency_matrix()  # 无向图邻接矩阵
    directed_adjacency_matrix()  # 有向图邻接矩阵
    undirected_adjacency_list()  # 无向图邻接表
    directed_adjacency_list()  # 有向图邻接表
