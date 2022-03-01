# voice_assistent
This program is my graduation project. 
The program recognizes the human voice and executes commands. 
The list of commands is limited. You can also add new commands.

If you want to run this programm you need to make:
- setup Python v3.7-32bit; 
  you can use another versision Python, 
  however, I do not guarantee that everything will work correctly, 
  without the need to make changes to the code. 
- check setup this modules on yout system: os, time, random, webbrowser, speech_recognition, fuzzywuzzy, pyttsx3, datetime;
  if you do not have the listed modules installed, install them.
  
A stable internet connection is required for the program to work!
  
This program only works with commands in Russian. Command list who understand voice assistant:
   - "alias": ("кеша", "кеш", "инокентий", "иннокентий", "кишун", "киш", "кишаня", "киш", "кяша", "кэша"),
   - "tbr": ("скажи", "расскажи", "покажи", "сколько", "произнеси"),
   - "variantsTranslateReplace": ('переведи', 'перевести', 'переводить', 'перевод'),
   + "cmds": {
       - "hello": ("привет", "прив", "здравствуйте", "здравствуй", "добрые день", "доброго времени суток", "приветсвую"),
       - "farewell": ("пока", "прощай", "до скорых встреч"),
       - "ctime": ("текущее время", "сейчас времени", "который час"),
       - "year": ("текущий год", "какой сейчас год", "какой год"),
       - "month": ("какой месяц", "что за месяц", "в каком месяце"),
       - "day": ("какой сегодня день", "какой день недели", "день недели"),
       - "datetime": ("полная дата"),
       - "radio": ("включи музыку", "воспроизведи радио", "включи радио"),
       - "syper90": ("супердискотека 90-х", "супердискотека девяностых", "музыка девностых", "музыка 90-х"),
       - "pop": ("поп радио", "pop радио","поп музыка", "pop музыка"),
       - "dorojRad": ("дорожное радио"),
       - "ruskRadio": ("русское радио", "руское радио"),
       - "rock": ("рок музыка", "альтернативный рок", "метал"),
       - "classik": ("классическое радио", "класическое радио", "классическая музыка"),
       - "prank": ("расскажи анекдот", "рассмеши меня", "ты знаешь анекдот"),
       - "openVK": ("открой вк", "открой вконтакте", "вк", "вконтакте", "vk", "vkontakt"),
       - "openYoutube": ("открой ютуб", "youtube", "открой youtube"),
       - "openGoogle": ("открой гугл", "google", "запусти goodle", "гугл поиск", "запусти гугл"),
       - "openYandex": ("открой яндекс", "yandex", "запусти yandex", "яндекс поиск", "запусти яндекс", "открой браузер", "браузер", "открой сайт", "открой поиск"),
       - "powerOff": ("выключи компьютер", "выруби комп", "выключи шарманку"),
       - "translate": ("переведи фразу", "переведи", "как переводится", "перевод"),
       - "search": ("найди", "найти")
        }
        
If the program does not recognize your voice, it will tell you about it. 
