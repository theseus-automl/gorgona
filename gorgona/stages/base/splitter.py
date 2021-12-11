from gorgona.stages.base.base_stage import BaseStage


class Splitter(BaseStage):
    def __init__(
        self,
        name: str,
        regexp: str,
    ) -> None:
        super().__init__(
            name,
            regexp,
        )

    def __call__(
        self,
        text: str,
        *args,
        **kwargs,
    ) -> str:
        return self._regexp.split(
            text,
            *args,
            **kwargs,
        )
