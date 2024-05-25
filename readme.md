## This is for my personal use i am trying to store some useful library here


##### you can install this project by
#####  `git+https://github.com/Vivekkumar-IN/External-Plugins@main`


### ChatGpt


```python
from YUKKI import api

Api = api()

results= Api.chatgpt("hello ai")

print(results)
```
Result of print(results):

```python

{'results': 'Hello! How can I assist you today?', 'join': '@ZeroXCoderZChat', 'success': True}
```


### Random quote

```python
from YUKKI import api

Api = api()

results= Api.quote()

print(results)

```

Result of print(results):

```python


{'quote': 'The truest greatness lies in being kind, the truest wisdom in a happy mind.', 'author': 'Ella Wheeler Wilcox', 'join': '@ZeroXCoderZChat'}

```

### Write
```python
from YUKKI import api

Api = api()

text = "Jai shree Ram"

results= Api.write(text)

print(results)

```

Result of print(results):

```python
https://telegra.ph/file/63ff2e31cae67d511cfae.jpg
```





This Project is Licensed under [License](https://github.com/Vivekkumar-IN/External-Plugins/blob/main/LICENSE)