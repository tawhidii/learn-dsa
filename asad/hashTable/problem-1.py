

def name(list1, list2):
    hashMap = {}
    for i in list1:
        hashMap[i] = True
    for i in list2:
        if i in hashMap:
            return True
    return False


a = name([1, 2, 3, 10], [4, 5, 99])

print(a)
