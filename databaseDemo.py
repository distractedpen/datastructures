#Small Database Class
#Adds Data to a BST and a Hash Table

from BST import BinarySearchTree as bst
from hashTable import HashTable as ht
import random as rnd
import time

class Database():

    def __init__(self, size):
        self.MAXSIZE = size
        self.tree = bst()
        self.table = ht(self.MAXSIZE)

    def getSize(self):
        return self.table.getSize()

    def insert(self, data):
        self.tree.insert(data)
        self.table.insert(data)

    def lookup(self, data):
        self.table.lookup(data)

    def display(self):
        self.tree.printTree()

    def averageValue(self):
        return self.table.averageValue()

    def maxValue(self):
        return self.tree.maxValue()

    def minValue(self):
        return self.tree.minValue()


def main():
  limit = 100
  db = Database(limit)

  start_time = time.time()
  for i in range(limit):
      db.insert(int(rnd.random() * 100))
  end_time = time.time()
  print("Inserted {0} values in {1} seconds.".format(db.getSize(), end_time - start_time))
  
  start_time = time.time()
  db.display()
  end_time = time.time()
  print("Displayed values in {0} seconds.".format(end_time - start_time))
  start_time = time.time()
  print("Average Value: ", db.averageValue())
  end_time = time.time()
  print("Calculated average value in {0} seconds.".format(end_time - start_time))
  start_time = time.time()
  print("Min Value: ", db.minValue())
  end_time = time.time()
  print("Caculated min value in {0} seconds.".format(end_time - start_time))
  start_time = time.time()
  print("Max Value: ", db.maxValue())
  end_time = time.time()
  print("Calculated max value in {0} seconds.".format(end_time - start_time))


if __name__ == "__main__":
    main()
