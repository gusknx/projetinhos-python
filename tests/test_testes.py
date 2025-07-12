"""ta faltando uma doc aqui tbm"""
from app.teste import testando_coisas

def test_testando_coisas_saida(capfd):
    """faltando docstring aqui"""
    testando_coisas()
    out = capfd.readouterr()
    assert 'teste, encerrado.' in out
    assert 'vez errada' in out
