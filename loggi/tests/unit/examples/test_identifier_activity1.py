import pytest

from examples.identifier import Identifier

@pytest.fixture
def identifier():
    return Identifier()

def test_case_01(identifier):
    is_valid = identifier.validate_identifier('ab')
    assert is_valid is True

def test_case_02(identifier):
    is_valid = identifier.validate_identifier('1a')
    assert is_valid is False

def test_case_03(identifier):
    is_valid = identifier.validate_identifier('abcdef')
    assert is_valid is True

def test_case_04(identifier):
    is_valid = identifier.validate_identifier('abcdefg')
    assert is_valid is False

def test_case_05(identifier):
    is_valid = identifier.validate_identifier('a*bcde')
    assert is_valid is False

def test_case_06(identifier):
    is_valid = identifier.validate_identifier('a12345')
    assert is_valid is True