class HashTable:
    def __init__(self,size):
        self.table = [None] * size

    # generate hash 
    def __hash(self,key):
        hash_value = 0
        for letter in key:
            hash_value = (hash_value + ord(letter) * 23) % len(self.table)
        return hash_value

    def set_value(self,key,value):
        address = self.__hash(key)
        if self.table[address] == None:
            self.table[address] = []
        self.table[address].append([key,value])

    
    def show_table(self):
        for idx , value in enumerate(self.table):
            print(f"{idx}:{value}")
    

hash_table = HashTable(10)
hash_table.set_value('banana',100)
hash_table.set_value('apple',220)
hash_table.set_value('komla',90)
hash_table.set_value('komla',90)
hash_table.show_table()