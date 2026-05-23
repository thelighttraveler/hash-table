class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, str):
        index_order = 0
        for s in str:
            index_order += ord(s)
        return index_order

    def add(self, key, value):
        hash_result = self.hash(key)
        if hash_result in self.collection:
            self.collection[hash_result].update({key: value})
        else:
            self.collection[hash_result] = {key: value}

    def remove(self, key):
        hash_result = self.hash(key)
        if hash_result in self.collection:
            if key in self.collection[hash_result]:
                return self.collection[hash_result].pop(key)
            else:
                return None

    def lookup(self, key):
        hash_result = self.hash(key)
        if hash_result in self.collection:
            if key in self.collection[hash_result]:
                return self.collection[hash_result][key]
            else:
                return None