class Node:
    def __init__(self, k=None):
        """
        Initialize a Trie node
        """
        self.key = k
        self.children = {}
        self.isWord = False
        self.parent = None

class Trie:
    def __init__(self):
        """
        Initialize a Trie
        """
        self.root = Node()

    def insert(self, word):
        """
        Insert a string in the Trie
        :param word: string which is to be inserted
        :return: None
        """
        currentNode = self.root
        for letter in word:
            newKey = ord(letter) - ord('a')
            if newKey not in currentNode.children.keys():
                currentNode.children[newKey] = Node(letter)
            currentNode.children[newKey].parent = currentNode
            currentNode = currentNode.children[newKey]
        currentNode.isWord = True

    def search(self, word):
        """
        Search for string in the Trie
        :param word: string which is to be searched for
        :return: Boolean
        """
        currentNode = self.root
        for letter in word:
            newKey = ord(letter) - ord('a')
            if newKey not in currentNode.children.keys():
                return False
            currentNode = currentNode.children[newKey]
        return currentNode.isWord


def main():
    T = Trie()
    with open('word_list/words_44k.txt') as dictionary:
        for entry in dictionary.readlines():
            T.insert(entry.rstrip())
    word = input("Enter a word to check its validity: ")
    if T.search(word):
        print("Valid word.")
    else:
        print("Invalid word.")


if __name__ == '__main__':
    main()

