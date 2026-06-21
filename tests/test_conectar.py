# testes da criacao do cliente da api do github
from github import Github

from saiku import coleta


def test_conectar_sem_token():
    assert isinstance(coleta.conectar(), Github)


def test_conectar_com_token():
    assert isinstance(coleta.conectar("token-falso"), Github)
