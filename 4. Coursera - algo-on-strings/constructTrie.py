class Node:
    def __init__(self, val='root') -> None:
        self.children = [None for x in range(26)]
        self.isEndOfWord = False
        self.val = val


class Trie:
    def __init__(self) -> None:
        self.root = Node()

    def _charToIndex(self, ch):
        return ord(ch)-ord('a')

    def add(self, word):
        currentNode = self.root
        for alphabet in word:
            index = self._charToIndex(alphabet)
            if not currentNode.children[index]:
                currentNode.children[index] = Node(alphabet)
            currentNode = currentNode.children[index]
        currentNode.isEndOfWord = True

    def addList(self, wordsList):
        for word in wordsList:
            self.add(word)

    def _printTrieHelper(self, currentNode, currentString):
        if currentNode.val != 'root':
            currentString += currentNode.val

        if currentNode.isEndOfWord:
            print(currentString)
            return
        for word in currentNode.children:
            if word:
                self._printTrieHelper(word, currentString)

    def printTrie(self):
        currentString = ''
        currentNode = self.root
        self._printTrieHelper(currentNode, currentString)


if __name__ == '__main__':
    trie = Trie()
    trie.addList(['ataga', 'atc', 'gat'])
    trie.printTrie()
