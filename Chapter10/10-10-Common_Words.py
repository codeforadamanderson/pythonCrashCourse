def word_count(filename, word):
    with open(filename) as f:
        contents = f.read()
        count = contents.lower().count(word)
        print(f"The word '{word}' occurs approximately "
            f"{count} times in {filename}.")

word_count('moby_dick.txt', 'the')
word_count('moby_dick.txt', 'the ')
word_count('moby_dick.txt', 'whale')
word_count('alice.txt', 'whale')