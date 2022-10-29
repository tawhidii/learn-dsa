class HashTable:
    def __init__(self,size):
        self.table = [None] * size

    # generate hash 
    def __hash(self,key):
        hash_value = 0
        for letter in key:
            hash_value = (hash_value + ord(letter) * 23) % len(self.table)
        return hash_value

    # set value 
    def set_value(self,key,value):
        address = self.__hash(key)
        if self.table[address] is None:
            self.table[address] = []
        self.table[address].append([key,value])

    # get value
    def get_value(self,key):
        address = self.__hash(key)
        if self.table[address] is not None:
            for i in range(len(self.table[address])):
                if self.table[address][i][0] == key:
                    return self.table[address][i][1]
        return None

    # show keys
    def keys(self):
        all_keys = []
        for i in range(len(self.table)):
            if self.table[i] is not None:
                for j in range(len(self.table[i])):
                    all_keys.append(self.table[i][j][0])
        return all_keys
    
    


    
    
    def show_table(self):
        for idx , value in enumerate(self.table):
            print(f"{idx}:{value}")
    

hash_table = HashTable(10)
hash_table.set_value('banana',100)
hash_table.set_value('apple',220)
hash_table.set_value('komla',90)
hash_table.set_value('komla',190)
print(hash_table.keys())
