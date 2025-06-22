"""
Word occurrences
Estimated time to complete:1 hour
Actual time to complete: 20 mins
"""


def main():
    """Run a word occurrence program"""

word_to_count = {}
text = input("Enter text: ")
for word in text.split():
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1

max_length = max(len(word) for word in word_to_count)

for word in sorted(word_to_count):
    print(f"{word:{max_length}}: {word_to_count[word]}")

main()