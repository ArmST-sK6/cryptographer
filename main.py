def encryption(a, b, c):
    result = []
    for j in range(len(a)):
        result.append(b[c.index(a[j])])
    return result


def decryption(a, b, c):
    result = []
    for j in range(len(a)):
        result.append(b[c.index(a[j])])
    return result


def main(sel):
    stock = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '.', ',', ':', '?', '-', 'A', 'a', 'B', 'b', 'C',
             'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K',
             'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u',
             'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']
    cypher = []
    sentence = str(input("Sentence - "))
    wd_code = list(input("Cypher - "))
    code = []
    for i in wd_code:
        if i not in code:
            code.append(i)

    for i in range(len(code)):
        cypher.append(code[i])

    for i in range(len(stock)):
        if stock[i] not in cypher:
            cypher.append(stock[i])
    if sel == 1:
        result = encryption(sentence, stock, cypher)
        print("Result -", end=' \"')
        for i in range(len(result)):
            print(result[i], end='')
        print('\"\n\n\n\n')

    else:
        result = decryption(sentence, cypher, stock)
        print("Result -", end=' \"')
        for i in range(len(result)):
            print(result[i], end='')
        print('\"\n\n\n\n')


while True:
    print("\t1 - Encrypt\n\t2 - Decrypt")
    sel = input("\tSelect option - ")
    if sel in "0123456789":
        sel = int(sel)
    while sel == 1 or sel == 2:
        main(sel)
        break
