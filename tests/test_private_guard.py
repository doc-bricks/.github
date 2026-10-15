"""Check that a privacy failure does not echo the configured private name."""
import pytest

import test_profile_parity as profile


def test_private_name_is_absent_from_failure(monkeypatch):
    name = "synthetic-private-sentinel-62941"
    monkeypatch.setenv(profile.PRIVATE_REPOS_ENV, name)
    monkeypatch.setattr(profile, "get_file_content", lambda _path: name)
    with pytest.raises(AssertionError) as caught:
        profile.test_private_repo_leak_guard()
    assert name not in str(caught.value)
