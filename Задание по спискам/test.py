"""Задание по спискам:
1.1. Create file with file name test.py
1.2. Create variable x and assign a list ['a', 'b', 'c'] to it.
1.3. Print a string with all elements of this list sepatated with "**" - a**b**c
1.4. Insert "c" letter to the list x on first position and print it.
1.5. Think, how you can remove all duplicated symbols in this list. Print the result.


Задание со звездочкой:
Take a list, say for example this one:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:

1. Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in
it and print out this new list.
2. Write this in one line of Python.
3. Ask the user for a number and return a list that contains only elements from the original list a that are smaller
than that number given by the user."""

x=['a', 'b', 'c']
# отсюда https://stackoverflow.com/questions/22556449/print-a-list-of-space-separated-elements-in-python-3
print(*x, sep='**')
# при insert снеачала указываем на какое место ставим, потом что вставляем
x.insert(0,"c")
print(x)
# удалим все 'c' с помощью цикла while, вконце print(x) подвинули влево дабы не смотреть промежуточный результат
while 'c' in x:
    x.remove('c')
print(x)
# если надо было удалить одно повторяющееся 'c', можно с помощью метода remove удалит первое найденное:
x=['c', 'a', 'b', 'c']
x.remove('c')
print(x)




