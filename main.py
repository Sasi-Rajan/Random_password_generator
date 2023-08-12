import random
inp_characters = int(input("How many characters do you need "))
inp_symbols = int(input("How many symbols do you need "))
inp_numbers = int(input("How many numbers do you need "))

character = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z',
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']
symbol=['!','#','$','^','(',')','&']
number=['1','2','3','4','5','6','7','8','9','10']

empty=[]

for i in range (inp_characters):
    empty.append(random.choice(character))
for j in range (inp_numbers):
    empty.append(random.choice(number))
for k in range (inp_symbols):
    empty.append(random.choice(symbol))

random.shuffle(empty)

password="".join(empty)
print(f"Your generated password is {password}")