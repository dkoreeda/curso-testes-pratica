import pytest

from base.utils.phone import format_phone_number

@pytest.mark.parametrize(
    'phone_number, expected_formatted_phone_number',
    [
        pytest.param('11979999999', '(11) 97999-9999', id='CT1 com DDD'),
        pytest.param('1179999999', '(11) 7999-9999', id='CT2 com DDD'),
        pytest.param('979999999', '97999-9999', id='CT3 sem DDD'),
        pytest.param('79999999', '7999-9999', id='CT3 sem DDD')
    ]
)
def test_case_0(phone_number, expected_formatted_phone_number):
    formatted_phone_number = format_phone_number(phone_number)
    assert formatted_phone_number == expected_formatted_phone_number