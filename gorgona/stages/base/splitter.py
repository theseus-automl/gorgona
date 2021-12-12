from gorgona.stages.base.base_stage import BaseStage


class Splitter(BaseStage):
    def __init__(
        self,
        name: str,
        regexp: str,
        join_on: str,
    ) -> None:
        super().__init__(
            name,
            regexp,
        )
        self._join_on = join_on

    def __call__(
        self,
        text: str,
        *args,
        **kwargs,
    ) -> str:
        return self._join_on.join(
            self._regexp.split(
                text,
                *args,
                **kwargs,
            ),
        )
