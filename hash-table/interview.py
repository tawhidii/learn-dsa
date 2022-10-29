# def common_item(list_one,list_two):
#     for i in list_one:
#         for j in list_two:
#             if i==j:
#                 return True
#     return False




# ans = common_item([3,7,10],[1,7,10])
# print(ans)


def common_item(list_one,list_two):
    my_hash_map = {}
    for i in list_one:
        my_hash_map[i] = True
        
    for j in list_two:
        if j in my_hash_map:
            return True
    return False


ans = common_item([3,7,10],[1,7,10])
print(ans)