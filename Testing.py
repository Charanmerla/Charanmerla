import pytest
import requests
import json


# @pytest.mark.one
# def test_method1():
#     x = 5
#     y = 10
#     assert x == y
#
#
# @pytest.mark.two
# def test_method2():
#     a = 15
#     b = 20
#     assert a + 5 == b
# ----------------------------------
# class TestClass:
#     def test_one(self):
#         x = "charan"
#         assert "r" in x
#
#     def test_two(self):
#         x = "hello"
#         assert hasattr(x,"check")
# ----------------------------------
# @pytest.fixture
# def numbers():
#     a = 10
#     b = 20
#     c = 25
#     return [a, b, c]
#
#
# @pytest.mark.xfail
# def test_method1(numbers):
#     x = 15
#     assert numbers[0] == x
#
#
# @pytest.mark.skip
# def test_method2(numbers):
#     y = 20
#     assert numbers[1] == y
#
#
# def test_method3(numbers):
#     z = 25
#     assert numbers[2] == z
# ----------------------------------

# @pytest.mark.parametrize("x,y,z",[(10,20,200),(20,40,400)])
# def test_method(x,y,z):
#     assert x*y == z
# ----------------------------------


def test_valid_login():
    url = 'https://reqres.in/api/login/'
    data = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response = requests.post(url, data=data)
    token = json.loads(response.text)
    assert response.status_code == 200
    assert token['token'] == "QpwL5tke4Pnpja7X4"
