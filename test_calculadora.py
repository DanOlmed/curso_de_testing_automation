import pytest
from testclase3 import sumar, resta, multiplicar, dividir


#pytest -m smoke # solo tests “sumar”

#pytest -m exception # solo tests “dividir” con error
@pytest.mark.smoke
@pytest.mark.parametrize("a,b,resultado",[
    (10,4,14),
    (3,9,12),
    (14,2,16)
])
def test_sumar(a,b,resultado):
    assert sumar(a,b) == resultado


@pytest.mark.parametrize("a,b,resultado",[
    (3,4,-1),
    (50,20,30),
    (70,50,20)
])
def test_resta(a,b,resultado):
    assert resta(a,b) == resultado



def test_division_decimal():
    assert dividir(10,3)== pytest.approx(3.3333, rel=1e-3)


@pytest.mark.exception
def test_division_por_0():
    with pytest.raises(ZeroDivisionError):
        dividir(22,0)
    
@pytest.mark.parametrize("a,b,resultado",[
    (2,2,4),
    (22,3,66),
    (50,-2,-100)
])
def test_multiplicar(a,b,resultado):
    assert multiplicar(a,b)== resultado




