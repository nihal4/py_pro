def bd_number(pera):
    new = ""
    new2 = ""

    for x in range(1, 14):
        new = new + pera[x]
    for y in range(15, len(pera)):
        new2 = new2 + pera[y]
    if new.isdigit():
        print(new)
        get_p(new2)
    else:
        get_p(new2)


def us_number(pera):
    new = ""
    new2 = ""

    for x in range(1, 12):
        new = new + pera[x]
    for y in range(13, len(pera)):
        new2 = new2 + pera[y]
    if new.isdigit():
        print(new)
        get_p(new2)
    else:
        get_p(new2)


def calcu(pera1):
    while True:
        if pera1[0:3] == "+88" and pera1[1:14].isdigit() == True:
            bd_number(pera1)
            break
        elif pera1[0:2] == "+1" and pera1[1:11].isdigit() == True:
            us_number(pera1)
            break
        else:
            return pera1[1:]


def get_p(texts):
    while texts is not None:
        index = texts.find('+')
        if index == -1:
            break
        texts = calcu(texts[index:])


if __name__ == "__main__":
    get_p(input("=>"))
