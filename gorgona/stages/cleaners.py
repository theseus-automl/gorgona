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
