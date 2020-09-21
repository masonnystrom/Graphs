"""
vertext - a word

edge - a possible one letter transformation from source vertex to  another vertext

hot --d--> dot
dot --g--> dog

path - series of transformations from source vertext to destination vertext

BUILD GRAPH
- we can create all possible transformations of beginWord and all possible transformations of 
its transformations..But that would waste a lot of memory

- instead what we can do is to find out the next vertex(word) by coming up with all
valid one character transformations and seeing if those are valid vertices to visit (if it's in the word list
then it's a valid vertex)

"""

from collections import deque

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def findLadders(beginWord, endWord, wordList):
    words = set(wordList)
    visited = set()
    queue = deque()
    queue.append([beginWord])
    while len(queue) > 0:
        currPath = queue.popleft() # an array of our the current transformations
        currWord = currPath[-1]:
            continue 
        visited.add(currWord)
        if currWord == endWord:
            return currPath
        # determine which vertices to traverse next

        for i in range(len(currWord)):
            for letter in alphabet:
                transformedWord = currWord[:i] + letter + currWord[i +1] # changing letter for each index in current word
                # determine if word is in the word list (if it's a valid vertext to visit)
                if transformedWord in words:
                    # if in it's a valid transformation
                    #make a new path
                    newPath = list(currPath)
                    newPath.append(transformedWord)
                    queue.append(newPath)
        return []
