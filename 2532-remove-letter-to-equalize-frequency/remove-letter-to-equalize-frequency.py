class Solution:
    def equalFrequency(self, word: str) -> bool:
        word_counter = Counter(word)
        # All characters in `word` are the same character, or all characters are different (each only occur once)
        if len(word_counter) == 1 or len(word_counter) == len(word):
            return True
        frequency_counter = Counter(word_counter.values())
        # There are more than 2 type of counts
        if len(frequency_counter) != 2:
            return False
        max_count = max(frequency_counter.keys())
        min_count = min(frequency_counter.keys())
        # 1st Case: The character with different count than others only occur once
        # 2nd Case: The character with different count occur one more time than others
        return min_count == 1 and frequency_counter[min_count] == 1 or max_count - min_count == 1 and frequency_counter[max_count] == 1