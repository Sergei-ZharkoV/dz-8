# 1. Написать функцию email_parse(<email_address>),
# которая при помощи регулярного выражения извлекает имя пользователя и почтовый домен из email адреса
# и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError.
# Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
# имеет ли смысл в данном случае использовать функцию re.compile()?

import re

RE_EMAIL = re.compile(r'([a-z0-9.\.]+)@([a-z0-9]+\.[a-z]+)')

def email_parse(email):
    info_email = RE_EMAIL.findall(email)
    if info_email:
        name, addr = info_email[0]
    else:
        raise ValueError(f'wrang email: {email}')
    print(name, addr)

email_parse('reds09@mail.ru')




