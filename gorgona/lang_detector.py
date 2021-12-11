from pathlib import Path
from typing import Optional
from urllib.request import urlretrieve

from fasttext import load_model

from gorgona._paths import _FT_MODEL_PATH


class LanguageDetector:
    def __init__(
        self,
        model_path: Optional[Path],
    ) -> None:
        if model_path is None:
            if _FT_MODEL_PATH is None:
                self._download_model()

            self._model = load_model(str(_FT_MODEL_PATH))
        else:
            if not model_path.exists() or not model_path.is_file():
                raise OSError('language detection model does not exist or is not a file')

            self._model = load_model(str(model_path))

    def detect(
        self,
        text: str,
        threshold: float,
    ) -> str:
        pred = self._model.predict(
            text,
            threshold=threshold,
        )

        return pred

    @staticmethod
    def _download_model():
        urlretrieve(
            'https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin',
            _FT_MODEL_PATH,
        )
