import opencc


def convert():
    converter = opencc.OpenCC('s2twp.json')

    with open('zhcn_only.dict', 'r', encoding='utf-8') as rr, open('zhtw_only.dict', 'w', encoding='utf-8') as ww:
        line = rr.readline()
        while line:
            ww.writelines(converter.convert(line))
            line = rr.readline()


convert()
