words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']


def count_word_frequency(mylist):
    n_d = {}
    for word in mylist:
        n_d[word] = n_d.get(word,0)+1
    return n_d

result = count_word_frequency(words)
print(result)

# Time Complexity = O(n)
# Space Complexity  = O(n)