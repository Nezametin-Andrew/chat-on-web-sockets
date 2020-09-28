import random
import string



letter = string.ascii_letters
letter_Uper = []
letter_Smol = []
lst_Name = []


for i in range(len(letter) // 2):
    letter_Smol.append(letter[i])
    letter_Uper.append(letter[-i])

letter_Uper = ''.join(letter_Uper)
letter_Smol = ''.join(letter_Smol)





for i in range(10):
    lenName =random.randint(3, 10)
    temp_Name = []

    for s in range(lenName):
        key = random.randint(0, (len(letter_Uper) - 1))

        if lenName != len(temp_Name):
            if s == 0:
                temp_Name.append(letter_Uper[key])
            else:
                temp_Name.append(letter_Smol[key])

        if s == (lenName - 1):
            lst_Name.append(''.join(temp_Name))


print( lst_Name )