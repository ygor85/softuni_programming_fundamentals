# https://judge.softuni.org/Contests/Practice/Index/1739#2

substring = input()
string = input()

while substring in string:
    string = string.replace(substring, "")
print(string)
