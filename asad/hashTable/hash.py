from collections import Counter
from enum import Flag


magazine = 'give me one grand today night'
note = 'give one grand today'


def checkMagazine(magazine, note):
    magazineHash = {}
    flag = True
    for val in note:
        if val not in magazine:
            print("Nope")
            return

    for val in magazine:
        if val in magazineHash:
            magazineHash[val] += 1
            continue
        magazineHash[val] = 1

    for value in note:
        if value in magazineHash:
            magazineHash[value] -= 1
    for v in magazineHash:
        if magazineHash[v] < 0:
            flag = False
            break
    print("Yes" if flag else "No")


# def checkMagazine(magazine, note):
#     magazines = {}
#     notes = {}
#     magazines = Counter(magazine)
#     notes = Counter(note)
#     print(magazines)
#     result = notes - magazines

#     if result == {}:
#         print('Yes')
#         return
#     print('No')


# def checkMagazine(magazine, note):
#     magazine = magazine.split(' ')
#     note = note.split(' ')
#     magDict = {}
#     noteDict = {}
#     for data in magazine:
#         if data in magDict.keys():
#             magDict[data] = (magDict[data])+1
#             continue
#         magDict.update({data: 1})

#     for data in note:
#         if data in noteDict.keys():
#             noteDict[data] = (noteDict[data])+1
#             continue
#         noteDict.update({data: 1})
#     for k, v in noteDict.items():
#         if k in magDict.keys():
#             if v != magDict[k]:
#                 print('No')
#                 return
#         else:
#             print('No')
#             return
#     print('Yes')
#     return
print(checkMagazine(magazine, note))
