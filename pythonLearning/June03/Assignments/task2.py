# Task 2:
# Use Python's re module to find all occurrences of the word "Python" in a given text.

import re

text = "python is awesome because python is used everywhere, python is easy to learn and python has huge library."

word = "python"

count = len(re.findall(word, text))

print(f'In given text "{text}" the word "{word}" is occurred {count} times.')
