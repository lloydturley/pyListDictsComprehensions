numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
print(new_list)

name = "Angela"
letters_list = [letter for letter in name]
print(letters_list)

# double if even number
doubled_list = [n * 2 for n in range(1, 5) if n % 2 == 0]
print(doubled_list)

# add if length is less than 5 chars
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_names = [n for n in names if len(n) < 5]
print(short_names)

# allcaps if length is 5 or more chars
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
long_names = [n.upper() for n in names if len(n) > 4]
print(long_names)

# square numbers in list
newest_numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
print([n * n for n in newest_numbers])

# choose the even numbers
list_of_strings = "9,0,32,8,2,8,64,29,42,99".split(',')
first_list = [int(n) for n in list_of_strings]
result = [n for n in first_list if n % 2 == 0]
print(result)

# find duplicates
file1 = "file1.txt"
file2 = "file2.txt"
with open(file1) as list1:
    contents1 = list1.readlines()
contents1b = [n.strip() for n in contents1]
with open(file2) as list2:
    contents2 = list2.readlines()
contents2b = [n.strip() for n in contents1]
#results = [n for n in contents1b if contents1b.__contains__(n)]
results = [int(n) for n in contents1b if n in contents2b]
print(results)
