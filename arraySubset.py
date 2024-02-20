def hashElement(array):
    hash = dict()
    for element in array:
        hash[str(element)] = hash.get(str(element), 0) + 1
    return hash


num = [1,2,3,4,5,6,7,7,7,8,9]
print(hashElement(num))