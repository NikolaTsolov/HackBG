def sum_matrix(m):
    resault = 0
    for item in m:
        for somthing in item:
            resault += somthing
    return resault

def is_within(m, at):
    if at[0] < 0 or at[0] > len(m):
        return False
    if at[1] < 0 or at[1] > len(m[0]):
        return False
    else:
        return True


def bomb(m, at):
    if not is_within(m, at):
        return m
    bomb_target = m[at[0]][at[1]]
    for i_index in range(0, len(m)):
        for j_index in range(0, len(m[0])):
            if is_within(m, (i_index-1, j_index-1)):
                neighbour = m[i_index-1][j_index-1]
                m[i_index-1][j_index-1] -= min(neighbour, bomb_target)
            if is_within(m, (i_index+1, j_index-1)):
                neighbour = m[i_index+1][j_index-1]
                m[i_index+1][j_index-1] -= min(neighbour, bomb_target)
            if is_within(m, (i_index-1, j_index+1)):
                neighbour = m[i_index-1][j_index+1]
                m[i_index-1][j_index+1] -= min(neighbour, bomb_target)
            if is_within(m, (i_index+1, j_index+1)):
                neighbour = m[i_index+1][j_index+1]
                m[i_index+1][j_index+1] -= min(neighbour, bomb_target)
            if is_within(m, (i_index, j_index-1)):
                neighbour = m[i_index][j_index-1]
                m[i_index][j_index-1] -= min(neighbour, bomb_target)
            if is_within(m, (i_index, j_index+1)):
                neighbour = m[i_index][j_index+1]
                m[i_index][j_index+1] -= min(neighbour, bomb_target)
            if is_within(m, (i_index-1, j_index)):
                neighbour = m[i_index-1][j_index]
                m[i_index-1][j_index] -= min(neighbour, bomb_target)
            if is_within(m, (i_index+1, j_index)):
                neighbour = m[i_index+1][j_index]
                m[i_index+1][j_index] -= min(neighbour, bomb_target)
    return m




def matrix_bombing_plan(m):

    diction = {}
    for i_index in range(0, len(m)):
        for j_index in range(0, len(m[0])):
            bomb_target = bomb(m,(i_index, j_index))
            diction[(i_index, j_index)] = m[i_index][j_index]

    return diction

def main():
    print(matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

if __name__ == '__main__':
    main()
