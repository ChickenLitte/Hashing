class ChainMap():
    def __init__(self):
        self.keys = []
        self.vals = []

    def _index(self, key):
        for i, e in enumerate(self.keys):
            if key == e: return i
        return -1
    
    def get(self, key):
        index = self._index(key)
        return self.vals[index] if index >= 0 else None

    def put(self, key, val):
        index = self._index(key)
        if index < 0: 
            self.keys.append(key)
            self.vals.append(val)
        else:
            self.vals[index] = val
    
    def as_tuples(self):
        return [(self.keys[i], self.vals[i]) for i in range(len(self.keys))]
    