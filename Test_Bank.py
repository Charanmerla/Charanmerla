import pytest

from Bank_Management import BankAccount

cust1 = BankAccount(name="Ishan", mobile_no=9898989898, initial_deposit=1000, pin=1234)
cust2 = BankAccount(name="gill", mobile_no=9695969596, initial_deposit=1500, pin=5231)


# @pytest.fixture
def test_method1():
    assert cust1.name == "Ishan"


def test_method2():
    assert cust1.acc_balance == 1000


@pytest.mark.xfail
def test_method3():
    assert cust2.account_num == 42012


def test_method4():
    assert cust2.mobile_no == 9695969596


@pytest.mark.skip
def test_method5():
    assert cust1.account_num == 42011
