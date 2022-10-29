def solution(string):
    count_string = {}
    for value in string:
        if value in count_string:
            count_string[value] +=1
        else:
            count_string[value] = 1
    print(count_string)

solution('hello')