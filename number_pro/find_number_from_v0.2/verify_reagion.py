from extention import bd_number as bd
from extention import us_number as us


def calcu(pera1):
    while True:
        if pera1[0:3] == "+88" and pera1[1:14].isdigit() is True:
            bd.bd_number(pera1)
            break
        elif pera1[0:2] == "+1" and pera1[1:11].isdigit() is True:
            us.us_number(pera1)
            break
        else:
            return pera1[1:]
