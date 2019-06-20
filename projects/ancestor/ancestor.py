def adjacent_list(input_list):
    adjacent_list = {}
    for tuple in input_list:
        if tuple[1] in adjacent_list:
            adjacent_list[tuple[1]].append(tuple[0])
        elif tuple[1] not in adjacent_list:
            adjacent_list[tuple[1]] = tuple[0]
    return adjacent_list


def earliest_ancestor(test_ancestors, starting_vertex):
    adjacency_list = adjacent_list(test_ancestors)
    visited = set()
    stack = []
    stack.append([starting_vertex])
    possible_paths = []
    while len(stack) > 0:
        path = stack.pop()
        vertex = path[-1]
        count = 0
        if vertex not in visited:
            visited.add(vertex)
            if vertex in adjacency_list.keys():
                for neighbor in adjacency_list[vertex]:
                    if neighbor == None:
                        pass
                    else:
                        path_copy = path.copy()
                        path_copy.append(neighbor)
                        stack.append(path_copy)
            else:
                possible_paths.append(path)
    correct_path = possible_paths[0]
    for possible_path in possible_paths:
        if len(possible_path) > len(correct_path):
            correct_path = possible_path
        elif possible_path[0] < correct_path[0]:
            correct_path = possible_path
    return correct_path


test_ancestors = [
    (1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
    (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

adjacent_list(test_ancestors)

earliest_ancestor(test_ancestors, 6)
