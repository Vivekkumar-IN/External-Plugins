> [!NOTE]
> This is for my personal use if you want yo use so you can


##### Installation

```sh
pip install git+https://github.com/Vivekkumar-IN/TheApi@main
```

<details>
  <summary>Advice</summary>


  ```python

  from TheApi import api

  advice = api.get_advice()
  
  print(advice)

  ```

  Result of print(advice):

  ```python
  
If you are feeling down, try holding a pencil between your top lip and your nose for five minutes.

  ```
</details>

<details>
  <summary>Cat</summary>


  ```python

  from TheApi import api

  image = api.cat()
  
  print(image)

  ```

  Result of print(image):

  ```python
  
https://cdn2.thecatapi.com/images/1sk.jpg
  ```
</details>


<details>
  <summary>ChatGpt</summary>


  ```python
  from TheApi import api

  results= api.chatgpt("hello ai")

  print(results)
  ```
  Result of print(results):

  ```python

  Hello! How can I assist you today?
  ```

</details>
 


<details>
  <summary>Dog</summary>


  ```python

  from TheApi import api

  image = api.dog()
  
  print(advice)

  ```

  Result of print(image):

  ```python
  
https://random.dog/1f1d51c0-cdf7-4efb-8ae0-ecd7d6f73481.jpeg
  ```
</details>


<details>
  <summary>GitHub search</summary>


  ```python

  from TheApi import api
  
  query = "YukkiMusic"

  max_results = 10
  
  results = api.github_search(query, max_results)
  
  print(results)

  ```

  Result of print(results):

  ```python
  

[{'name': 'YukkiMusicBot', 'full_name': 'TeamYukki/YukkiMusicBot', 'description': 'Telegram Group Calls Streaming bot with some useful features, written in Python with Pyrogram and Py-Tgcalls. Supporting platforms like Youtube, Spotify, Resso, AppleMusic, Soundcloud and M3u8 Links.', 'url': 'https://github.com/TeamYukki/YukkiMusicBot'}, {'name': 'YukkiMusic-Old', 'full_name': 'NowayXD/YukkiMusic-Old', 'description': 'veez mega ( private music bot )', 'url': 'https://github.com/NowayXD/YukkiMusic-Old'}, {'name': 'YukkiMusicBot', 'full_name': 'YukkiOwner/YukkiMusicBot', 'description': 'About Telegram Group Calls Streaming bot with some useful features, written in Python with Pyrogram and Py-Tgcalls. Supporting platforms like Youtube, Spotify, Resso, AppleMusic, Soundcloud and M3u8 Links.', 'url': 'https://github.com/YukkiOwner/YukkiMusicBot'}, {'name': 'Testing-Alpha', 'full_name': 'SexyShekharXD/Testing-Alpha', 'description': 'YukkiMusic with new pyrogram v2 and pytgcalls with ntgcalls implimentation', 'url': 'https://github.com/SexyShekharXD/Testing-Alpha'}, {'name': 'YukkiMusic', 'full_name': 'crazyworld-izzy/YukkiMusic', 'description': None, 'url': 'https://github.com/crazyworld-izzy/YukkiMusic'}, {'name': 'YukkiMusicOld', 'full_name': 'Randi356/YukkiMusicOld', 'description': None, 'url': 'https://github.com/Randi356/YukkiMusicOld'}, {'name': 'YukkiMusic', 'full_name': 'TheTeamVivek/YukkiMusic', 'description': 'YukkiMusic based on YukkiMusicBot', 'url': 'https://github.com/TheTeamVivek/YukkiMusic'}, {'name': 'YukkiMusicBot', 'full_name': 'Rahulsharma45/YukkiMusicBot', 'description': None, 'url': 'https://github.com/Rahulsharma45/YukkiMusicBot'}, {'name': 'https-github.com-TeamYukki-YukkiMusicBot', 'full_name': 'supernovark/https-github.com-TeamYukki-YukkiMusicBot', 'description': None, 'url': 'https://github.com/supernovark/https-github.com-TeamYukki-YukkiMusicBot'}, {'name': 'Yukkimusic', 'full_name': 'EkooNihh/Yukkimusic', 'description': 'https://github.com/TeamYukki/YukkiMusicBot', 'url': 'https://github.com/EkooNihh/Yukkimusic'}]

  ```
</details>

<details>
  <summary>Hashtags </summary>


  ```python
  from TheApi import api

  text = "telegram"

  hashtags = api.gen_hashtag(text)

  print(hashtags)

  ```
  Result of print(hashtags):

  ```python

  
Hashtags:
#telegram  #telegramchannel  #telegrama  #telegramstickers  #telegram0123378624  #telegramtakeover  #telegramaanimado  #telegrambot  #telegramer  #telegramstickerpack  #telegramsams  #telegramsam  #Telegrams  #telegramma  #telegramgp  #TelegramIsBetter

 similar hashtags:
#telegramchannel #telegrama #telegramstickers #telegram0123378624 #telegramtakeover #telegramaanimado #telegrambot #telegramer #telegramstickerpack #telegramsams #telegramsam #Telegrams #telegramma #telegramgp #TelegramIsBetter
  ```
</details>

<details>
  <summary>Imagine</summary>


  ```python
  from TheApi import api

  image = api.imagine("A Litte Boy Walking in roadside")

  print(image)

  ```
  Result of print(image):

  ```python

  https://telegra.ph/file/057191058512f73cf5ed7.jpg
  ```
</details>


<details>
<summary>Jokes</summary>


  ```python
  import json
  from TheApi import api

  data = api.get_jokes() # for only one jokes
 
  print("This will print only One Joke\n" + data)

  jokes = api.get_jokes(3) # You can get jokes up to 10 make sure the amount of jokes is minimum 1 and maximum 10

  ```

  results of print
  ```python
  This will print only One Joke

My ex had an accident. I told the paramedics the wrong blood type for her. She'll finally experience what rejection is really like.

  This will print only 3 Joke

  1. Being a self-taught developer is almost the same as being a cut neck chicken because you have no sense of direction in the beginning.

  2. Four engineers get into a car. The car won't start.
  The Mechanical engineer says "It's a broken starter".
  The Electrical engineer says "Dead battery".
  The Chemical engineer says "Impurities in the gasoline".
  The IT engineer says "Hey guys, I have an idea: How about we all get out of the car and get back in".

  3. I've got a really good UDP joke to tell you but I don’t know if you'll get it.

  ```

</details>
 

<details>
  <summary>Hindi Joke </summary>


  ```python
  from TheApi import api

  joke = api.get_hindi_jokes()

  print(joke)

  ```
  Result of print(joke):

  ```python

  हमारे समाज में रीति रिवाज और प्रथाएं इतनी महान है कि एक निकम्मा पुरुष भी विवाह के बाद परमेश्वर बन जाता है 😆🤣😋😉
  ```
</details>


<details>
  <summary>Morse</summary>
  
  morse encode

  ```python

  from TheApi import api

  text = "HELLO WORLD"

  encoded = api.morse_code(text)

  print(encoded)
  ```

  Result of print(encoded):

  ```python
  .... . .-.. .-.. - / . - .-. .-.. -..

  ```

  Decode


  ```python

  from TheApi import api

  encoded = ".... . .-.. .-.. - / . - .-. .-.. -.."

  decoded = api.morse_code(encoded)

  print(decoded)
  ```

  Result of print(decoded):

  ```python
  HELLO WORLD

  ```
</details>



<details>
  <summary>Random quote</summary> 

  ```python
  from TheApi import api

  results= api.quote()

  print(results)

  ```

  Result of print(results):

  ```python

  The truest greatness lies in being kind, the truest wisdom in a happy mind. 
  author - Ella Wheeler Wilcox

  ```
</details>




<details>
<summary>Telegraph Text</summary>

  ```python
  from TheApi import api
  title = "A Title for telegraph page"
  query = "text that you want to upload to telegraph"
  results= api.telegraph(title,query)

  print(results)

  ```
  Result of print(results):

  ```python

  https://telegra.ph/A-Title-for-telegraph-page-05-25

   ```
</details>

<details>
  <summary>Useless Fact</summary>


  ```python

  from TheApi import api

  fact = api.get_uselessfact()

  print(fact)
  ```

  Result of print(word):

  ```python
  
In Aspen Colorado, you can have a maximum income of $104,000 and still receive government subsidized housing.

  ```
</details>


<details>
  <summary>Wikipedia</summary>


  ```python

  from TheApi import api

  text = "Python (programming language)"

  results= api.wikipedia(text)

  print(results)
  ```

  Result of print(results):

  ```python
  
{'title': 'Python (programming language)', 'summary': 'Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.\nPython is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.\nGuido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0. Python 2.0 was released in 2000. Python 3.0, released in 2008, was a major revision not completely backward-compatible with earlier versions. Python 2.7.18, released in 2020, was the last release of Python 2.\nPython consistently ranks as one of the most popular programming languages, and has gained widespread use in the machine learning community.\n\n', 'url': 'https://en.wikipedia.org/?curid=23862', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/500px-Python-logo-notext.svg.png'}
  ```
</details>

<details>
  <summary>Word</summary>


  ```python

  from TheApi import api

  word = api.words(5)

  print(word)
  ```

  Result of print(word):

  ```python
  ['micropublishers', 'nonlife', 'pollutes', 'fedexed', 'cissy']

  ```
</details>



<details>
  <summary>Random Word</summary>


  ```python

  from TheApi import api

  word = api.randomword()

  print(word)
  ```

  Result of print(word):

  ```python
  teroxide

  ```
</details>



<details>
  <summary>Write</summary>


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
</details>


This Project is Licensed under [License](https://github.com/Vivekkumar-IN/TheApi)
