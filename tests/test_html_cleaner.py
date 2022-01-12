import pytest

from gorgona.stages.cleaners import *


@pytest.fixture()
def setup_html_cleaner() -> HtmlCleaner:
    html_cleaner = HtmlCleaner(
        'html',
        '',
    )

    return html_cleaner


def test_html_cleaner_no_tags(setup_html_cleaner):
    assert setup_html_cleaner('hello world') == 'hello world'


# single tags
def test_html_cleaner_single_open_tag(setup_html_cleaner):
    assert setup_html_cleaner('<br>') == ''


def test_html_cleaner_single_open_tag_with_attr(setup_html_cleaner):
    assert setup_html_cleaner('<p color="green">') == ''


def test_html_cleaner_single_closing_tag(setup_html_cleaner):
    assert setup_html_cleaner('</br>') == ''


def test_html_cleaner_single_paired_tag_without_content(setup_html_cleaner):
    assert setup_html_cleaner('<p></p>') == ''


def test_html_cleaner_single_paired_tag_without_content_with_attr(setup_html_cleaner):
    assert setup_html_cleaner('<p style="bold"></p>') == ''


def test_html_cleaner_single_paired_tag_with_content(setup_html_cleaner):
    assert setup_html_cleaner('<p>hello, world!</p>') == 'hello, world!'


def test_html_cleaner_single_paired_tag_with_content_with_attr(setup_html_cleaner):
    assert setup_html_cleaner('<p class="news">hello, world!</p>') == 'hello, world!'


# multiple tags
def test_html_cleaner_multiple_open_tags(setup_html_cleaner):
    assert setup_html_cleaner('<br><a><p>') == ''


def test_html_cleaner_multiple_open_tags_with_attrs(setup_html_cleaner):
    assert setup_html_cleaner('<br attr=""><a href="hello.world"><p color="red">') == ''


def test_html_cleaner_multiple_closing_tags(setup_html_cleaner):
    assert setup_html_cleaner('</br></a></p>') == ''


def test_html_cleaner_multiple_paired_tags_without_content(setup_html_cleaner):
    assert setup_html_cleaner('<a></a><p></p>') == ''


def test_html_cleaner_multiple_paired_tags_without_content_with_attrs(setup_html_cleaner):
    assert setup_html_cleaner('<a href="hello.world"></a><p color="blue"></p>') == ''


def test_html_cleaner_multiple_paired_tags_with_content(setup_html_cleaner):
    assert setup_html_cleaner('<a>link</a> <p>text</p>') == 'link text'


def test_html_cleaner_multiple_paired_tags_with_content_with_attrs(setup_html_cleaner):
    assert setup_html_cleaner('<a href="hello.world">link</a> <p font="helvetica">text</p>') == 'link text'
