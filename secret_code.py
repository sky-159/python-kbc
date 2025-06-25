# SECRET CODE
import random
import string


def coding():
    code = input("Enter the text you want to code:\n")
    l_code = code.split()
    l_code_final = []
    for i in range(len(l_code)):
        code_str = str(l_code[i])
        if (len(code_str) <= 2):
            rev_code_str = code_str[::-1]
            l_code_final.append(rev_code_str)
        else:
            first_c = code_str[1:]
            second_c = code_str[0]
            alphabets = string.ascii_letters
            first_3 = random.choice(
                alphabets) + random.choice(alphabets) + random.choice(alphabets)
            last_3 = random.choice(
                alphabets) + random.choice(alphabets) + random.choice(alphabets)
            l_code_final.append(first_3 + first_c + second_c + last_3)
    for i in l_code_final:
        print(i, end=" ")


def decoding():
    decode = input("Enter the text you want to decode:\n")
    l_decode = decode.split()
    l_decode_final = []
    for i in range(len(l_decode)):
        decode_str = str(l_decode[i])
        if (len(decode_str) <= 2):
            rev_decode_str = decode_str[::-1]
            l_decode_final.append(rev_decode_str)
        else:
            del_leters = decode_str[3:-3]
            first_d = del_leters[-1]
            second_d = del_leters[:-1]
            l_decode_final.append(first_d + second_d)
    for i in l_decode_final:
        print(i, end=" ")


para = '''
What do you want to do?
1. Have a text CODED.
2. Have a text DE-CODED.
'''
print(para)

while True:
    try:
        choice = int(input("Enter your choice: "))
        if (choice == 1 or choice == 2):
            break
        else:
            print("Enter 1 or 2")
    except ValueError:
        print("Invalid input. Enter 1 or 2")
    except Exception as e:
        print(f"Unexcepted error occured {e}")

if choice == 1:
    coding()
else:
    decoding()
