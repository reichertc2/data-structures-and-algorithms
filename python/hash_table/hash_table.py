

class HashTableNode():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable():
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.buckets = [None] * self.capacity

    def add(self,key,value):
        pass

    def get(self,key):
        pass

    def contains(self,key):
        pass

    def hash(self,key):
        hashsum = 0
        for idx, value in enumerate(key):
            hashsum += (idx + len(key)) **ord(value)

            hashsum = hashsum % self.capacity

        return hashsum
