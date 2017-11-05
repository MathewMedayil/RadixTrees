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
        combos = getInstancesForAll(k)
        found = False
        for a in combos:
            for b in x.children.keys():
                if a[0] == b[:len(a[0])]:
                    found = True
                    if a[0] != b:
                        x.children[a[0]] = RadixNode(a[0])
                        x.children[a[0]].children[b[len(a):]] = x.children[b]
                        if a[1][len(a[0]):] != '':
                            x.children[a[0]].children[a[1][len(a[0]):]] = RadixNode(a[1][len(a[0]):])
                        del x.children[b]
                    else:
                        self.insert(x.children[b], k[len(a[0]):])
                    break
            if found:
                break
        if not found:
            x.children[k] = RadixNode(k)

def getInstancesForAll(string):
    for a in range(len(string), 0, -1):
        yield (string[:a], string)

def main():
    R = RadixTree()
    R.insert(R.root, 'hey')
    R.insert(R.root, 'hello')
    R.insert(R.root, 'hi')
    R.insert(R.root, 'tail')
    R.insert(R.root, 'tailored')
    R.insert(R.root, 'tailor')
    R.insert(R.root, 'tailoring')
    R.insert(R.root, 'wow')
    R.insert(R.root, 'wonderful')
    print(R.root.children)
    print(R.root.children['tail'].children['or'].children)

if __name__ == '__main__':
    main()