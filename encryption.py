# This is the link to this Python Coding Challenge
# https://www.codewars.com/kata/526d42b6526963598d0004db/train/python
userinput = input('encrypt or decrypt: ')
alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz';
# print(userinput)
def encrypt():
    plain_text = input('Type your word: ')
    shift_amount = int(input('Choose a number from 1 to 26:\n'))
    # print(f'{plain_text}, {shift_amount}')
    cipher_text = ''
    for i in plain_text:
        # print(i)
        pos = alphabet.index(i)
        newpos = pos + shift_amount
        # print(pos)
        # print(newpos)
        # print(alphabet[newpos])
        cipher_text += alphabet[newpos]
    print(cipher_text)

def decrypt():
    # print(f'Your input is {userinput}')
    plain_text = input('Type your word: ')
    shift_amount = int(input('Choose a number from 1 to 26:\n'))
    # print(f'{plain_text}, {shift_amount}')
    cipher_text = ''
    for i in plain_text:
        # print(i)
        pos = alphabet.index(i)
        newpos = pos - shift_amount
        # print(pos)
        # print(newpos)
        # print(alphabet[newpos])
        cipher_text += alphabet[newpos]
    print(cipher_text)

if userinput == 'encrypt':
    encrypt()
elif userinput == 'decrypt':
    decrypt()
else:
    print('Invalid Input')
