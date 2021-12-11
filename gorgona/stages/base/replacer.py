from gorgona.stages.base.base_stage import BaseStage


class Replacer(BaseStage):
    def __init__(
        self,
        name: str,
        regexp: str,
        repl: str,
    ) -> None:
        super().__init__(
            name,
            regexp,
        )
        self._repl = repl

    def __call__(
        self,
        text: str,
    ) -> str:
        return self._regexp.sub(
            self._repl,
            text,
        )
