def filter(list, object):
    filtered_list = []
    for i in list:
        if i == object:
            filtered_list.append(i)
    return filtered_list


def exclude(list, object):
    lenght = len(list)
    for i in range(lenght-1, -1, -1):
        if list[i] == object:
            list.pop(i)
    return list

def unique(list):
    lenght = len(list)
    unique_list = []
    for i in range(lenght-1, -1, -1):
        if list[i] in unique_list:
            list.pop(i)
        else:
            unique_list.append(list[i])
    return unique_list

list = ["d", "d", "d", "v", "r", 4, 6]

print unique(list)

