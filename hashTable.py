# creation of
# stock_prices = {}
#
# with open("data/hashData.txt", "r") as f:
#     for line in f:
#         token = line.split(",")
#         stock_prices[token[0]] = float(token[1])
# f.close()
# print(stock_prices)

class HashTable:

    # in here we create empty array for each index, if we have same hash this will solve the issue

    def __init__(self):
        self.max = 100
        self.arr = [[] for i in range(self.max)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max

    def __setitem__(self, key, value):
        hs = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[hs]):
            if len(element) == 2 and element[0] == key:
                self.arr[hs][idx] = (key, value)
                found = True
                break
        if not found:
            self.arr[hs].append((key, value))

    def __getitem__(self, key):
        hs = self.get_hash(key)
        for element in self.arr[hs]:
            if element[0] == key:
                return element[1]
        return None

    def __delitem__(self, key):
        hs = self.get_hash(key)
        for idx, element in enumerate(self.arr[hs]):
            if element[0] == key:
                del self.arr[hs][idx]
                return
        raise Exception("invalid key")


if __name__ == "__main__":
    ht = HashTable()
    ht["march 6"] = 230
    ht["march 6"] = 240
    ht["march 18"] = 210
    ht["march 27"] = 250
    print(ht["march 18"])
    print(ht["march 27"])
    print("-----------------")
    del ht["march 18"]
    print(ht["march 18"])
    print(ht["march 27"])
