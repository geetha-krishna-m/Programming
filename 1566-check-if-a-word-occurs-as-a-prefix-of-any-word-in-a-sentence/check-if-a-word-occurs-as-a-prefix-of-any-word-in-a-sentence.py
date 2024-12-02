class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words_list = sentence.split()
        targetLength = len(searchWord)
        for ind,word in enumerate(words_list):
            sourceWordLength = len(word)
            flag = True
            if(sourceWordLength < targetLength ):
                continue
            for j in range(targetLength):
                if(word[j]!=searchWord[j]):
                    flag = False
                    break
            if(flag):
                return ind+1
        return -1
                