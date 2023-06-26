from extention import get_file as gf
import verify_reagion as vr


def get_p(texts):
    while texts is not None:
        index = texts.find('+')
        if index == -1:
            break
        texts = vr.calcu(texts[index:])


if __name__ == "__main__":
    path = gf.file_select()
    with open(f"{path}", 'r+') as file_pera:
        file_pera = file_pera.read()
        get_p(file_pera)
