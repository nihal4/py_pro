import main as m


def bd_number(pera):
    new = ""
    new2 = ""

    for x in range(1, 14):
        new = new + pera[x]
    for y in range(15, len(pera)):
        new2 = new2 + pera[y]
    if new.isdigit():
        print(f"BD Number\t: {new[2:]}")
        m.get_p(new2)
    else:
        m.get_p(new2)
