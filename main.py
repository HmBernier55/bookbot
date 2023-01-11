with open("books/frankenstein.txt") as f:
    file_contents = f.read()

def word_count(book):
    words = book.split()
    count = len(words)
    return count

def letter_count(book):
    words = book.split()
    letters = {}
    for word in words:
        for letter in word.lower():
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    return letters


print(f"--- Begin report of books/frankenstein.txt ---")
print(f"{word_count(file_contents)} words found in the document\n")


letters = letter_count(file_contents)
letter_list = []
for letter in letters:
    if letter.isalpha():
        letter_list.append((letters[letter], letter))
letter_list.sort(reverse=True)

for i in letter_list:
    print(f"The {i[1]} character was found {i[0]} times")

print(f"--- End report ---")