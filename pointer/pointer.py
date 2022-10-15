# num_one  = 10
# num_two = num_one
# print(id(num_one))
# print(id(num_two))

# num_one = 20
# print(num_one)
# print(num_two)


dict_one = {"value":100}
dict_two = dict_one
# print(dict_one)
# print(dict_two)
dict_two['value'] = 200
dict_three = {"value": 500}
dict_one = dict_three
dict_two = dict_three
print(dict_one,dict_two,dict_three)

# print(dict_one)
# print(dict_two)

#[<QureySet:....>,]