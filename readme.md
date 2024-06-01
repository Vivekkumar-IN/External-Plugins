## This is for my personal use i am trying to store some useful library here


##### you can install this project by
#####  
```sh
pip install git+https://github.com/Vivekkumar-IN/TheApi@main
```

</details>

Image with Text
  <summary>Example of how to use</summary>

<details>
### ChatGpt


```python
from TheApi import api

results= api.chatgpt("hello ai")

print(results)
```
Result of print(results):

```python

{'results': 'Hello! How can I assist you today?', 'join': '@vk_zone', 'success': True}
```


### Random quote

```python
from TheApi import api

results= api.quote()

print(results)

```

Result of print(results):

```python


{'quote': 'The truest greatness lies in being kind, the truest wisdom in a happy mind.', 'author': 'Ella Wheeler Wilcox', 'join': '@vk_zone'}

```

### Write
```python
from TheApi import api

text = "Jai shree Ram"

results= api.write(text)

print(results)

```

Result of print(results):

```python
https://telegra.ph/file/63ff2e31cae67d511cfae.jpg
```


### Telegraph text

```python
from TheApi import api
title = "A Title for telegraph page"
query = "text that you want to upload to telegraph"
results= api.telegraph(title,query)

print(results)

```
Result of print(results):

```python

{'results': 'https://telegra.ph/A-Title-for-telegraph-page-05-25', 'join': '@vk_zone', 'success': True}

```

### Jokes
```python
import json
from TheApi import api

response = api.get_jokes()

data = json.loads(response)

jokes = data["jokes"]
num = 1
Jokes = ""
if isinstance(jokes, dict):
    
    for key in jokes:
        a = jokes[key]
        Jokes+=(f"{num}. {a}\n\n")
        num+=1
    print(Jokes)

else:
    print(jokes["joke"])
```

results of print
```python

1. Two fish in a tank. One turns to the other and says, "Do you know how to drive this thing?"

```

```python

response = api.get_jokes()
# This will return 1 Jokes

response = api.get_jokes(2)
# This will return 1 Jokes

# like this you can get 10 Jokes

# if the number is greater then 10 in cause an exception returns 

# Example : 

import json
from TheApi import api

response = api.get_jokes(13)

data = json.loads(response)

jokes = data["jokes"]
num = 1
Jokes = ""
if isinstance(jokes, dict):
    
    for key in jokes:
        a = jokes[key]
        Jokes+=(f"{num}. {a}\n\n")
        num+=1
    print(Jokes)

else:
    print(jokes["joke"])

# in this api.get_jokes(13) the jokes is greater then 10 so the an exception returns 


raise InvalidAmountError(amount)
YUKKI.errors.InvalidAmountError: Invalid amount of jokes requested: 11. Maximum allowed is 10. Minimum allowed is 1.

```

### Hindi Jokes
```python
from TheApi import api

joke = api.get_hindi_jokes()

print(joke)
```
results of print:
```python

हमारे समाज में रीति रिवाज और प्रथाएं इतनी महान है कि एक निकम्मा पुरुष भी विवाह के बाद परमेश्वर बन जाता है 😆🤣😋😉
```


This Project is Licensed under [License](https://github.com/Vivekkumar-IN/External-Plugins/blob/main/LICENSE)
