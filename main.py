numbers = [1,2,3]
new_list = [n+1 for n in numbers]
print(new_list)

name = "Angela"
letters_list = [letter for letter in name]
print(letters_list)

#double if even number
doubled_list = [n*2 for n in range(1,5) if n%2==0]
print(doubled_list)

#add if length is less than 5 chars
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_names = [n for n in names if len(n)<5]
print(short_names)

#allcaps if length is 5 or more chars
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
long_names = [n.upper() for n in names if len(n)>4]
print(long_names)

#square numbers in list
newest_numbers=[1,1,2,3,5,8,13,21,34,55]
print([n*n for n in newest_numbers])


