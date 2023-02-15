# -*- coding: utf-8 -*
from requests import Session
import requests
from pprint import pprint
# resp = requests.post(url='http://185.182.111.235/snippets/',
#                     auth=('peskovatskov_vitalik', 'qwerty123'),
#                     json={
#                             "title": "Gleb_molodeц 2.0",
#                             "code": "print('Я люблю тестики')",
#                             "linenos": True,
#                             "language": "python",
#                             "style": "dracula"
#                             })
#
# print('Тип -', type(resp))
# print(resp.status_code)
# print('Тип -', type(resp.status_code))
#
# print(resp.text)
# print('Тип -', type(resp.text))
#
# my_response_dict = resp.json()
#
# print(my_response_dict)
# print('Тип -', type(my_response_dict))
my_sessio = Session()

my_sessio.auth = ('peskovatskov_vitalik', 'qwerty123')

resp_1 = my_sessio.post(url='http://185.182.111.235/snippets/',
                        json={
                            "title": "Gleb_molodeц 3.0",
                            "code": "print('Я люблю тестики')",
                            "linenos": True,
                            "language": "python",
                            "style": "dracula"
                            })
print(resp_1)
my_resp_dict = resp_1.json()
print(my_resp_dict)
id_1 = my_resp_dict['id']
print(id_1)

resp_2 = my_sessio.get(url='http://185.182.111.235/snippets/' + str(id_1) + '/')
pprint(resp_2.json())

resp_3 = my_sessio.delete(url='http://185.182.111.235/snippets/' + str(id_1) + '/')
print(resp_3)

resp_4 = my_sessio.get(url='http://185.182.111.235/snippets/' + str(id_1) + '/')
print(resp_4)