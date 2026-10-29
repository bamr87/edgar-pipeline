from edgar_pipeline.config import MAX_REQUESTS_PER_SECOND, submissions_url


def test_cik_padding():
    assert submissions_url(320193).endswith("CIK0000320193.json")


def test_rate_cap():
    assert MAX_REQUESTS_PER_SECOND <= 10
