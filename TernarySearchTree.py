class Node:
    def __init__(self, data=None):
        """
        Initialize a Node
        :param data=character of the word to be inserted
        """
        self.data = data
        self.right = None
        self.left = None
        self.eq = None


class TernarySearchTree:
    def __init__(self):
        """
        Initialize a Ternary Search Tree
        """
        self.root = Node()
        self.leaf = None

    def _search(self, node, leaf):
        """
        :param node: node at which character is to searched
        :param leaf: the character to be searced
        """
        while node:
            if node.data == leaf:
                return node
            if leaf and node.data and leaf < node.data:
                node = node.left
            else:
                node = node.right
        return None

    def _insert(self, node, leaf):
        """
        :param node:node at which character is to be inserted
        :param leaf:character passed
        """
        if node is None:
            return leaf
        elif leaf.data == node.data:
            return node
        elif leaf.data and node.data and leaf.data < node.data:
            node.left = self._insert(node.left, leaf)
        else:
            node.right = self._insert(node.right, leaf)
        return node

    def insert(self, word):
        """
        inserts the word
        :param word:the word to be insserted
        """
        node = self.root
        for char in word:
            child = self._search(node.eq, char)
            if not child:  # not null
                # create a new node
                child = Node(char)
                node.eq = self._insert(node.eq, child)
            node = child
        if not self._search(node.eq, self.leaf):  # not null
            node.eq = self._insert(node.eq, Node(self.leaf))

    def search(self, word):
        """
        searches for the word
        :param word:the word to be searched
        """
        node = self.root
        for c in word:
            node = self._search(node.eq, c)
            if not node:
                return False
        return self._search(node.eq, self.leaf) is not None

    def _traverse(self, node, leaf):
        """
        traverses from the given node
        :param node:node from where the traversalshoukd start
        :param leaf:the character ehich is at node
        """
        if node:
            for c in self._traverse(node.left, leaf):
                yield c
            if node.data == leaf:
                yield []
            else:
                for c in self._traverse(node.eq, leaf):
                    yield [node.data] + c
            for c in self._traverse(node.right, leaf):
                yield c

    def traverse(self):
        """
        to split the word and traverse
        """
        for w in self._traverse(self.root.eq, self.leaf):
            print(''.join(w))

    def common_prefix(self, chars):
        """
        to find all words in dict with the given prefix
        :param chars:words to chars as their prefix
        """ 
        node = self.root
        buff = []
        for char in chars:
            buff.append(char)
            node = self._search(node.eq, char)
            if not node:
                return
        for x in self._traverse(node.eq, self.leaf):
            yield ''.join(buff + x)


def main():
    tst = TernarySearchTree()
    with open('word_list/words_44k.txt') as dictionary:
        for entry in dictionary.readlines():
            tst.insert(entry.rstrip())
    word = input("Enter a word to check its validity: ")
    if tst.search(word):
        print("Valid word.")
    else:
        print("Invalid word.")
    word = input("Enter the string for autocomplete suggestions: ")
    for item in tst.common_prefix(word):
        print(item)


if __name__ == '__main__':
    main()

