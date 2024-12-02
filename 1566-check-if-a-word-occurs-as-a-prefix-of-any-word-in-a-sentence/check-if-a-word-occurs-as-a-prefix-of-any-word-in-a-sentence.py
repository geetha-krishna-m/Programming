from collections import defaultdict
class Trie:
    def __init__(self):
        self.trie = defaultdict(Trie)
        self.isEnd = False
class Solution:
    def __init__(self):
        self.root = Trie()
    def add(self,word):
        curr = self.root
        for c in word:
            if c not in curr.trie:
                curr.trie[c] = Trie()
            curr = curr.trie[c]
        curr.isEnd = True
    def checkPrefixMatch(self,word):
        curr = self.root
        for c in word:
            if curr.isEnd:
                return True
            if c not in curr.trie:
                return False
            curr = curr.trie[c]
        return curr.isEnd
            


    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words_list = sentence.split()

        self.add(searchWord)

        for ind in range(len(words_list)):
           if(self.checkPrefixMatch(words_list[ind])):
            return ind+1
        return -1
                