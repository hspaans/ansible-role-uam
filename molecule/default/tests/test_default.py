"""Role testing files using testinfra."""

import pytest


@pytest.mark.parametrize("group", ["ansible"])
def test_group_installed(host, group):
    """Test if package installed."""
    item = host.group(group)

    assert item.exists


@pytest.mark.parametrize("group", ["department99"])
def test_group_not_installed(host, group):
    """Test if package installed."""
    item = host.group(group)

    assert not item.exists


@pytest.mark.parametrize("user", ["ansible"])
def test_user_installed(host, user):
    """Test if package installed."""
    item = host.user(user)

    assert item.exists
