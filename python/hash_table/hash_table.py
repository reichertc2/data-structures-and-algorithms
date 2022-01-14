

class Node():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable():
    def __init__(self, capacity=1024):
        self.capacity = capacity
        self.size = 0
        self.buckets = [None] * self.capacity

    def add(self,key,value=None):
        self.size += 1
        index = self.hash(key)
        node = self.buckets[index]
        if node is None:
            self.buckets[index] = Node (key,value)
            return
        prev = node

        while node is not None:
            prev = node
            node = node.next

        prev.next = Node(key,value)

    def get(self,key):
        index = self.hash(key)

        node = self.buckets[index]

        while node is not None:
            node = node.next

        if node is None:
            return None

        else:
            return node.value

    def contains(self,key):

        index = self.hash(key)
        node = self.buckets[index]

        if node is None:
            return False


        while node is not None:
            if node.key == key:
                return True

            node = node.next

        return False


    def hash(self,key):
        hashsum = 0
        for idx, value in enumerate(str(key)):
            hashsum += (idx + len(str(key))) **ord(value)

            hashsum = hashsum % self.capacity

        return hashsum
