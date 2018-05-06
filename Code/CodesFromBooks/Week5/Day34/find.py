def find(target,items):
    return occurrences(target,items)>0

def occurrences(target,items):
    counter = 0
    for elem in items:
        if elem is target:
            counter+=1
    return counter
    