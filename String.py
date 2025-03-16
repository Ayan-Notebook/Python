sentence = "To change the overall look of your document. To change the look available in the gallery"

word_count = {}
words = sentence.split()

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

for word, count in word_count.items():
    print(f"{word}: {count}")
