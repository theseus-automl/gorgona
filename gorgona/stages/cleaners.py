import re
from itertools import chain
from string import punctuation

from emoji import EMOJI_DATA
from phonenumbers import PhoneNumberMatcher
from phonenumbers.data import _COUNTRY_CODE_TO_REGION_CODE

from gorgona.stages.base.replacer import Replacer

_SUPPORTED_REGIONS = set(chain.from_iterable(list(_COUNTRY_CODE_TO_REGION_CODE.values())))

_UL = '\u00a1-\uffff'
_IPV4_RE = r'(?:25[0-5]|2[0-4]\d|[0-1]?\d?\d)(?:\.(?:25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}'
_IPV6_RE = r'\[[0-9a-f:\.]+\]'
_HOSTNAME_RE = r'[a-z' + _UL + r'0-9](?:[a-z' + _UL + r'0-9-]{0,61}[a-z' + _UL + r'0-9])?'
_DOMAIN_RE = r'(?:\.(?!-)[a-z' + _UL + r'0-9-]{1,63}(?<!-))*'
_TLD_RE = (
    r'\.'
    r'(?!-)'
    r'(?:[a-z' + _UL + '-]{2,63}'
    r'|xn--[a-z0-9]{1,59})'
    r'(?<!-)'
    r'\.?'
)
HOST_RE = '(' + _HOSTNAME_RE + _DOMAIN_RE + _TLD_RE + '|localhost)'


class HtmlCleaner(Replacer):
    def __init__(
        self,
        name: str,
        repl: str,
    ) -> None:
        super().__init__(
            name,
            r'<.*?>',
            repl,
        )


class EmailCleaner(Replacer):
    def __init__(
        self,
        name: str,
        repl: str,
    ) -> None:
        super().__init__(
            name,
            # r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            r"[a-z0-9!#$%&'*+/=?^_‘{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_‘{|}~-]+)*@"
            r"(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?",
            repl,
        )


class PhoneNumberCleaner(Replacer):
    def __init__(
        self,
        name: str,
        repl: str,
    ) -> None:
        super().__init__(
            name,
            '',
            repl,
        )

    def __call__(
        self,
        text: str,
    ) -> str:
        for region in _SUPPORTED_REGIONS:
            for number in PhoneNumberMatcher(text, region):
                text = text.replace(
                    number.raw_string,
                    self._repl,
                )

        return text


class UrlCleaner(Replacer):
    def __init__(
        self,
        name: str,
        repl: str,
    ) -> None:
        super().__init__(
            name,
            r'^(?:http|ftp)s?://'
            r'(?:\S+(?::\S*)?@)?'
            r'(?:' + _IPV4_RE + '|' + _IPV6_RE + '|' + HOST_RE + ')'
            r'(?::\d{2,5})?'
            r'(?:[/?#][^\s]*)?'
            r'\Z',
            repl,
        )


class EmojiCleaner(Replacer):
    def __init__(
        self,
        name: str,
        repl: str,
    ) -> None:
        super().__init__(
            name,
            u'(' + u'|'.join(re.escape(u) for u in sorted(EMOJI_DATA, key=len, reverse=True)) + u')',
            repl,
        )


class MentionCleaner(Replacer):
    def __init__(
        self,
        name: str,
        repl: str,
    ) -> None:
        super().__init__(
            name,
            r'\B@\S+',
            repl,
        )


class SpecialSymbolsCleaner(Replacer):
    def __init__(
        self,
        name: str,
        repl: str,
        exceptions: str = '',
    ) -> None:
        escaped = ''.join(re.escape(ch) for ch in punctuation)
        exceptions = set(exceptions)

        super().__init__(
            name,
            f"[{''.join(ch for ch in escaped if ch not in exceptions) if exceptions else escaped}]",
            repl,
        )


class NumberCleaner(Replacer):
    def __init__(
        self,
        name: str,
        repl: str,
    ) -> None:
        super().__init__(
            name,
            r'\b[-+]?\d*\.?\d+|[-+]?\d+\b',
            repl,
        )
