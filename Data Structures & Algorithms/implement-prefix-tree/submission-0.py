class PrefixTree:

    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def insert(self, word: str) -> None:
        cur = self
        for c in word:
            carId = ord(c) - ord('a')
            if cur.children[carId] == None:
                newNode = PrefixTree()
                cur.children[carId] = newNode
            cur = cur.children[carId]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self
        for c in word:
            carId = ord(c) - ord('a')
            if cur.children[carId] == None:
                return False
            cur = cur.children[carId]
        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self
        for c in prefix:
            carId = ord(c) - ord('a')
            if cur.children[carId] == None:
                return False
            cur = cur.children[carId]
        return True
        
        