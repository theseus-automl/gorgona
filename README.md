# gorgona
Gorgona allows you to preprocess your text datasets without writing a lot of code.

### 1. Installation
For now, only Python 3.8 is supported. You can try other versions, but no guarantees that it'll work properly.  

Clone repository:
```
git clone https://github.com/theseus-automl/gorgona
cd gorgona
```

Install package:
```
python setup.py install
```

### 2. Usage
First, you need to create YAML configuration file. Let's start with **stages** section review:
```yaml
stages:
  - type: "unicode"
    form: "nfkd"

  - type: "html"
    repl: ""

  - type: "email"
    repl: ""

  - type: "phone"
    repl: ""

  - type: "url"
    repl: ""

  - type: "emoji"
    repl: ""

  - type: "whitespace"
    repl: ""

  - type: "strip"
```

Each stage may includes following parameters:
1. **type** - stage type
2. **name** - optional stage name. It can be useful for debug mode
3. **repl** - string to replace on for stages based on replacing
4. **join_on** - string to join on for stages based on splitting  

Language detection stage is a bit more complex and may include such parameters:
1. **model_path** - path to FastText model for language detection. You can download it from [here](https://fasttext.cc/docs/en/language-identification.html) or left it to Gorgona
2. **target_lang** - texts in languages different from the target are replaced with empty strings
3. **threshold** - max threshold for set language to unknown

You can use **defaults** section to set custom default **repl** and **join_on** for all stages:
```yaml
defaults:
  repl: ""
  join_on: " "
```  

Now, you can import **Runner** and start preprocessing:
```python
from pathlib import Path
from gorgona import Runner

# create Runner instance, set path to config and number of workers
r = Runner(Path('config.yaml'), 4)

# get your texts
texts = [...]

# start preprocessing
res = r.run(texts)
```  

Previous example uses **multiprocessing** as a backend, but **Ray** is also supported. If you don't know how to set up a cluster, Ray has beautiful [docs](https://docs.ray.io/en/latest/index.html):
```python
r = Runner(Path('config.yaml'), 4, backend='ray', ray_cluster_address='<address>')
```

You can also use **Preprocessor** separately in your code:
```python
from pathlib import Path
from gorgona import Preprocessor

# create Preprocessor instance and set path to config
pr = Preprocessor(Path('config.yaml'))

# call Preprocessor on your text
pr('hello, world!')
```  

**Preprocessor** also supports debug mode, where you can view every stage result:
```python
pr('hello, world!', True)

# output:
# GORGONA DEBUG MODE
# RUNNING STAGE #0: stage 0
# BEFORE: ...
# AFTER: ...
# -------------------------
# RUNNING STAGE #1: stage 1
# BEFORE: ...
# AFTER: ...
# -------------------------
```  

### 3. Writing custom stages
Important notes:
1. You must inherit from any of the base stages
2. You must use **register** decorator on your class. Provided alias is used to identify your stage when parsing config
3. No duplicate aliases are allowed

There are two base stages to choose from:
- **BaseStage** is the most flexible one. You can do anything in call method, for example:
```python
from gorgona.stages import BaseStage, register

@register(alias='my_stage')
class MyStage(BaseStage):
    def __init__(self, name, regexp):
        super().__init__(name, regexp)

    def __call__(self, text, *args, **kwargs):
        print('this is my stage!')
        
        text = self._regexp.sub(':)', text)

        return text
```
- **Replacer** allows you to create convenient text replacement stages. For example, standard HtmlClenaer is a Replacer:
```python
from gorgona.stages import Replacer

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
```


### 4. Development
Feel free to open issues, send pull requests and ask any questions!