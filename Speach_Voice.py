import os
import time
import random
import webbrowser
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime

# Глобальный массив данных с определением команды
opts = {
    "alias": ("кеша", "кеш", "инокентий", "иннокентий", "кишун", "киш", "кишаня", "киш", "кяша", "кэша"),
    "tbr": ("скажи", "расскажи", "покажи", "сколько", "произнеси"),
    "variantsTranslateReplace": ('переведи', 'перевести', 'переводить', 'перевод'),
    "cmds": {
        "hello": ("привет", "прив", "здравствуйте", "здравствуй", "добрые день", "доброго времени суток", "приветсвую"),
        "farewell": ("пока", "прощай", "до скорых встреч"),
        "ctime": ("текущее время", "сейчас времени", "который час"),
        "year": ("текущий год", "какой сейчас год", "какой год"),
        "month": ("какой месяц", "что за месяц", "в каком месяце"),
        "day": ("какой сегодня день", "какой день недели", "день недели"),
        "datetime": ("полная дата"),
        "radio": ("включи музыку", "воспроизведи радио", "включи радио"),
        "syper90": ("супердискотека 90-х", "супердискотека девяностых", "музыка девностых", "музыка 90-х"),
        "pop": ("поп радио", "pop радио","поп музыка", "pop музыка"),
        "dorojRad": ("дорожное радио"),
        "ruskRadio": ("русское радио", "руское радио"),
        "rock": ("рок музыка", "альтернативный рок", "метал"),
        "classik": ("классическое радио", "класическое радио", "классическая музыка"),
        "prank": ("расскажи анекдот", "рассмеши меня", "ты знаешь анекдот"),
        "openVK": ("открой вк", "открой вконтакте", "вк", "вконтакте", "vk", "vkontakt"),
        "openYoutube": ("открой ютуб", "youtube", "открой youtube"),
        "openGoogle": ("открой гугл", "google", "запусти goodle", "гугл поиск", "запусти гугл"),
        "openYandex": ("открой яндекс", "yandex", "запусти yandex", "яндекс поиск", "запусти яндекс", "открой браузер", "браузер", "открой сайт", "открой поиск"),
        "powerOff": ("выключи компьютер", "выруби комп", "выключи шарманку"),
        "translate": ("переведи фразу", "переведи", "как переводится", "перевод"),
        "search": ("найди", "найти")
    }
}

prankList = ['Циля Соломоновна, а сколько у вас было мужей? Всего или своих', 'Фраза "жизнь коротка" побуждает людей к поступкам, которые делают ее еще короче.', 'С 9 июня все москвичи, которые будут сидеть дома, обязаны заплатить штраф 5000 рублей за нарушение режима отмены режима самоизоляции.', 'У сына в 9-ом классе новый предмет - "Карьера". Вести его будет большой специалист в этом деле - трудовик.', 'Только начинаешь привыкать к хорошему, как жизнь становится ещё лучше.', '– Какой у тебя ICQ? – Не ниже, чем у других!', 'Девушка сказала, что я у нее первый, но шрам от кесарева как-то напрягал...',
         'Мужик жалуется приятелю: Весь день не спал. Всю ночь не ел. Понятное дело, устаешь!', 'Вы к нам почаще заходите, без вас потом так хорошо.', '- Пустота убивает... - В душе? - В холодильнике.', '- От меня жена ушла. - А ты на кухне смотрел?', '- Сына, купил тебе новую Саll оf Dutу в 3D. - Пап, это же авиабилет до Сирии... - Так ты определись уже, любишь воевать или нет.', 'Дураков не нужно учить, они необучаемы. Но платёжеспособны. В этом суть тренингов.', '- В мой компьютер попал вирус. - Ну и что же ты сделал? - Прививку. - Куда?! - Под мышку...']

hiMes = ['О, здравствуй, мой драгоценный друг!', 'Добрый день, повелитель', 'Здравствуйте, несказанно рад видеть вашу физиономию перед собой!',
            'Мне кажется, или я реально тебя вижу!', 'Не верю своим глазам! А ну-ка, протри-ка мне стекла!']

obrMes = ['Кеша слушает', 'Иннокентий на связи',
            'Кеша ответит на твой запрос, если знает ответ', 'Что хотите узнать']

farMes = ['До скорой встречи!', 'Пока! Будь здоров.', 'Бывай! Пока.', 'Всего доброго!']

variantsTranslateReplace = ['переведи', 'перевести', 'переводить', 'перевод']

# Говорить
def speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()

# Вызывается каждый раз при произнесенной фразе в микрофон
def callback():
    r = sr.Recognizer()
    m = sr.Microphone()

    with m as source:
        print("Скажите команду: ")
        audio = r.listen(source)

    # spot_listenting = r.listen_in_background(m, callback)
    # while True: time.sleep(0.1) # infinite loop

    try:
        global voice
        voice = r.recognize_google(audio, language="ru").lower()
        # voice = ('vwebt').lower()
        print("[log] Распознано: " + voice)
        cmd = voice
        # Корректировка полученной строки и выполнение команды
        if voice.startswith(opts["alias"]):
            correct(cmd)
        else:
            correct(cmd)

    except sr.UnknownValueError:
        print("[log] Голос не распознан!")
    except sr.RequestError as e:
        print("[log] Неизвестная ошибка, проверьте интернет")

# Коррекция принятой строки
def correct(cmd):
    for x in opts["alias"]:
        cmd = cmd.replace(x, "").strip()

    for x in opts["tbr"]:
        cmd = cmd.replace(x, "").strip()

    # Распознаем и выполняем команду
    cmdс = recognize_cmd(cmd)
    print("Факт выполнения команды" + str(cmdс))
    execute_cmd(cmdс)

# Нечеткий поиск команды, которую получил Кеша
def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c, v in opts['cmds'].items():

        for x in v:
            vrt = fuzz.token_set_ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
    return RC

# Преобразование команды в действие
def execute_cmd(cmd):
    if cmd.get('cmd') == 'ctime':
        # Сказать текущее время
        now = datetime.datetime.now()
        speak("Сейчас " + str(now.hour) + ":" + str(now.minute))

    elif cmd.get('cmd') == 'year':
        # Сказать текущий год
        now = datetime.datetime.now()
        speak("Сейчас " + str(now.year) + " год")

    elif cmd.get('cmd') == 'month':
        # Сказать текущий месяц
        now = datetime.datetime.now()
        speak("Сейчас " + str(now.strftime('%B')) + " месяц. Порядковый номер " + str(now.month))

    elif cmd.get('cmd') == 'day':
        # Сказать текущий день недели
        now = datetime.datetime.today()
        speak("Сегодня " + str(now.strftime('%A')))

    elif cmd.get('cmd') == 'datetime':
        # Сказать полную дату
        now = datetime.datetime.now()
        speak("Сегодня " + str(now.year) + " год " + str(now.month) + " месяц." +
              " День недели "+str(now.day) + " время " + str(now.hour) + ":" + str(now.minute))

    elif cmd.get('cmd') == "radio":
        # Воспроизвести рандомное радио
        radio()

    elif cmd.get('cmd') == "syper90":
        # Воспроизвести радио супер 90-е
        syper90()

    elif cmd.get('cmd') == "pop":
        # Воспроизвести радио поп
        pop()

    elif cmd.get('cmd') == "dorojRad":
        # Воспроизвести радио дорожное
        dorojRad()

    elif cmd.get('cmd') == "ruskRadio":
        # Воспроизвести русское радио
        ruskRadio()

    elif cmd.get('cmd') == "rock":
        # Воспроизвести рок радио
        rock()

    elif cmd.get('cmd') == "classik":
        # Воспроизвести классическое радио радио
        classik()

    elif cmd.get('cmd') == 'prank':
        # Рассказать рандомный анекдот анекдот
        prank()

    elif cmd.get('cmd') == 'openVK':
        # Открыть ВК
        openVK()

    elif cmd.get('cmd') == 'openYoutube':
        # Открыть YouTube
        openYoutube()

    elif cmd.get('cmd') == 'openBrowser':
        # Открыть Браузер
        openBrowser()

    elif cmd.get('cmd') == 'openGoogle':
        # Открыть Google
        openGoogle()

    elif cmd.get('cmd') == 'openYandex':
        # Открыть Yandex
        openYandex()

    elif cmd.get('cmd') == 'hello':
        # Приветсвие
        speak(random.choice(hiMes))

    elif cmd.get('cmd') == 'farewell':
        # Прощание
        speak(random.choice(farMes))

    elif cmd.get('cmd') == 'powerOff':
        # Выключить компьютер
        os.system('shutdown /s /f /t 60')
    
    elif cmd.get('cmd') == 'translate':
        # Перевод
        checkTranslate()
    
    elif cmd.get('cmd') == 'search':
        # Поиск в браузере
        searchInBrowser()
 
    else:
        print('Команда не распознана, повторите!')


def radio():
    allRadio = ['http://air.radiorecord.ru:8102/sd90_320', 'http://ice-the.musicradio.com/CapitalXTRANationalMP3', 'http://dorognoe.hostingradio.ru:8000/dorognoe',
                'http://play.russianradio.eu/stream', 'http://galnet.ru:8000/hard', 'http://stream.srg-ssr.ch/m/rsc_de/mp3_128']
    webbrowser.open(random.choice(allRadio))

def syper90():
    webbrowser.open('http://air.radiorecord.ru:8102/sd90_320')

def pop():
    webbrowser.open('http://ice-the.musicradio.com/CapitalXTRANationalMP3')

def dorojRad():
    webbrowser.open('http://dorognoe.hostingradio.ru:8000/dorognoe')

def ruskRadio():
    webbrowser.open('http://play.russianradio.eu/stream')

def rock():
    webbrowser.open('http://galnet.ru:8000/hard')

def classik():
    webbrowser.open('http://stream.srg-ssr.ch/m/rsc_de/mp3_128')

def prank():
    speak(random.choice(prankList))

def openVK():
    webbrowser.open('https://vk.com/')

def openYoutube():
    webbrowser.open('https://www.youtube.com/')

def openGoogle():
    webbrowser.open('https://www.google.ru/')

def openYandex():
    webbrowser.open('https://yandex.ru/')

def checkTranslate():
    global voice, tr 
    tr = 0
    for x in opts["variantsTranslateReplace"]:
        if (x in voice)&(tr == 0):
            words = voice
            words = words.replace(x, "").strip()
            webbrowser.open('https://translate.yandex.ru/?lang=auto&text={}'.format(words))
            tr = 1
            words = ''

def searchInBrowser():
    global voice
    if 'найди' in voice:
        wordForSearch = voice.replace('найди', '').strip()
        webbrowser.open('https://yandex.ru/search/?text={}&lr=12'.format(wordForSearch))
    elif 'найти' in voice:
        wordForSearch = voice.replace('найди', '').strip()
        webbrowser.open('https://yandex.ru/search/?text={}&lr=12'.format(wordForSearch))
    else:
        print('Извините я не понял о чем идет речь. Повторите пожалуйста')


if __name__ == '__main__':
    print("Well")
    speak_engine = pyttsx3.init()

    # Только если у вас установлены голоса для синтеза речи!
    voices = speak_engine.getProperty('voices')
    if(speak_engine.setProperty('voice', voices[4].id) != True):
        pass
    else:
        speak_engine.setProperty('voice', voices[4].id)

    # Приветствующие фразы
    speak(random.choice(hiMes))
    speak(random.choice(obrMes))
    
    # Зацикливание для непрерывного использоваия программы
    while True:
        callback()
