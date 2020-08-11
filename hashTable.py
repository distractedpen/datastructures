#Hash Table Class

class Data():

    def __init__(self, data):
        self.data = data

class HashTable():

    def __init__(self, size):
        self.MAXSIZE = size
        self.t = [None] * self.MAXSIZE
        self.size = 0

##    def __iter__(self):
##        self.i = 0
##        return self
##
##    def __next__(self):
##        n = self.t[self.i]
##        self.i += 1
##        return n

    def getSize(self):
        return self.size
        

    def hashCode(self, data):
        return data % self.MAXSIZE

    def insert(self, data):
        key = self.hashCode(data)
        while self.t[key] != None:
            key += 1
            key %= self.MAXSIZE
            if key == self.hashCode(data):
                return print("Hash Table is Full.")
        self.t[key] = data
        self.size += 1

    def delete(self, data):
        key = self.hashCode(data)
        while self.t[key] != data:
            key += 1
            key %= self.MAXSIZE
            if key == self.hashCode(data):
                return print("{0} Not Found.".format(data))
        self.t[key] = None
        self.size -= 1
                
        

    def lookup(self, data):
        key = self.hashCode(data)

        while True:
            if self.t[key] == data:
                return print("Found {0} at location {1}.".format(self.t[key], key))
            else:
                key += 1
                key %= self.MAXSIZE
                if key == self.hashCode(data):
                    return print("{0} Not Found.".format(data))

    def averageValue(self):
        t_sum = 0
        for i in self.t:
            if i != None:
                t_sum += i
        return t_sum // self.getSize()
    
    def debug(self):
        print(self.t)

#Testing Code
def main():
    table = HashTable(5)
    table.insert(2) #in slot 2
    table.insert(3) #in slot 3
    table.lookup(2)
    table.lookup(3)
    table.insert(1) #in slot 1
    table.insert(6) #in slot 4
    table.lookup(6)
    table.delete(1)
    table.debug()
    table.delete(6)
    table.lookup(6)
    table.delete(4)
if __name__ == "__main__":
    main()
            
                
            

    
