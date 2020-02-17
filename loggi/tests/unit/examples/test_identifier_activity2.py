import pytest

from examples.identifier import Identifier

@pytest.fixture
def identifier():
    return Identifier()


def test_case_0(identifier):
    is_valid = identifier.validate_identifier('')
    assert is_valid is False

def test_case_1(identifier):
    is_valid = identifier.validate_identifier('a')
    assert is_valid is True

def test_case_3(identifier):
    is_valid = identifier.validate_identifier('ab')
    assert is_valid is True

def test_case_4(identifier):
    is_valid = identifier.validate_identifier('abcde')
    assert is_valid is True

def test_case_5(identifier):
    is_valid = identifier.validate_identifier('abcdef')
    assert is_valid is True

def test_case_6(identifier):
    is_valid = identifier.validate_identifier('abcdefg')
    assert is_valid is False

def test_case_7(identifier):
    is_valid = identifier.validate_identifier('1a')
    assert is_valid is False

def test_case_8(identifier):
    is_valid = identifier.validate_identifier('a12345')
    assert is_valid is True

def test_case_9(identifier):
    is_valid = identifier.validate_identifier('a1')
    assert is_valid is True