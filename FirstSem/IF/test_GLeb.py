from requests import session
from pprint import pprint


def test_current_user_auth_pass():
    # Тест на Изменения с помощью PATCH

    # Логи и пароль пользователя
    login = 'peskovatskov_vitalik'
    password = 'qwerty123'

    # http сессия
    my_session = session()
    my_session.auth = (login, password)

    # Тестовый сценарий

    # создание пользователся с помощь POST
    resp = my_session.post(url='http://185.182.111.235/snippets/',
                           json={'title': 'Gleb krut',
                                 'code': 'print(vso good)',
                                 "linenos": 'true',
                                 "language": "python",
                                 "style": "dracula"})
    pprint(resp.json())

    resp_1 = my_session.get(url='http://185.182.111.235/current_user/')

    my_resp_dict = resp.json()
    id = my_resp_dict['id']
    titl = my_resp_dict['title']
    code = my_resp_dict['code']
    print(titl, code)


    # Отправка запроса PATCH
    resp = my_session.patch(url=f'http://185.182.111.235/snippets/{id}/',
                            json={'title': 'Gleb krut123321',
                                  'code': 'print(tebya vzlomali)'})

    my_resp_dict = resp.json()
    titl1 = my_resp_dict['title']
    code1 = my_resp_dict['code']
    print(titl1)
    print(code1)


    assert titl1 != 'Gleb krut', 'Остался прежним'
    assert titl1 == 'Gleb krut123321',  'Реально любит анегдоты'
    assert code1 != 'print(vso good)', 'Остался прежним'
    assert code1 == 'print(tebya vzlomali)', 'Поменялся и тебя реально взломани'
    assert '54' in resp_1.text, "id пользователя не равен 54"
    # Удали_ПЖ
    # resp = my_session.delete(url=f'http://185.182.111.235/snippets/{id}/')