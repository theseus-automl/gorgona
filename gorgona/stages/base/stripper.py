from gorgona.stages.base.base_stage import BaseStage


class Stripper(BaseStage):
    def __init__(
        self,
        name: str,
    ) -> None:
        super().__init__(name)

    def __call__(
        self,
        text: str,
    ) -> str:
        return text.strip()
