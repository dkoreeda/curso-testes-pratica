# pytest tests/unit/examples/test_identifier_all_cases.py -vvv : mostra a descricao dos parametros
# pytest tests/unit/examples/test_identifier_activity3.py -k test_exception_raised --trace : debug
# pytest tests/unit/examples/test_identifier_activity3.py -k test_exception_raised --setupt-show : mostra setup dos tests
# pytest tests/unit/examples/test_identifier_activity3.py --cov=example.identifier --cov-report=html : mostra um relatório de coverage em html
# pytest tests/unit/examples/test_identifier_activity3.py --duration=10 : mostra quais são os 10 testes mais lentos

import pytest

from examples.identifier import Identifier


# scope='module' : reutiliza a fixture em todos os testes sem precisar fazer setup antes da execução de cada função.
# diferentemente do que acontece com scope 'function'
# @pytest.fixture(scope='function')
# def identifier():
#     return Identifier()

@pytest.fixture(scope='function', params=['abcd', 'ab'])
def identifier_tupla(request):
    # retornando uma tupla
    return (Identifier(), request.param)

def test_example_fixture_with_params(identifier_tupla):
    is_valid = identifier_tupla[0].validate_identifier(identifier_tupla[1])
    assert is_valid is True

@pytest.mark.parametrize(
    'param',
    [
        pytest.param('a', id='1 caracter válido'),
        pytest.param('ab', id='2 caracteres válidos'),
        pytest.param('abcde'),
        pytest.param('abcdef'),
        pytest.param('a1'),

    ]
)
def test_all_cases(param, identifier):
    is_valid = identifier.validate_identifier(param)
    assert is_valid is True

def test_exception_raised(identifier):
    with pytest.raises(ValueError) as e:
        identifier.validate_identifier('')

    # pytest.set_trace()
    assert str(e.value) == 'Identificador inválido'