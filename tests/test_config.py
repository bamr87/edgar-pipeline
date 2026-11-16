import pytest

from edgar_pipeline.config import MAX_REQUESTS_PER_SECOND, ConfigError, submissions_url, user_agent


def test_cik_padding():
    assert submissions_url(320193).endswith("CIK0000320193.json")


def test_rate_cap():
    assert MAX_REQUESTS_PER_SECOND <= 10


def test_config_error_is_a_value_error():
    assert issubclass(ConfigError, ValueError)


def _assert_user_agent_rejected():
    with pytest.raises(ConfigError) as excinfo:
        user_agent()
    message = str(excinfo.value)
    assert "EDGAR_USER_AGENT" in message
    assert "Acme Research jane@example.com" in message  # the example a user can copy


def test_user_agent_unset_fails_fast(monkeypatch):
    monkeypatch.delenv("EDGAR_USER_AGENT", raising=False)
    _assert_user_agent_rejected()


@pytest.mark.parametrize("value", ["", "   ", "Acme Research"], ids=["empty", "whitespace", "no-contact"])
def test_user_agent_blank_or_without_contact_fails_fast(monkeypatch, value):
    monkeypatch.setenv("EDGAR_USER_AGENT", value)
    _assert_user_agent_rejected()


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("  Acme jane@example.com  ", "Acme jane@example.com"),
        ("Acme https://acme.example", "Acme https://acme.example"),
    ],
    ids=["email-stripped", "url"],
)
def test_user_agent_with_contact_is_returned_stripped(monkeypatch, value, expected):
    monkeypatch.setenv("EDGAR_USER_AGENT", value)
    assert user_agent() == expected
