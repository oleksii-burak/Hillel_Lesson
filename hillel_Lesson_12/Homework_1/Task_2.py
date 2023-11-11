def longest_words(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
    max_length = max(len(word) for word in words)
    longest = [word for word in words if len(word) == max_length]
    return longest

# Використання функції
print(longest_words("article.txt"))
