correct_word1 = "прроцесор".replace("рр", "р").replace("с", "сс")  # Исправление слова "прроцесор"
correct_phrase1 = "теекстовыйфайл".replace("ее", "е").replace("ыйфайл", "ый файл")  # Исправление фразы "теекстовыйфайл"
correct_phrase2 = "програма и аллгоритм".replace("мм", "м").replace("лл", "л").replace("програма", "программа")  # Исправление фразы "програма и аллгоритм"
correct_phrase3 = "процесор и паммять".replace("с", "сс").replace("мм", "м")  # Исправление фразы "процесор и паммять"

print(f"Исправленное слово: {correct_word1}")
print(f"Исправленная фраза 1: {correct_phrase1}")
print(f"Исправленная фраза 2: {correct_phrase2}")
print(f"Исправленная фраза 3: {correct_phrase3}")
