sentence = input("Enter a sentence: ")

matches = [word for word in sentence.split() if "нн" in word]

if matches:
    print("Words containing 'нн':")
    for word in matches:
        print(word)
else:
    print("No occurrences of 'нн' found.")

