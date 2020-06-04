import colorama

streamstr = []
matrix = []
digraphs = []
spacemat = []
alphs = '0123456789abcdefghijklmnopqrstuvwxyz'



def find_space(t):

    global spacemat
    spacemat = []
    idx = 0
    for x in t:
        if x == ' ':
            spacemat.append(idx)
        else:
            idx += 1


def encode_space(t):
    textt = ''
    if not spacemat:
        return t.rstrip('X')
    for x in spacemat:
        textt = t[0:x] + ' ' + t[x:]
    return textt.rstrip('X')


def create_stream(ky):
    global alphs
    alphs = alphs.upper()
    global streamstr
    streamstr = []
    lngstr = ky + alphs
    for x in lngstr:
        if len(streamstr) < 37 and x not in streamstr:
            streamstr.append(x)


def construct_matrix():
    global streamstr, matrix
    matrix = []
    a = []
    for x in streamstr:
        if len(a) == 6:
            matrix.append(a)
            a = [x]
        else:
            a.append(x)
    if len(matrix) != 6:
        matrix.append(a)


def display_matrix():
    print(colorama.Fore.LIGHTGREEN_EX + '    CIPHER MATRIX\n______________________', end='')
    print(colorama.Style.RESET_ALL, end='')

    global streamstr
    i = 0
    if not streamstr:
        streamstr = alphs

    for i in range(36):
        if i % 6 == 0:
            print('\n', end='')
        print(streamstr[i], end='   ')
    print(colorama.Fore.GREEN + '\n______________________')
    print(colorama.Style.RESET_ALL, end='')


def find_char(char):
    r = c = 0
    global matrix
    for sbl in matrix:
        if char in sbl:
            c = sbl.index(char.upper())
            # print(f'found at row:{r+1} col:{c+1}')
            break
        else:
            r += 1
            # print('skipped row')
    return r, c


def make_digraphs(txt):
    global digraphs
    digraphs = []
    di = []
    for x in txt:
        if len(di) == 2:
            digraphs.append(di)
            di = [x]
        else:
            di.append(x)
    if len(di) > 0:
        if len(di) < 2:
            di.append('X')
        digraphs.append(di)
    clean_digraphs()
    print(colorama.Fore.GREEN + 'Digraphs-->', digraphs)
    print(colorama.Style.RESET_ALL, end='')


def clean_digraphs():
    global digraphs
    for x in digraphs:
        if x[0] == x[1]:
            x[1] = 'X'


def encrypt(txt):
    ciphertext = ''
    global digraphs
    for x in digraphs:
        f1 = find_char(x[0])
        f2 = find_char(x[1])

        if f1[0] == f2[0]:
            print(f'{x[0]} {x[1]} same row')
            row = matrix[f1[0]]
            # print(row)

            if f1[1] == 5:
                n1 = row[0]
            else:
                n1 = row[f1[1] + 1]
            if f2[1] == 5:
                n2 = row[0]
            else:
                n2 = row[f2[1] + 1]

            ciphertext += n1 + n2

        elif f1[1] == f2[1]:
            print(f'{x[0]} {x[1]} same column')

            if f1[0] == 5:
                n1 = matrix[0][f1[1]]
            else:
                n1 = matrix[f1[0] + 1][f1[1]]
            if f2[0] == 5:
                n2 = matrix[0][f2[1]]
            else:
                n2 = matrix[f2[0] + 1][f2[1]]

            ciphertext += n1 + n2
        else:
            print(f'{x[0]} {x[1]} Rectangle')
            r1, c1 = f1
            r2, c2 = f2
            n1 = matrix[r1][c2]
            n2 = matrix[r2][c1]

            ciphertext += n1 + n2

    print('\nPlain Text-->' + txt)
    print(colorama.Fore.GREEN + ciphertext)
    print(colorama.Fore.GREEN + 'Cipher Text--> ' + encode_space(ciphertext))
    print(colorama.Style.RESET_ALL, end='')


def decrypt(txt):
    plaintext = ''
    global digraphs
    for x in digraphs:
        f1 = find_char(x[0])
        f2 = find_char(x[1])

        if f1[0] == f2[0]:
            print(f'{x[0]} {x[1]} same row')
            row = matrix[f1[0]]
            # print(row)

            if f1[1] == 0:
                n1 = row[5]
            else:
                n1 = row[f1[1] - 1]
            if f2[1] == 0:
                n2 = row[5]
            else:
                n2 = row[f2[1] - 1]

            plaintext += n1 + n2

        elif f1[1] == f2[1]:
            print(f'{x[0]} {x[1]} same column')

            if f1[0] == 0:
                n1 = matrix[5][f1[1]]
            else:
                n1 = matrix[f1[0] - 1][f1[1]]
            if f2[0] == 0:
                n2 = matrix[5][f2[1]]
            else:
                n2 = matrix[f2[0] - 1][f2[1]]

            plaintext += n1 + n2
        else:
            print(f'{x[0]} {x[1]} Rectangle')
            r1, c1 = f1
            r2, c2 = f2
            n1 = matrix[r1][c2]
            n2 = matrix[r2][c1]

            plaintext += n1 + n2

    print('\nCipher Text-->' + txt)
    print(colorama.Fore.GREEN +plaintext)
    print(colorama.Fore.GREEN + 'Decoded Text-->' + encode_space(plaintext))
    print(colorama.Style.RESET_ALL, end='')


while True:
    print('\n-----------------------------------------------')
    print(colorama.Fore.GREEN + '\tEnter Choice\n\tE==> ENCRYPT\t      D==> DECRYPT\n\tS==> Show Matrix      Q-->Quit')
    print(colorama.Style.RESET_ALL, end='')
    print('-----------------------------------------------')
    choice = input('-> ')
    choice = choice.upper()
    print('\n')

    if choice == 'E':

        print(colorama.Fore.LIGHTGREEN_EX + '-----ENCRYPTION-----')
        print(colorama.Style.RESET_ALL, end='')
        keywerd = input('Enter Keyword-> ')
        print('')
        create_stream(keywerd.upper())
        display_matrix()
        print('\n')
        construct_matrix()
        ptxt = input('Enter Plain Text-> ')
        pl = ptxt
        find_space(ptxt)
        ptxt = ptxt.replace(' ', '')
        make_digraphs(ptxt.upper())
        encrypt(ptxt)

    elif choice == 'S':
        display_matrix()
        print('')

    elif choice == 'D':
        print(colorama.Fore.LIGHTGREEN_EX + '-----DECRYPTION-----')
        print(colorama.Style.RESET_ALL, end='')
        keywerd = input('Enter Keyword for decryption-> ')
        print('')
        create_stream(keywerd.upper())
        display_matrix()
        print('')
        construct_matrix()
        ctxt = input('Enter Cipher Text-> ')
        find_space(ctxt)
        ctxt = ctxt.replace(' ', '')

        make_digraphs(ctxt.upper())
        decrypt(ctxt)

    elif choice == 'Q':
        print('-----Exiting-----')
        exit(900)
        print('\n')

    else:
        print(colorama.Fore.RED + 'Invalid Choice. Try Again\n')
        print(colorama.Style.RESET_ALL, end='')
