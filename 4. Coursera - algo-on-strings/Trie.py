class Node:
    def __init__(self, val='root') -> None:
        self.children = [None for x in range(26)]
        self.isEndOfWord = False


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
                currentNode.children[index] = Node()
            currentNode = currentNode.children[index]
        currentNode.isEndOfWord = True

    def addList(self, wordsList):
        for word in wordsList:
            self.add(word)

    def _printTrieHelper(self, currentNode, currentString, currentIndex):
        # if currentNode.val != 'root':
        #     currentString += currentNode.val
        if currentNode != self.root:
            currentString += chr(ord('a')+currentIndex)
        if currentNode.isEndOfWord:
            print(currentString)
            return
        for index in range(len(currentNode.children)):
            if currentNode.children[index]:
                self._printTrieHelper(
                    currentNode.children[index], currentString, index)

    def printTrie(self):
        currentString = ''
        currentNode = self.root
        self._printTrieHelper(currentNode, currentString, 0)

    def find(self, string):
        currentIndex = 0
        currentNode = self.root
        while currentIndex != len(string):
            if not currentNode.children[self._charToIndex(string[currentIndex])]:
                print(False)
                return False
            else:
                currentNode = currentNode.children[self._charToIndex(
                    string[currentIndex])]
                currentIndex += 1
        if currentNode.isEndOfWord:
            print(True)
            return True
        print(False)
        return False

    def trieMatching(self, string):
        startIndex = 0
        while startIndex < len(string):
            for endIndex in range(len(string[startIndex:])):
                isPresent = self.find(string[startIndex:startIndex+endIndex])
                if isPresent:
                    print(string[startIndex:startIndex+endIndex], 'is present')

            startIndex += 1


if __name__ == '__main__':
    trie = Trie()
    trie.addList(['atcg', 'gggt'])
    trie.printTrie()
    trie.find('gg')
    trie.trieMatching('aatcgggttcaatcggggt')
