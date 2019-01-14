"""Задание по строкам:
1.1. Create file with file name test.py
1.2. Create variable x and assign "London has a diverse range of people and cultures, and more than 300 languages are
spoken in the region." string to it.
1.3. Print this string with all letters uppercase.
1.4. Print this string the index of first "c" letter in this string.
1.5. Print the count of "o" letters in this string.
1.6. Print a list of all words in this string. Should be - ['London', 'has', 'a', 'diverse', 'range', 'of', 'people',
'and', 'cultures,', 'and', 'more', 'than', '300', 'languages', 'are', 'spoken', 'in', 'the', 'region.']
1.7. Replace all "a" letters with "A" in this string."""

x = "London has a diverse range of people and cultures, and more than 300 languages are spoken in the region."
print(x.upper())
print(x.find('c'))
print(x.count('o'))
a = x.split()
print(a)
print(x.replace('a', 'A'))
