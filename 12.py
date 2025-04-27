class HashTableChaining:
    def __init__(self, size=5): 
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def get(self, key):
        index = self.hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

h1 = HashTableChaining()   # No error because size has default 5
h1.insert(1, 'A')
print(h1.get(1))  # Output: A
h1.insert(6, 'B')
print(h1.get(6))  # Output: B
h1.insert(1, 'C')  # Update value for key 1
print(h1.get(1))  # Output: C (updated value)
h1.insert(2, 'D')
print(h1.get(2))  # Output: D (new value for key 2)\
