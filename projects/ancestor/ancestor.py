def adjacent_list(input_list):
    adjacent_list = {}
    for tuple in input_list:
        if tuple[1] in adjacent_list:
            adjacent_list[tuple[1]].append(tuple[0])
        elif tuple[1] not in adjacent_list:
            adjacent_list[tuple[1]] = tuple[0]
    return adjacent_list
