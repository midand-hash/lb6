sentence = input("Enter a sentence: ")

first_comma = sentence.find(',')
second_comma = sentence.find(',', first_comma + 1)

if first_comma != -1 and second_comma != -1:
    result = sentence[first_comma + 1:second_comma]
elif first_comma != -1:
    result = sentence[first_comma + 1:]
else:
    result = "No commas found in the sentence."

print(f"Result: {result.strip()}")
