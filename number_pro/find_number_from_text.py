def calcu(pera):
    new = ""
    new2 = ""
    for x in range(1, 14):
        new = new + pera[x]
    for y in range(15, len(pera)):
        new2 = new2 + pera[y]
    if new.isdigit():
        print(new)
        return new2


def get_p(texts):
    while True:
        index = texts.find('+')
        if index == -1:
            break
        texts = calcu(texts[index:])
        if texts is None:
            break


if __name__ == "__main__":
    get_p(input("=>"))
