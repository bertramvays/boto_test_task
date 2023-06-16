import re

non_typical_pattern = re.compile(
    r'[a-z]|[a-z][абвгдеёжзийклмнопрстуфхцчшщъыьэюя]|ёё|ёщ|ыё|ёу|йэ|гъ|кщ|'
    r'щф|щз|эщ|щк|гщ|щп|щт|щш|щг|щм|фщ|щл|щд|дщ|ьэ|чц|вй|ёц|ёэ|ёа|йа|шя|шы|'
    r'ёе|йё|гю|хя|йы|ця|гь|сй|хю|хё|ёи|ёо|яё|ёя|ёь|ёэ|ъж|эё|ъд|цё|уь|щч|чй|'
    r'шй|шз|ыф|жщ|жш|жц|ыъ|ыэ|ыю|ыь|жй|ыы|жъ|жы|ъш|пй|ъщ|зщ|ъч|ъц|ъу|ъф|ъх|'
    r'ъъ|ъы|ыо|жя|зй|ъь|ъэ|ыа|нй|еь|цй|ьй|ьл|ьр|пъ|еы|еъ|ьа|шъ|ёы|ёъ|ът|щс|оь|'
    r'къ|оы|щх|щщ|щъ|щц|кй|оъ|цщ|лъ|мй|шщ|ць|цъ|щй|йь|ъг|иъ|ъб|ъв|ъи|ъй|ъп|ър|'
    r'ъс|ъо|ън|ък|ъл|ъм|иы|иь|йу|щэ|йы|йъ|щы|щю|щя|ъа|мъ|йй|йж|ьу|гй|эъ|уъ|аь|'
    r'чъ|хй|тй|чщ|ръ|юъ|фъ|уы|аъ|юь|аы|юы|эь|эы|бй|яь|ьы|ьь|ьъ|яъ|яы|хщ|дй|фй')
non_useful = re.compile(r'[0-9]|\W')
file = './unigrams'


def isBeliberda(s):
    if len(s) <= 1:
        return False
    counter = 0
    str = re.sub(non_useful, ' ', s).lower()
    non_typical_amount = non_typical_pattern.findall(str)
    if len(non_typical_amount) > 0:
        counter -= 1
    string_words = str.split()
    for word in string_words:
        if len(word) < 3:
            continue
        elif str.count(word) > 2:
            counter -= 1
        else:
            with open(file, 'r') as f:
                for line in f.readlines():
                    if line.split()[0] == word:
                        counter += 1
    if counter > 0:
        return True
    else:
        return False
