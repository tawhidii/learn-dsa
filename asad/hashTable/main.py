

class HashTable:
    def __init__(self, size) -> None:
        self.table = [None] * size

    def __hash(self, key) -> int:
        hashKey = ''
        hashKey = ord(key[0]) % len(self.table)
        return hashKey

    def add(self, key, value):
        address = self.__hash(key)
        if self.table[address] is None:
            self.table[address] = list()
        self.table[address].append([key, value])

    def find(self, key) -> int:
        address = self.__hash(key)
        if self.table[address] is not None:
            return self.table[address][len(self.table[address])-1][1]

    def showTable(self) -> list():
        table = list()
        # for key, value in enumerate(self.table):
        #     table.append([key, value])
        # return table
        return self.table

    def showKeys(self) -> list():
        keys = list()
        for key, value in enumerate(self.table):
            if value is not None:
                for val in value:
                    keys.append(val)
        return keys

    def remove(self, key):
        address = self.__hash(key)
        self.table[address] = None


hashTable = HashTable(10)
hashTable.add('sohel', 50)
hashTable.add('arif', 5550)
hashTable.add('bellal', 70)
hashTable.add('manob', 40)
print(hashTable.remove('sohel'))
print(hashTable.showTable())

