"""Test parsing from file."""

import pytest

from livingdocs.userneeds import load_userneeds_from_file


@pytest.mark.integtest
def test_userneeds_from_file() -> None:
    userneeds = load_userneeds_from_file("testfiles/userneeds.csv")
    assert len(userneeds) == 6
