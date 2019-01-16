"""Задание по спискам:
1.1. Create file with file name test.py
1.2. Create variable x and assign a list ['a', 'b', 'c'] to it.
1.3. Print a string with all elements of this list sepatated with "**" - a**b**c
1.4. Insert "c" letter to the list x on first position and print it.
1.5. Think, how you can remove all duplicated symbols in this list. Print the result."""

x = ['a', 'b', 'c']
print(x)
# отсюда https://stackoverflow.com/questions/22556449/print-a-list-of-space-separated-elements-in-python-3
print(*x, sep='**')
# при insert сначала указываем на какое место ставим, потом что вставляем
x.insert(0, "c")
print(x)
# удалим все 'c' с помощью цикла while, вконце print(x) подвинули влево дабы не смотреть промежуточный результат
while 'c' in x:
    x.remove('c')
print(x)
