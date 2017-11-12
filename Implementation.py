from Radix import *

def main():
    R = RadixTree()
    names=['hey','wow','hi','tailor','tailored','tail','tailoreing','he','wonderful','hello']
    for name in names:
        R.insert(R.root,name)
    print(R.root.children)
    print(R.root.children['h'].children['e'].children)
    print(R.root.children['tail'].children)
    print(R.root.children['tail'].children['or'].children)
    print(R.root.children['wo'].children)
    print(R.search(R.root, "wow"))
    print(R.search(R.root, "wo"))
    print(R.search(R.root, "he"))
    print(R.search(R.root, "tail"))
    print(R.search(R.root, "tailored"))
    print(R.printTree(names,0))

if __name__ == '__main__':
    main()
