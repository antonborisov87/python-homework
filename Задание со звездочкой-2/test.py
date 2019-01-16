"""Задание со звездочкой-2:
1. In console run command: python -c “import this”;
2. Grab the output you get, and assign it to a string variable, let’s say “L” in a new python script (you can just copy
-paste the text manually);
3. Take your personal email as a second string and concatenate it with L;
4. Print the length of L;
5. Print the count all the vowels in L;
6. Print each 18th symbol of the string, but do it in case opposite to the original (print A if the letter is a, print
a if A etc.) adding the position of that letter in the string in format like:
o 18,
o 36E
o 54
o 72I
o …"""

L = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""
A = 'antonborisov87@gmail.com'
# в принте не забыть пробел когда соединяем:
print(L + ' ' + A)
print(len(L))
vowels = 0
for i in L:
    if i in 'aeiouy':
        vowels += 1
print(vowels)
