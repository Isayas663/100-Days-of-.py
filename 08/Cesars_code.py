from Art_Cesars import cesarsa
from Cesars_list import *
def cesars(text,shift,direction):
    end_word = ''
    for n in range(0,len(text)):
            if not text[n] in alphabet:
                end_word += text[n]
                continue
            indexx = alphabet.index(text[n])
            if direction == 'encode':
                indexx += shift%25
                if indexx > 25:
                    indexx -=26
            elif direction == 'decode':
                indexx -= shift%25
                if indexx < 0:
                    indexx +=26
            end_word += alphabet[indexx]
    print(f"here is your {direction}d text bro")
    print(end_word)


print(cesarsa)
end = False
while not end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    cesars (text,shift,direction)

    finish = input("Would you like to try again??? yes or no -> ")
    if finish in ['no','n']:
        end = True
        print("See you bro")

    #decrypt(text,shift)


