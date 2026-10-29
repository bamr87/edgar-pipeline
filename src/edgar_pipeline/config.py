"""SEC fair-access configuration: every request carries a descriptive User-Agent and stays under 10 req/s."""
import os

MAX_REQUESTS_PER_SECOND = 10
SUBMISSIONS_URL = "https://data.sec.gov/submissions/CIK{cik:010d}.json"


def user_agent() -> str:
    return os.environ.get("EDGAR_USER_AGENT", "edgar-pipeline/0.1 (contact: set EDGAR_USER_AGENT)")


def submissions_url(cik: int) -> str:
    return SUBMISSIONS_URL.format(cik=cik)
