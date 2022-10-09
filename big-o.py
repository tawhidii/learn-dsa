# a = 10000000000000000
# b = 20000000000000000
# c = a + b # O(1)
# print(c)

# array = [2,3,4,5,6,7,8,9,10,1]

# print(array[5]) # O(1)

# def something(n):
#     return n==2 # O(1)

# array = [2,3,4,5,6,7,8,9,10,1]

# # O(n) -> Linear Time Complexity
# def solve(arr,target1,target2,target3):
#     # Linear Search 
#     for val in arr: 
#         if val == target1:
#             return True


#     for val in arr: 
#         if val == target2:
#             return True
#     return False

#     for val in arr: 
#         if val == target3:
#             return True
#     return False


# ans = solve(array,1,5,6)
# print(ans)

nested_arr = [[1,2,3],[4,5,6],[7,8,9]]

#O(n^2) -> Quadratic Time Complexity
for arr in nested_arr:
    for value in arr:
        print(value)



