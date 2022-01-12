import re
from string import punctuation

from emoji import EMOJI_DATA

from gorgona.stages.base.replacer import Replacer


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
            r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
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
            r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})',
            repl,
        )


class UrlCleaner(Replacer):
    def __init__(
        self,
        name: str,
        repl: str,
    ) -> None:
        super().__init__(
            name,
            r'^https?:\/\/.*[\r\n]*',
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
            r'@(\S+|$)',
            repl,
        )


class SpecialSymbolsCleaner(Replacer):
    def __init__(
        self,
        name: str,
        repl: str,
        exceptions: str = '',
    ) -> None:
        super().__init__(
            name,
            ''.join(ch for ch in punctuation if ch not in exceptions) if exceptions else punctuation,
            repl,
        )
