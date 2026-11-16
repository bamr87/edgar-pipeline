"""SEC fair-access configuration: every request carries a descriptive User-Agent and stays under 10 req/s."""
import os
import re

MAX_REQUESTS_PER_SECOND = 10
SUBMISSIONS_URL = "https://data.sec.gov/submissions/CIK{cik:010d}.json"

USER_AGENT_ENV = "EDGAR_USER_AGENT"
# The contact SEC fair access asks for: an email-like token or an http(s) URL.
_CONTACT = re.compile(r"\S+@\S+|https?://\S+")
_USER_AGENT_HELP = (
    "SEC fair access requires a descriptive User-Agent with a contact (an email address or an http(s) URL), "
    f"e.g. {USER_AGENT_ENV}='Acme Research jane@example.com'"
)


class ConfigError(ValueError):
    """A required setting is missing or invalid."""


def user_agent() -> str:
    """Return the User-Agent for SEC requests: the stripped value of EDGAR_USER_AGENT.

    Raises ConfigError when the variable is unset, blank or names no contact, instead of
    sending a placeholder without a real contact.
    """
    value = os.environ.get(USER_AGENT_ENV, "").strip()
    if not value:
        raise ConfigError(f"{USER_AGENT_ENV} is not set. {_USER_AGENT_HELP}")
    if not _CONTACT.search(value):
        raise ConfigError(f"{USER_AGENT_ENV} has no contact: {value!r}. {_USER_AGENT_HELP}")
    return value


def submissions_url(cik: int) -> str:
    return SUBMISSIONS_URL.format(cik=cik)
