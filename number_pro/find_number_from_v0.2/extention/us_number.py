import main as m


def us_number(pera):
    new = ""
    new2 = ""

    for x in range(1, 12):
        new = new + pera[x]
    for y in range(13, len(pera)):
        new2 = new2 + pera[y]
    if new.isdigit():
        print(f"USA Number\t: {new[0:]}")
        m.get_p(new2)
    else:
        m.get_p(new2)
