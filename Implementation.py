from Radix import *

def main():
    R = RadixTree()
    R.insert(R.root, 'hey')
    R.insert(R.root, 'hello')
    R.insert(R.root, 'hi')
    R.insert(R.root, 'tailor')
    R.insert(R.root, 'tailored')
    R.insert(R.root, 'tail')
    R.insert(R.root, 'tailoring')
    R.insert(R.root, 'wow')
    R.insert(R.root, 'wonderful')
    R.insert(R.root, 'he')
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
    R.printTree(R.root, "")

if __name__ == '__main__':
    main()
