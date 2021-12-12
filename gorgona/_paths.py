from pathlib import Path

_CWD = Path(__file__).parents[1]

_MODELS_DIR = _CWD / 'models'
_MODELS_DIR.mkdir(
    exist_ok=True,
    parents=True,
)

_FT_MODEL_PATH = _MODELS_DIR / 'ld.176.bin'
