from pathlib import Path
from setuptools import (
    find_packages,
    setup,
)
from typing import List

_CWD = Path(__file__).parent


def _get_requirements(
    file: Path,
) -> List[str]:
    reqs = []

    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()

            if line:
                reqs.append(line)

    return reqs


with open(_CWD / 'README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='gorgona',
    version='0.1.0',
    author='Timur Kasimov',
    description='Low-code text datasets preprocessor with parallelism support',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/theseus-automl/gorgona',
    packages=find_packages(),
    install_requires=_get_requirements(_CWD / 'requirements.txt'),
)
