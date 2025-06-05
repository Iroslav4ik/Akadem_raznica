import re


def extract_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    hyphen_words = re.findall(r'\b\w+(?:-\w+)+\b', content)

    parentheses_content = re.findall(r'\((.*?)\)', content)

    return hyphen_words, parentheses_content


file_path = 'task1-en.txt'
hyphen_words, parentheses_content = extract_data(file_path)

print("Слова с дефисом:")
for word in hyphen_words:
    print(word)

print("\n" + "_" * 55)

print("\nСодержимое в круглых скобках:")
for item in parentheses_content:
    print(item)