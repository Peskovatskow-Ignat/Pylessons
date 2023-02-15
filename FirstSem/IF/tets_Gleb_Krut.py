# -*- coding: utf-8 -*
from requests import Session
import pytest

@pytest.mark.parametrize('title', ["12345678998765432", "qty123321", "23456789098765345678", "sdfghjk;'lkljgyhftgdxd", "12567890", "AA_@", "ABA", "VItalik_neut", "12345678998765432", "qty123321", "23456789098765345678", "sdfghjk;'lkljgyhftgdxd", "12567890", "AA_@", "ABA", "VItalik_neut", "123456789098765432", "qwerty123321", "234567890987654312345678", "sdfghjklk;'lkljkhujgyhftgdxd", "1234567890", "ABOBA_@", "ABOBA", "VItalik_ne_krut" "12345678998765432", "qty123321", "23456789098765345678", "sdfghjk;'lkljgyhftgdxd", "12567890", "AA_@", "ABA", "VItalik_neut", "12345678998765432", "qty123321", "23456789098765345678", "sdfghjk;'lkljgyhftgdxd", "12567890", "AA_@", "ABA", "VItalik_neut", "123456789098765432", "qwerty123321", "234567890987654312345678", "sdfghjklk;'lkljkhujgyhftgdxd", "1234567890", "ABOBA_@", "ABOBA", "VItalik_ne_krut", "12345678998765432", "qty123321", "23456789098765345678", "sdfghjk;'lkljgyhftgdxd", "12567890", "AA_@", "ABA", "VItalik_neut", "12345678998765432", "qty123321", "23456789098765345678", "sdfghjk;'lkljgyhftgdxd", "12567890", "AA_@", "ABA", "VItalik_neut", "123456789098765432", "qwerty123321", "234567890987654312345678", "sdfghjklk;'lkljkhujgyhftgdxd", "1234567890", "ABOBA_@", "ABOBA", "VItalik_ne_krut", "12345678998765432", "qty123321", "23456789098765345678", "sdfghjk;'lkljgyhftgdxd", "12567890", "AA_@", "ABA", "VItalik_neut", "12345678998765432", "qty123321", "23456789098765345678", "sdfghjk;'lkljgyhftgdxd", "12567890", "AA_@", "ABA", "VItalik_neut", "123456789098765432", "qwerty123321", "234567890987654312345678", "sdfghjklk;'lkljkhujgyhftgdxd", "1234567890", "ABOBA_@", "ABOBA", "VItalik_ne_krut", "12345678998765432", "qty123321", "23456789098765345678", "sdfghjk;'lkljgyhftgdxd", "12567890", "AA_@", "ABA", "VItalik_neut", "12345678998765432", "qty123321", "23456789098765345678", "sdfghjk;'lkljgyhftgdxd", "12567890", "AA_@", "ABA", "VItalik_neut", "123456789098765432", "qwerty123321", "234567890987654312345678", "sdfghjklk;'lkljkhujgyhftgdxd", "1234567890", "ABOBA_@", "ABOBA", "VItalik_ne_krut"])
@pytest.mark.parametrize('language', ["abap", "abnf", "ada", "antlr-python", "antlr-ruby", "apacheconf", "java", "javascript"])
@pytest.mark.parametrize('style', ["abap", "autumn", "arduino", "dracula", "igor", "one-dark"])
@pytest.mark.parametrize('lineos', [True, False])
def test_with_papam(language, style, lineos, title):

    login = 'suranov_ignat'
    password = '123321'

    my_session = Session()
    my_session.auth = (login, password)

    resp = my_session.post(url='http://185.182.111.235/snippets/',
                           json={'title': title,
                                 'code': 'print(vso good)',
                                 "linenos": lineos,
                                 "language": language,
                                 "style": style})

    assert resp.status_code == 201


# def test_current_user_auth_pass():
#     """
#         Тест на прохождение авторизации
#     """
#
#     # Параметры теста
#     login = 'peskovatskov_vitalik'
#     password = 'qwerty123'
#
#
#     # http сессия
#     my_session = Session()
#     my_session.auth = (login, password)
#
#     # Тестовый сценарий
#     resp = my_session.get(url='http://185.182.111.235/current_user/')
#     json_ans = resp.json()
#
#     # Проверки
#     assert resp.status_code == 200, "Статус код не 200"
#     assert login in resp.text, "Логин не совпадает"
#     assert '54' in resp.text, "id пользователя не равен 21"