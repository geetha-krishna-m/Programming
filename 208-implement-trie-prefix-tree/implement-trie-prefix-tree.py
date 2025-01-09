class TrieNode:
    def __init__(self):
        self.dicti = dict()
        self.end = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str) -> None:
        trieNode = self.root
        for i in word:
            if(i not in trieNode.dicti):
                trieNode.dicti[i] = TrieNode()
            trieNode = trieNode.dicti[i]
        trieNode.end = True

    def search(self, word: str) -> bool:
        trieNode = self.root
        for i in word:
            if(i not in trieNode.dicti):
                return False
            trieNode = trieNode.dicti[i]
        if(trieNode.end==True):
            return True
        return False
     

    def startsWith(self, prefix: str) -> bool:
        trieNode = self.root
        for i in prefix:
            if(i not in trieNode.dicti):
                return False
            trieNode = trieNode.dicti[i]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)