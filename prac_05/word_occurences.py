"""
Word Occurrences
Estimate: 1 hour
Actual: 2 hours
"""

occurrences_count = {}
text_string = input("Enter string: ")
words = text_string.split()
for word in words:
    frequency = occurrences_count.get(word, 0)
    occurrences_count[word] = frequency + 1
words = list(occurrences_count.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print(f"{word:{max_length}} : {occurrences_count[word]}")
