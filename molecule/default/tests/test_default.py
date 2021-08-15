"""Role testing files using testinfra."""

import pytest


@pytest.mark.parametrize("group", ["ansible", "department99"])
def test_pkg_installed(host, group):
    """Test if package installed."""
    assert host.group(group).exists
