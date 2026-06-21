from collections import OrderedDict


class LRUMap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = OrderedDict()

    def get(self, key):
        if key not in self.data:
            return None
        else:
            self.data.move_to_end(key)
            return self.data[key]
    def put(self, key, value):
        self.data[key] = value
        self.data.move_to_end(key)

        if len(self.data) > self.capacity:
            self.data.popitem(last=False)
            pass


cache = LRUMap(2)
cache.put("a", 1)
cache.put("b", 2)
print(cache.get("a"))
cache.put("c", 3)
print(cache.get("a"))
print(cache.get("b"))
print(cache.get("c"))

#popitem() usuwa ostatni element - najświeższy
