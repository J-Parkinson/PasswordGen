symbols = '!"£^&*()_+:@<>?,./;#-='

from random import randint

with open("pw.txt", "r") as words:
    words = words.read().split("\n")

with open("newpasswords.txt", "a+") as newpasswords:
    for word in words:
        new = ""
        for char in word:
            if char.isalpha():
                if randint(0, 13) == 13:
                    new += symbols[randint(0, len(symbols) - 1)]
                elif randint(0, 12) == 12:
                    new += str(randint(0, 9))
                if randint(0, 1) == 0:
                    new += char.upper()
                else:
                    new += char.lower()

        if len(new) < 10:
            for x in range(2):
                if randint(1, 3) == 3:
                    new += str(randint(0, 9))
                else:
                    new += symbols[randint(0, len(symbols) - 1)]

        newpasswords.write(new + "\n")