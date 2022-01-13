import pytest

from gorgona.stages.cleaners import EmojiCleaner


@pytest.fixture()
def setup_emoji_cleaner():
    ec = EmojiCleaner(
        '',
        '',
    )

    return ec


def test_no_emoji(setup_emoji_cleaner):
    assert setup_emoji_cleaner('hello, world') == 'hello, world'


def test_only_emoji(setup_emoji_cleaner):
    assert setup_emoji_cleaner('😀🥺😡') == ''


def test_mixed(setup_emoji_cleaner):
    assert setup_emoji_cleaner('hello 🤡, world 😳') == 'hello , world '
