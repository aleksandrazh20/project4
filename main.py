s = input('Введите строку: ').lower()
print('1 - шифр Цезаря, 2 - транспозиция, 3 - азбука морзе')
kode_type = int(input('Выберите шифр: '))
if kode_type == 1:
    for i in range(len(s)):
        a = ord(s[i]) + 3
        ss = chr(a)
        print(ss, end='')
if kode_type == 2:
    for i in range(0,len(s)-1,2):
        s1 = s[i+1]
        s2 = s[i]
        print(s1 + s2, end='')
if kode_type == 3:
    for i in range(len(s)):
        if s[i] == 'a':
            s1 = '.-'
        elif s[i] == 'b':
            s1 = '-...'
        elif s[i] == 'c':
            s1 = '-.-.'
        elif s[i] == 'd':
            s1 = '-..'
        elif s[i] == 'e':
            s1 = '.'
        elif s[i] == 'f':
            s1 = '..-.'
        elif s[i] == 'g':
            s1 = '--.'
        elif s[i] == 'h':
            s1 = '....'
        elif s[i] == 'i':
            s1 = '..'
        elif s[i] == 'j':
            s1 = '.---'
        elif s[i] == 'k':
            s1 = '-.-'
        elif s[i] == 'l':
            s1 = '.-..'
        elif s[i] == 'm':
            s1 = '--'
        elif s[i] == 'n':
            s1 = '-.'
        elif s[i] == 'o':
            s1 = '---'
        elif s[i] == 'p':
            s1 = '.--.'
        elif s[i] == 'q':
            s1 = '--.-'
        elif s[i] == 'r':
            s1 = '.-.'
        elif s[i] == 's':
            s1 = '...'
        elif s[i] == 't':
            s1 = '-'
        elif s[i] == 'u':
            s1 = '..-'
        elif s[i] == 'w':
            s1 = '.--'
        elif s[i] == 'x':
            s1 = '-..-'
        elif s[i] == 'y':
            s1 = '-.--'
        elif s[i] == 'z':
            s1 = '--..'
        else:
            s1 = s[i]
        print(s1, end='')