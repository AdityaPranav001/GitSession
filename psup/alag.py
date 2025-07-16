sentence = "My name is adityaaa"
sentence = sentence.split()

i = 0
longest_word = ""

while True:
    if len(sentence[i]) > len(longest_word):
        longest_word = sentence[i]
    i += 1
    if i == len(sentence):
        break

print(f"The longest word in {sentence} is: {longest_word}")
