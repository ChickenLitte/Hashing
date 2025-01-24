#Implement the class OpenAddressingHashTable using linear probing. How does its runtime compare to the hashmap with separate chaining?
import ChainMap

class LinearProbe:
    def __init__(self, hash_fn):
        self.buckets = [ChainMap.ChainMap() for _ in range(100)]
        self.hash = hash_fn
        self._n = 100
        self._sz = 0
        print(self._sz)
    
    def _bucket(self, key):
        return self.hash(key) % self._n

    def put(self, key, val):

        if self._bucket(key) == None:
            bucket = self._bucket(key)
            bucket.put(key, val)
            self._sz += 1
        else:
            k = self._bucket(key)
            while self._bucket(key) != None:
                if k < self._sz:
                    k += 1
                else:
                    k = 0
            bucket = k
            bucket.put(key, val)
            self._sz += 1

        if self._sz >= (self._n * (2/3)):
            self._double()
    
    def get(self, key):
        p =0

        bucket = self._bucket(key)

        if bucket.get(key) == self.val:
            return bucket.get(key)
        
        while bucket.get(key) != self.val:
            k = self._bucket(key)
            if k < self._sz:
                k += 1
            else:
                k = 0
            
            if (bucket.get(key)) == None:
                return None
        
        return bucket.get(k)

    def _double(self):
        old_buckets = self.buckets
        self._n *= 2
        self.buckets = [ChainMap.ChainMap() for _ in range(self._n)]

        for bucket in old_buckets:
            for key, val in bucket.as_tuples():
                self.put(key, val)

def hash_fn(x,mod = 100):
    combinedVal = 0
    for char in x:
        combinedVal += ord(char)
    print(combinedVal)
    return combinedVal

def main():
    LP = LinearProbe(hash_fn)
    LP.put('h','i')

if __name__ == "__main__":
    main()
