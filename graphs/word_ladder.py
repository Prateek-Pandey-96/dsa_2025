from typing import List
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque()
        word_set = set()
        for word in wordList:
            word_set.add(word)
        
        queue.append(beginWord)
        level = 0
        while queue:
            size = len(queue)
            level += 1
            while size > 0:
                curr = queue.popleft()
                if curr == endWord:
                    return level
                curr_word = []
                for ch in curr:
                    curr_word.append(ch)

                for j in range(len(curr_word)):
                    ch = curr_word[j]
                    for i in range(26):
                        new_ch = chr(ord('a')+i)
                        if new_ch == ch:
                            continue
                        curr_word[j] = new_ch
                        new_word = ''.join(curr_word)
                        if new_word in word_set:
                            queue.append(new_word)
                            word_set.remove(new_word)
                        curr_word[j] = ch
                size -= 1

        return 0    
