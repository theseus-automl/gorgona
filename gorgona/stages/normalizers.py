from unicodedata import normalize

from gorgona.stages.base.base_stage import BaseStage
from gorgona.stages.base.replacer import Replacer


class UnicodeNormalizer(BaseStage):
    def __init__(
        self,
        name: str,
        mode: str,
    ) -> None:
        super().__init__(name)
        self._mode = mode

    def __call__(
        self,
        text: str,
        *args,
        **kwargs,
    ) -> str:
        return normalize(
            unistr=text,
            form=self._mode,
        )


class WhitespaceNormalizer(Replacer):
    def __init__(
        self,
        name: str,
        repl: str = ' ',
    ) -> None:
        super().__init__(
            name,
            r' +',
            repl,
        )
