"""
Given two words (begin_word and end_word), and a dictionary's word list, return the shortest transformation sequence from begin_word to end_word, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. 
Note that begin_word is not a transformed word.

Note:
Return None if there is no such transformation sequence.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume begin_word and end_word are non-empty and are not the same.


Sample:
begin_word = "hit"
end_word = "cog"
return: ['hit', 'hot', 'cot', 'cog']

begin_word = "sail"
end_word = "boat"
['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']

beginWord = "hungry"
endWord = "happy"
None
"""

from day1 import Graph, Queue
import string

#get the words from a file into a set 
words = set()
with open('words.txt') as f:
    for w in f:
        w = w.strip()
        words.add(w)
        
#create a graph with the words as nodes connected to neighbors that are words that differ by 1 letter 

#gets all words that differ by 1 into neighbor list
#total runtime complexity --> O(26680n) over length of word
def get_neighbors1(word):
    neighbors = []
    for w in words: #O(n) for number of words
        if len(w) == len(word):
            diff_count = 0
            
            for i in range(len(w)): #O(n) over length of word 
                if w[i] != word[i]:
                    diff_count += 1
                if diff_count > 1:
                    break
                
            if diff_count == 1:
                neighbors.append(w)
                
    return neighbors

#for each letter in the word switch with each letter in the alphabet and checking if the word is in the dictionary
#total runtime complexity --> O(26n) over length of word
def get_neighbors(word):
    neighbors = []
    #possible letters a-z
    alphabet = list(string.ascii_lowercase)
    
    word_letters = list(word)
    
    for i in range(len(word_letters)): #O(n) over length of the word
        for a in alphabet: #O(26)
            word_letters_copy = list(word_letters)
            word_letters_copy[i] = a
            candidate_word = "".join(word_letters_copy)
            
            if candidate_word != word and candidate_word in words:
                neighbors.append(candidate_word)
    
    return neighbors
                

def bfs(begin_word, end_word):
    visited = set()
    q = Queue()
    
    q.enqueue([begin_word])
    
    while q.size() > 0:
        path = q.dequeue()
        last_word = path[-1]
        
        if last_word not in visited:
            visited.add(last_word)
            
            if last_word == end_word:
                return path
            
            for neighbor in get_neighbors(last_word):
                path_copy = path + [neighbor]
                q.enqueue(path_copy)
                
print(bfs('four', 'door'))