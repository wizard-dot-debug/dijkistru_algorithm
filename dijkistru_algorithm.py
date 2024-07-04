def dijkistru(a,b,c = ''):
    unvisited = list(a)
    distances = {i : 0 if i == b else float('inf') for i in a}
    #distances has to be a dict beacuse i is the element of a list therefore it can't have value
    paths = {i :[] for i in a}
    paths[b].append(b)
    # return paths

    while unvisited:
        in_process = min(unvisited, key=distances.get)
        for i ,j in a[in_process]:
            new_distance = distances[in_process] + j
            if new_distance < distances[i]:
                distances[i] = new_distance
                if paths[i] and paths[i][-1] == i:
                    paths[i] = paths[in_process][:]
                else:
                    paths[i].extend(paths[in_process])
                paths[i].append(i)
        unvisited.remove(in_process)
    
    target = [c] if c else a
    for i in target:
        if i == b:
            continue
        else:
            print(f'Distance of {b}-{i} is : {distances[i]}\npath is : {'-'.join(paths[i])}')
    return distances,paths


my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C',1 ), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}


dijkistru(my_graph,'A','F')
