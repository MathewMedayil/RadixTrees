class RadixNode:
    def __init__(self, k=None):
        self.key = k
        self.children = {}
        self.isLeaf = False

    def __str__(self):
        return self.key

class RadixTree:
    def __init__(self):
        self.root = RadixNode()

    def insert(self, x, k):
        if k == '':
            x.isLeaf = True
            return
        combos = getAllStrings(k)
        for a in combos:
            for b in x.children.keys():
                if a[0] == b[:len(a[0])]:
                    if a[0] != b:
                        x.children[a[0]] = RadixNode(a[0])
                        x.children[a[0]].children[b[len(a[0]):]] = x.children[b]
                        x.children[a[0]].children[b[len(a[0]):]].key = b[len(a[0]):]
                        if a[1][len(a[0]):] != '':
                            x.children[a[0]].children[a[1][len(a[0]):]] = RadixNode(a[1][len(a[0]):])
                            x.children[a[0]].children[a[1][len(a[0]):]].isLeaf = True
                        else:
                            x.children[a[0]].isLeaf = True
                        del x.children[b]
                    else:
                        self.insert(x.children[b], k[len(a[0]):])
                    return
        x.children[k] = RadixNode(k)
        x.children[k].isLeaf = True

    def search(self, x, k):
        if k == '':
            return x.isLeaf
        for a in getAllStrings(k):
            if a[0] in x.children.keys():
                return self.search(x.children[a[0]], k[len(a[0]):])
        return False

    def printTree(self, x, string):
        for a in sorted(x.children.keys()):
            if x.children[a].isLeaf:
                print(string + a)
            self.printTree(x.children[a], string + a)

def getAllStrings(string):
    for a in range(len(string), 0, -1):
        yield (string[:a], string)
