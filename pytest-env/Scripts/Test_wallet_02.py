import pytest
from wallet import Wallet,InsufficientAmount

"""
@pytest.fixture
def empty_wallet():
    return Wallet()
@pytest.fixture
def wallet():
    return Wallet(100)

def test_default_initial_amount(empty_wallet):
    #wallet = Wallet()
    assert empty_wallet.balance == 0

def test_setting_initial_amount(wallet):
    #wallet = Wallet(100)
    assert wallet.balance == 100

def test_wallet_add_cash(wallet):
    #wallet = Wallet(100)
    wallet.add_cash(10)
    assert wallet.balance == 110

def test_wallet_spend_cash(wallet):
    #wallet = Wallet(100)
    wallet.spend_cash(10)
    assert wallet.balance == 90

def test_wallet_spend_cash_raises_exception_on_insufficient_amount(empty_wallet):
    #wallet = Wallet()
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(100)

@pytest.mark.parametrize("earned,spent,expected",[(30,20,10),(20,2,18)])
def test_transaction(empty_wallet,earned,spent,expected):
    empty_wallet.add_cash(earned)
    empty_wallet.spend_cash(spent)
    assert empty_wallet.balance == expected
"""


def demo(a):
    return a

def test_demo():
    assert demo("abcd") == "abcd"














