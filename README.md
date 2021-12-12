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

Each stage includes following parameters:
1. **type** - stage type
2. **name** - optional stage name. It can be useful for debug mode
3. **repl** - string to replace on for stages based on replacing
4. **join_on** - string to join on for stages based on splitting  

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

### 3. Development
Feel free to open issues, send pull requests and ask any questions!