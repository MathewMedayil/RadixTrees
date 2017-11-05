class RadixNode:
    def __init__(self, k=None):
        self.key = k
        self.children = {}

    def __str__(self):
        return self.key

class RadixTree:
    def __init__(self):
        self.root = RadixNode()

    def insert(self, x, k):
        combos = getAllStrings(k)
        for a in combos:
            for b in x.children.keys():
                if a[0] == b[:len(a[0])]:
                    if a[0] != b:
                        x.children[a[0]] = RadixNode(a[0])
                        x.children[a[0]].children[b[len(a[0]):]] = x.children[b]
                        if a[1][len(a[0]):] != '':
                            x.children[a[0]].children[a[1][len(a[0]):]] = RadixNode(a[1][len(a[0]):])
                        del x.children[b]
                    else:
                        self.insert(x.children[b], k[len(a[0]):])
                    return
        x.children[k] = RadixNode(k)

    def search(self, x, k):
        if k == '':
            return True
        for a in getAllStrings(k):
            if a[0] in x.children.keys():
                return self.search(x.children[a[0]], k[len(a[0]):])
        return  False

def getAllStrings(string):
    for a in range(len(string), 0, -1):
        yield (string[:a], string)