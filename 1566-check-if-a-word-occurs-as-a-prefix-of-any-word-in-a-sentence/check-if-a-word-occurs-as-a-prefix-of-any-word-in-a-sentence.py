class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words_list = sentence.split()
        words_list_length = len(words_list)
        targetLength = len(searchWord)
        for ind in range(words_list_length):
            sourceWordLength = len(words_list[ind])
            j = 0
            if(sourceWordLength < targetLength ):
                continue
            word = words_list[ind]
            while(j<targetLength and word[j] ==searchWord[j]):
                j = j + 1
            if(j == targetLength):
                return ind+1
        return -1
                