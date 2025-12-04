class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        i = self.hash(key)
        for item in self.table[i]:
            if item[0] == key:
                item[1] = value
                return
        self.table[i].append([key, value])

    def get(self, key):
        i = self.hash(key)
        for item in self.table[i]:
            if item[0] == key:
                return item[1]
        return None

    def delete(self, key):
        i = self.hash(key)
        for j, item in enumerate(self.table[i]):
            if item[0] == key:
                self.table[i].pop(j)
                return True
        return False


ht = HashTable(5)
ht.insert("name", "john")
ht.insert("age", "20")
ht.insert("city", "kyiv")

print(ht.get("name"))
print(ht.get("age"))

ht.delete("age")
print(ht.get("age"))
print(ht.delete("unknown"))
