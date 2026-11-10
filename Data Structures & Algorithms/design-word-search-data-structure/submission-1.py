class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def addWord(self, word: str) -> None:
        cur = self
        for c in word:
            index = ord(c) - ord('a')
            if cur.children[index] == None:
                cur.children[index] = WordDictionary()
            cur = cur.children[index]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self
        for i, c in enumerate(word):
            if c == ".":
                for child in cur.children:
                    if child and child.search(word[i+1:]):
                        return True
                return False
            else:
                index = ord(c) - ord('a')
                if cur.children[index] == None:
                    return False
                cur = cur.children[index]
        return cur.isEnd 
        
