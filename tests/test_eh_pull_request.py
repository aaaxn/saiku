# teste da deteccao de pr pelo payload da listagem de issues
from saiku import coleta


class _FakeIssue:
    def __init__(self, rawdata):
        self._rawData = rawdata


def test_issue_com_pull_request():
    assert coleta._eh_pull_request(_FakeIssue({"pull_request": {"url": "x"}})) is True


def test_issue_comum_nao_eh_pr():
    assert coleta._eh_pull_request(_FakeIssue({"title": "x"})) is False
